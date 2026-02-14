from __future__ import annotations

import numpy as np
import pandas as pd


def ema(series: pd.Series, span: int) -> pd.Series:
    return series.ewm(span=span, adjust=False).mean()


def atr(df: pd.DataFrame, period: int = 14) -> float:
    high_low = df["high"] - df["low"]
    high_close = (df["high"] - df["close"].shift()).abs()
    low_close = (df["low"] - df["close"].shift()).abs()
    tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    return float(tr.rolling(period).mean().iloc[-1])


def rsi(series: pd.Series, period: int = 14) -> float:
    delta = series.diff()
    gains = delta.clip(lower=0).rolling(period).mean()
    losses = (-delta.clip(upper=0)).rolling(period).mean()
    rs = gains / losses.replace(0, np.nan)
    val = 100 - (100 / (1 + rs.iloc[-1]))
    return float(np.nan_to_num(val, nan=50.0))


def vwap(df: pd.DataFrame) -> float:
    typical_price = (df["high"] + df["low"] + df["close"]) / 3
    return float((typical_price * df["volume"]).sum() / max(df["volume"].sum(), 1))


def volume_zscore(series: pd.Series, window: int = 20) -> float:
    rolling_mean = series.rolling(window).mean().iloc[-1]
    rolling_std = series.rolling(window).std().iloc[-1]
    if not rolling_std or np.isnan(rolling_std):
        return 0.0
    return float((series.iloc[-1] - rolling_mean) / rolling_std)


def adx(df: pd.DataFrame, period: int = 14) -> float:
    up_move = df["high"].diff()
    down_move = -df["low"].diff()
    plus_dm = np.where((up_move > down_move) & (up_move > 0), up_move, 0)
    minus_dm = np.where((down_move > up_move) & (down_move > 0), down_move, 0)

    tr = pd.concat(
        [
            df["high"] - df["low"],
            (df["high"] - df["close"].shift()).abs(),
            (df["low"] - df["close"].shift()).abs(),
        ],
        axis=1,
    ).max(axis=1)

    atr_vals = tr.rolling(period).mean()
    plus_di = 100 * (pd.Series(plus_dm).rolling(period).mean() / atr_vals)
    minus_di = 100 * (pd.Series(minus_dm).rolling(period).mean() / atr_vals)
    dx = (abs(plus_di - minus_di) / (plus_di + minus_di)).replace(np.nan, 0) * 100
    return float(dx.rolling(period).mean().iloc[-1])


def normalize_0_1(value: float, low: float, high: float) -> float:
    if high <= low:
        return 0.5
    clipped = min(max(value, low), high)
    return (clipped - low) / (high - low)
