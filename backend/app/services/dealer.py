from __future__ import annotations

from typing import List

from app.models.schemas import OptionStrike


class DealerPositioningEngine:
    CONTRACT_SIZE = 50

    def compute(self, options_chain: List[OptionStrike]) -> tuple[float, float]:
        dealer_delta = 0.0
        dealer_gamma = 0.0
        for s in options_chain:
            dealer_delta += (s.call_delta * s.call_oi + s.put_delta * s.put_oi) * self.CONTRACT_SIZE
            dealer_gamma += (s.call_gamma * s.call_oi + s.put_gamma * s.put_oi) * self.CONTRACT_SIZE

        positioning_score = 0.5
        if dealer_delta < 0:
            positioning_score += 0.25
        else:
            positioning_score -= 0.1

        if dealer_gamma > 0:
            positioning_score += 0.15
        else:
            positioning_score -= 0.15

        return dealer_delta, max(0.0, min(1.0, positioning_score))
