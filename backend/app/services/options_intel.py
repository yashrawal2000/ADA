from __future__ import annotations

import statistics
from typing import List

from app.models.schemas import OIClassification, OptionStrike, OptionsIntel, StrikeIntel


class OptionsIntelligenceEngine:
    def classify_strike(self, s: OptionStrike) -> OIClassification:
        net_price_move = s.call_ltp - s.put_ltp
        net_oi_move = s.call_oi - s.put_oi
        if net_price_move > 0 and net_oi_move > 0:
            return OIClassification.LONG_BUILDUP
        if net_price_move < 0 and net_oi_move > 0:
            return OIClassification.SHORT_BUILDUP
        if net_price_move > 0 and net_oi_move < 0:
            return OIClassification.SHORT_COVERING
        return OIClassification.LONG_UNWINDING

    def compute(self, options_chain: List[OptionStrike], spot: float) -> tuple[OptionsIntel, float]:
        strikes = sorted(options_chain, key=lambda x: x.strike)
        total_put_oi = sum(s.put_oi for s in strikes)
        total_call_oi = sum(s.call_oi for s in strikes)
        pcr = total_put_oi / max(total_call_oi, 1.0)

        iv_values = [0.5 * (s.call_iv + s.put_iv) for s in strikes]
        iv_rank = 0.0
        if iv_values:
            iv_rank = (iv_values[-1] - min(iv_values)) / max(max(iv_values) - min(iv_values), 1e-6)

        strike_intel = []
        weighted_buildups = []
        for s in strikes:
            c = self.classify_strike(s)
            weight = (s.call_oi + s.put_oi) / max(total_call_oi + total_put_oi, 1.0)
            if c == OIClassification.LONG_BUILDUP:
                wb = 1.0 * weight
            elif c == OIClassification.SHORT_COVERING:
                wb = 0.75 * weight
            elif c == OIClassification.SHORT_BUILDUP:
                wb = 0.4 * weight
            else:
                wb = 0.2 * weight
            weighted_buildups.append(wb)
            strike_intel.append(StrikeIntel(strike=s.strike, classification=c, weighted_buildup=wb))

        pain_scores = {
            s.strike: sum(abs(other.strike - s.strike) * (other.call_oi + other.put_oi) for other in strikes)
            for s in strikes
        }
        max_pain = min(pain_scores, key=pain_scores.get) if pain_scores else spot

        concentration = sorted(
            strikes,
            key=lambda x: x.call_oi + x.put_oi,
            reverse=True,
        )[:3]
        concentration_zones = [x.strike for x in concentration]

        weighted_buildup = sum(weighted_buildups)
        pcr_trend = min(1.0, max(0.0, pcr / 1.5))
        oi_strength = 0.5 * weighted_buildup + 0.3 * pcr_trend + 0.2 * (1 - iv_rank)

        intel = OptionsIntel(
            pcr_trend=pcr,
            iv_rank=iv_rank,
            max_pain=max_pain,
            concentration_zones=concentration_zones,
            strike_intel=strike_intel,
        )
        return intel, min(1.0, oi_strength)
