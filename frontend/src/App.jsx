import React, { useState } from 'react';
import './index.css';

function App() {
  const [mode, setMode] = useState('math');
  const [input, setInput] = useState('');
  const [output, setOutput] = useState('');

  const handleRun = async () => {
    try {
      const res = await fetch('http://localhost:5000/compile', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ mode, input }),
      });
      const data = await res.json();
      setOutput(data.output);
    } catch (error) {
      setOutput('❌ Backend connection error');
    }
  };

  return (
    <div className="container">
      <h1>🚀 Smart Compiler</h1>

      <div>
        {['math', 'markdown', 'sql'].map((m) => (
          <button
            key={m}
            onClick={() => setMode(m)}
            className={mode === m ? 'active' : ''}
          >
            {m.toUpperCase()}
          </button>
        ))}
      </div>

      <textarea
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder={`Enter ${mode} code...`}
      ></textarea>

      <button onClick={handleRun}>Run</button>

      <div>
        <h2>Output:</h2>
        <pre style={{ whiteSpace: 'pre-wrap' }}>{output}</pre>
      </div>
    </div>
  );
}

export default App;
