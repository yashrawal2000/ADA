from __future__ import annotations

import pandas as pd

from app.core.indicators import atr, ema, normalize_0_1, rsi, volume_zscore, vwap
from app.models.schemas import InstrumentInput, TradeIntelligence
from app.services.dealer import DealerPositioningEngine
from app.services.flow import InstitutionalFlowDetector
from app.services.gamma import GammaEngine
from app.services.options_intel import OptionsIntelligenceEngine
from app.services.regime import Regime, RegimeDetector
from app.services.risk import RiskEngine


class TradingIntelligenceEngine:
    def __init__(self) -> None:
        self.regime_detector = RegimeDetector()
        self.options_engine = OptionsIntelligenceEngine()
        self.gamma_engine = GammaEngine()
        self.dealer_engine = DealerPositioningEngine()
        self.flow_engine = InstitutionalFlowDetector()
        self.risk_engine = RiskEngine()

    def _candles_df(self, candles) -> pd.DataFrame:
        return pd.DataFrame([c.model_dump() for c in candles])

    def evaluate(
        self,
        payload: InstrumentInput,
        account_equity: float,
        daily_drawdown: float,
        consecutive_losses: int,
    ) -> TradeIntelligence:
        df_5m = self._candles_df(payload.ohlcv_5m)
        regime, regime_conf = self.regime_detector.detect(df_5m)

        atr_value = atr(df_5m)
        rsi_val = rsi(df_5m["close"])
        vwap_val = vwap(df_5m)
        vol_z = volume_zscore(df_5m["volume"])
        ema20 = float(ema(df_5m["close"], 20).iloc[-1])
        ema50 = float(ema(df_5m["close"], 50).iloc[-1])
        ema200 = float(ema(df_5m["close"], 200).iloc[-1])

        options_intel, oi_strength = self.options_engine.compute(payload.options_chain, payload.spot)
        gamma_regime, gamma_flip, gamma_modifier = self.gamma_engine.compute(payload.options_chain, payload.spot)
        dealer_delta, dealer_score = self.dealer_engine.compute(payload.options_chain)

        vwap_strength = (payload.spot - vwap_val) / max(vwap_val, 1e-6)
        delivery_spike = payload.delivery_percent - 50
        flow_score = self.flow_engine.compute(vol_z, payload.order_imbalance, delivery_spike, vwap_strength)

        ml_probability = normalize_0_1((rsi_val - 50) + (ema20 - ema50) + (ema50 - ema200), -150, 150)
        sentiment = normalize_0_1(payload.futures_price - payload.spot, -100, 100)
        volume_strength = normalize_0_1(vol_z, -3, 3)
        liquidity_factor = normalize_0_1(df_5m["volume"].iloc[-1], 1_000, 2_000_000)
        volatility_penalty = max(0.2, normalize_0_1(payload.india_vix, 10, 30))

        edge_raw = (
            0.35 * ml_probability
            + 0.25 * oi_strength
            + 0.15 * sentiment
            + 0.15 * volume_strength
            + 0.10 * regime_conf
        )

        edge = (edge_raw * liquidity_factor / volatility_penalty) * gamma_modifier
        edge_score = max(0.0, min(100.0, edge * 100))

        buy_probability = max(0.0, min(100.0, (0.55 * ml_probability + 0.25 * flow_score + 0.2 * dealer_score) * 100))
        sell_probability = 100 - buy_probability
        confidence = max(0.0, min(1.0, 0.4 * edge + 0.3 * regime_conf + 0.3 * flow_score))

        stop_atr = 0.9
        target_atr = 1.8
        stop_loss_distance = atr_value * stop_atr
        high_vol = regime in {Regime.VOL_EXPANSION}
        position_size = self.risk_engine.position_size_percent(
            account_equity=account_equity,
            stop_loss_distance=stop_loss_distance,
            spot=payload.spot,
            volatility_regime=high_vol,
        )

        can_trade, reason = self.risk_engine.can_trade(
            daily_drawdown=daily_drawdown,
            consecutive_losses=consecutive_losses,
            event_risk=payload.economic_event_risk,
        )

        regime_aligned = regime in {Regime.TRENDING, Regime.RANGING}
        oi_aligned = oi_strength > 0.55
        rr_ok = target_atr / max(stop_atr, 1e-6) >= 1.5

        signal = "No Trade — insufficient edge"
        if can_trade and edge_score > 70 and regime_aligned and oi_aligned and rr_ok:
            signal = "Buy Bias" if buy_probability >= sell_probability else "Sell Bias"
        elif reason:
            signal = "No Trade — risk halt"

        return TradeIntelligence(
            edge_score=round(edge_score, 2),
            buy_probability=round(buy_probability, 2),
            sell_probability=round(sell_probability, 2),
            regime=regime,
            gamma_regime=gamma_regime,
            oi_strength=round(oi_strength, 2),
            flow_score=round(flow_score, 2),
            position_size_percent=round(position_size, 2),
            stop_loss=f"{stop_atr} ATR",
            target=f"{target_atr} ATR",
            confidence=round(confidence, 2),
            signal=signal,
            reason=reason,
        )
