from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class Regime(str, Enum):
    TRENDING = "Trending"
    RANGING = "Ranging"
    VOL_EXPANSION = "Volatility Expansion"
    VOL_COMPRESSION = "Volatility Compression"


class GammaRegime(str, Enum):
    POSITIVE = "Positive"
    NEGATIVE = "Negative"
    FLIP = "Flip Zone"


class OIClassification(str, Enum):
    LONG_BUILDUP = "Long Buildup"
    SHORT_BUILDUP = "Short Buildup"
    SHORT_COVERING = "Short Covering"
    LONG_UNWINDING = "Long Unwinding"


class OptionStrike(BaseModel):
    strike: float
    call_oi: float
    put_oi: float
    call_iv: float
    put_iv: float
    call_delta: float
    put_delta: float
    call_gamma: float
    put_gamma: float
    call_ltp: float
    put_ltp: float


class Candle(BaseModel):
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float


class InstrumentInput(BaseModel):
    symbol: str
    spot: float
    futures_price: float
    india_vix: float
    delivery_percent: float
    order_imbalance: float = Field(description="-1 to +1")
    economic_event_risk: bool = False
    ohlcv_1m: List[Candle]
    ohlcv_5m: List[Candle]
    ohlcv_15m: List[Candle]
    options_chain: List[OptionStrike]


class TradeIntelligence(BaseModel):
    edge_score: float
    buy_probability: float
    sell_probability: float
    regime: Regime
    gamma_regime: GammaRegime
    oi_strength: float
    flow_score: float
    position_size_percent: float
    stop_loss: str
    target: str
    confidence: float
    signal: str
    reason: Optional[str] = None


class StrikeIntel(BaseModel):
    strike: float
    classification: OIClassification
    weighted_buildup: float


class OptionsIntel(BaseModel):
    pcr_trend: float
    iv_rank: float
    max_pain: float
    concentration_zones: List[float]
    strike_intel: List[StrikeIntel]


class BacktestResult(BaseModel):
    sharpe_ratio: float
    max_drawdown: float
    win_rate: float
    total_trades: int
    slippage_cost: float
    brokerage_cost: float
