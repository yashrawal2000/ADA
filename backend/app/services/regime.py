from __future__ import annotations

import pandas as pd

from app.core.indicators import adx
from app.models.schemas import Regime


class RegimeDetector:
    @staticmethod
    def detect(df: pd.DataFrame) -> tuple[Regime, float]:
        returns = df["close"].pct_change().dropna()
        rolling_std = returns.rolling(20).std().iloc[-1]
        adx_val = adx(df)

        if rolling_std > 0.02:
            return Regime.VOL_EXPANSION, min(1.0, rolling_std / 0.05)
        if rolling_std < 0.005:
            return Regime.VOL_COMPRESSION, max(0.4, 1 - rolling_std / 0.005)
        if adx_val >= 25:
            return Regime.TRENDING, min(1.0, adx_val / 45)
        return Regime.RANGING, max(0.4, 1 - adx_val / 35)
