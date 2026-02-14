from __future__ import annotations

from typing import List

from app.models.schemas import GammaRegime, OptionStrike


class GammaEngine:
    CONTRACT_SIZE = 50

    def compute(self, options_chain: List[OptionStrike], spot: float) -> tuple[GammaRegime, float, float]:
        call_gex, put_gex = 0.0, 0.0
        strike_gex = []
        for s in options_chain:
            c = s.call_gamma * s.call_oi * self.CONTRACT_SIZE * (spot**2)
            p = s.put_gamma * s.put_oi * self.CONTRACT_SIZE * (spot**2)
            call_gex += c
            put_gex += p
            strike_gex.append((s.strike, c - p))

        total_gex = call_gex - put_gex
        gamma_regime = GammaRegime.POSITIVE if total_gex > 0 else GammaRegime.NEGATIVE
        if abs(total_gex) < 1e-5:
            gamma_regime = GammaRegime.FLIP

        gamma_flip = min(strike_gex, key=lambda x: abs(x[1]))[0] if strike_gex else spot
        gamma_modifier = 1.05 if gamma_regime == GammaRegime.POSITIVE else 0.95
        return gamma_regime, gamma_flip, gamma_modifier
