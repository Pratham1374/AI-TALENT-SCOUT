import { useState } from "react";
import "./App.css";

function App() {
  const [jd, setJd] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const analyze = async () => {
    setLoading(true);

    const res = await fetch("http://127.0.0.1:8000/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ jd }),
    });

    const data = await res.json();
    setResults(data.results);
    setLoading(false);
  };

  return (
    <div className="App">

      <h1>🚀 AI Talent Scout</h1>

      <textarea
        rows="5"
        placeholder="Paste Job Description..."
        value={jd}
        onChange={(e) => setJd(e.target.value)}
      />

      <br /><br />

      <button onClick={analyze}>
        {loading ? "Analyzing..." : "Analyze"}
      </button>

      <h2>Results</h2>

      {results.map((c, index) => (
        <div key={index} className="card">

          <h3>{index + 1}. {c.candidate}</h3>

          <p><b>Match Score:</b> {c.match_score}</p>

          {/* Progress Bar */}
          <div className="progress-container">
            <div
              className="progress-bar"
              style={{ width: `${c.match_score}%` }}
            ></div>
          </div>

          <p>
            <b>Interest:</b>{" "}
            <span className={c.interest_level.toLowerCase()}>
              {c.interest_level}
            </span>
          </p>

          <div className="reason">
            <b>Why selected:</b> {c.reason}
          </div>

        </div>
      ))}

    </div>
  );
}

export default App;