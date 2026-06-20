import { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState();

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api")
      .then((response) => response.json())
      .then((data) => setMessage(data.message))
      .catch((error) => console.error("error fatching:", error));
  }, []);

  return (
    <div>
      <h1>fronend and backend  connect </h1>
      <p>{message || "looding"}</p>
    </div>
  );
}
export default App;
