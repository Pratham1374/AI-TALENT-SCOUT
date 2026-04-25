import { useState } from "react";
import "./App.css";

function App() {
  const [jd, setJd] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const [name, setName] = useState("");
  const [skills, setSkills] = useState("");
  const [file, setFile] = useState(null);

  // 🔍 Analyze
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

  // ➕ Add Candidate
  const addCandidate = async () => {
    const res = await fetch("http://127.0.0.1:8000/add_candidate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: name,
        skills: skills.split(",").map(s => s.trim())
      }),
    });

    const data = await res.json();
    alert(data.message);

    setName("");
    setSkills("");
  };

  // 📄 Upload Resume
  const uploadResume = async () => {
    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://127.0.0.1:8000/upload_resume", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    alert(data.message);
  };

  return (
    <div className="App">

      <h1>🚀 AI Talent Scout</h1>

      {/* 🔍 JD Input */}
      <textarea
        rows="4"
        placeholder="Paste Job Description..."
        value={jd}
        onChange={(e) => setJd(e.target.value)}
      />

      <br /><br />

      <button onClick={analyze}>
        {loading ? "Analyzing..." : "Analyze"}
      </button>

      {/* ➕ Add Candidate */}
      <h2>Add Candidate</h2>

      <input
        type="text"
        placeholder="Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <input
        type="text"
        placeholder="Skills (comma separated)"
        value={skills}
        onChange={(e) => setSkills(e.target.value)}
      />

      <button onClick={addCandidate}>Add Candidate</button>

      {/* 📄 Upload Resume */}
      <h2>Upload Resume</h2>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button onClick={uploadResume}>Upload</button>

      {/* 📊 Results */}
      <h2>Results</h2>

      {results.map((c, index) => (
        <div key={index} className="card">

          <h3>{index + 1}. {c.candidate}</h3>

          <p><b>Match Score:</b> {c.match_score}</p>

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