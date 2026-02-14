from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RiskPolicy:
    max_risk_per_trade: float = 0.02
    daily_loss_cap: float = 0.05
    max_consecutive_losses: int = 3


class RiskEngine:
    def __init__(self, policy: RiskPolicy | None = None) -> None:
        self.policy = policy or RiskPolicy()

    def position_size_percent(
        self,
        account_equity: float,
        stop_loss_distance: float,
        spot: float,
        volatility_regime: bool,
    ) -> float:
        risk_capital = account_equity * self.policy.max_risk_per_trade
        size = risk_capital / max(stop_loss_distance, 1e-6)
        size_pct = (size / max(account_equity / spot, 1e-6))
        if volatility_regime:
            size_pct *= 0.6
        return min(2.0, max(0.1, size_pct))

    def can_trade(self, daily_drawdown: float, consecutive_losses: int, event_risk: bool) -> tuple[bool, str | None]:
        if event_risk:
            return False, "No trade filter active: major event risk"
        if daily_drawdown >= self.policy.daily_loss_cap:
            return False, "Trading halted: daily loss cap breached"
        if consecutive_losses >= self.policy.max_consecutive_losses:
            return False, "Trading halted: 3 consecutive losses"
        return True, None
