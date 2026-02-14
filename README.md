# AI-Powered F&O Trading Intelligence System

Risk-first decision-support engine for personal capital trading in F&O markets.

## Safety Principles
- No guaranteed signals.
- Max 2% capital risk per trade.
- Daily loss cap at 5%.
- Trading halt after 3 consecutive losses.
- Event-risk filter blocks trades during major events.

## Architecture
- **Backend**: FastAPI + analytics engines (`backend/app/services`)
- **ML stack integration points**: PyTorch + HuggingFace (FinBERT/Chronos ready)
- **Data stores**: PostgreSQL (structured), Redis (real-time)
- **Frontend**: Next.js dark-theme institutional dashboard
- **Deployment**: Docker Compose (EC2-ready baseline)

## Implemented Engines
1. Technical indicators: ATR, RSI, VWAP, EMA(20/50/200), Volume Z-score
2. Regime detection: volatility clustering + ADX + rolling std
3. Edge score model
4. Options OI intelligence (buildup class, PCR trend, IV rank, max pain, OI concentration)
5. Gamma exposure & gamma regime
6. Dealer positioning (delta + gamma blend)
7. Institutional flow score
8. Risk management & execution filter logic
9. Backtesting utility with slippage/brokerage and metrics
10. Audit logger

## API
### POST `/api/v1/evaluate`
Returns structured intelligence JSON:

```json
{
  "edge_score": 78,
  "buy_probability": 71,
  "sell_probability": 29,
  "regime": "Trending",
  "gamma_regime": "Negative",
  "oi_strength": 0.68,
  "flow_score": 0.74,
  "position_size_percent": 2.1,
  "stop_loss": "0.9 ATR",
  "target": "1.8 ATR",
  "confidence": 0.73
}
```

## Run
```bash
docker compose up --build
```
- Backend: `http://localhost:8000`
- Frontend dashboard: `http://localhost:3000`

## Notes
This system provides probabilistic decision support for discretionary or supervised trading workflows, not guaranteed outcomes.
