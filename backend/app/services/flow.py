from __future__ import annotations

from app.core.indicators import normalize_0_1


class InstitutionalFlowDetector:
    def compute(self, volume_z: float, order_imbalance: float, delivery_spike: float, vwap_strength: float) -> float:
        vz = normalize_0_1(volume_z, -3, 3)
        imb = normalize_0_1(order_imbalance, -1, 1)
        deliv = normalize_0_1(delivery_spike, -20, 20)
        vwap = normalize_0_1(vwap_strength, -0.02, 0.02)
        score = 0.3 * vz + 0.3 * imb + 0.2 * deliv + 0.2 * vwap
        return max(0.0, min(1.0, score))
