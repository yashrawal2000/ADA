from __future__ import annotations

import numpy as np

from app.models.schemas import BacktestResult


class WalkForwardBacktester:
    def run(self, returns: list[float], brokerage_bps: float = 2.5, slippage_bps: float = 4.0) -> BacktestResult:
        arr = np.array(returns, dtype=float)
        if arr.size == 0:
            return BacktestResult(
                sharpe_ratio=0,
                max_drawdown=0,
                win_rate=0,
                total_trades=0,
                slippage_cost=0,
                brokerage_cost=0,
            )

        slippage_cost = float(np.sum(np.abs(arr)) * slippage_bps / 10_000)
        brokerage_cost = float(arr.size * brokerage_bps / 10_000)
        net = arr - (slippage_bps + brokerage_bps) / 10_000

        equity = np.cumprod(1 + net)
        peak = np.maximum.accumulate(equity)
        max_dd = float(np.max((peak - equity) / np.maximum(peak, 1e-6)))
        sharpe = float(np.mean(net) / (np.std(net) + 1e-8) * np.sqrt(252))
        win_rate = float(np.mean(net > 0))

        return BacktestResult(
            sharpe_ratio=round(sharpe, 3),
            max_drawdown=round(max_dd, 3),
            win_rate=round(win_rate, 3),
            total_trades=int(arr.size),
            slippage_cost=round(slippage_cost, 4),
            brokerage_cost=round(brokerage_cost, 4),
        )
