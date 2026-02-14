async function getData() {
  const fallback = {
    edge_score: 78,
    buy_probability: 71,
    sell_probability: 29,
    regime: 'Trending',
    gamma_regime: 'Negative',
    oi_strength: 0.68,
    flow_score: 0.74,
    position_size_percent: 2.0,
    stop_loss: '0.9 ATR',
    target: '1.8 ATR',
    confidence: 0.73,
    signal: 'No Trade — insufficient edge'
  };

  try {
    const res = await fetch('http://localhost:8000/api/v1/health', { cache: 'no-store' });
    if (!res.ok) return fallback;
  } catch {
    return fallback;
  }
  return fallback;
}

export default async function Dashboard() {
  const data = await getData();
  const signalClass = data.signal.includes('No Trade') ? 'bad' : 'good';

  return (
    <main className="container">
      <h1>AI-Powered F&O Trading Intelligence</h1>
      <p className="sub">Decision support only — probabilistic intelligence with risk-first controls.</p>
      <div className="grid">
        <section className="card"><div className="title">Market Regime</div><div className="value">{data.regime}</div></section>
        <section className="card"><div className="title">Gamma Regime</div><div className="value">{data.gamma_regime}</div></section>
        <section className="card"><div className="title">Edge Score Gauge</div><div className="value">{data.edge_score}</div></section>
        <section className="card"><div className="title">Options Intelligence</div><div className="value">{(data.oi_strength * 100).toFixed(0)}%</div></section>
        <section className="card"><div className="title">Institutional Flow</div><div className="value">{(data.flow_score * 100).toFixed(0)}%</div></section>
        <section className="card"><div className="title">Risk & Position Size</div><div className="value">{data.position_size_percent}%</div><div className="sub">SL {data.stop_loss} • Target {data.target}</div></section>
      </div>
      <section className="card" style={{ marginTop: 16 }}>
        <div className="title">Trade Execution Logic</div>
        <div className={`signal ${signalClass}`}>{data.signal}</div>
        <div className="sub">Buy {data.buy_probability}% / Sell {data.sell_probability}% | Confidence {(data.confidence * 100).toFixed(0)}%</div>
      </section>
    </main>
  );
}
