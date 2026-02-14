from __future__ import annotations

from fastapi import APIRouter
from pydantic import BaseModel

from app.models.schemas import InstrumentInput, TradeIntelligence
from app.services.engine import TradingIntelligenceEngine

router = APIRouter(prefix="/api/v1", tags=["trading-intelligence"])
engine = TradingIntelligenceEngine()


class EvaluateRequest(BaseModel):
    instrument: InstrumentInput
    account_equity: float = 1_000_000
    daily_drawdown: float = 0.0
    consecutive_losses: int = 0


@router.post("/evaluate", response_model=TradeIntelligence)
def evaluate(req: EvaluateRequest) -> TradeIntelligence:
    return engine.evaluate(
        payload=req.instrument,
        account_equity=req.account_equity,
        daily_drawdown=req.daily_drawdown,
        consecutive_losses=req.consecutive_losses,
    )


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
