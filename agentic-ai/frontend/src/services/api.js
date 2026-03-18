// import axios from 'axios';

// const API_URL = 'http://localhost:8000/api'; // Adjust the URL as needed

// export const sendMessage = async (message) => {
//     try {
//         const response = await axios.post(`${API_URL}/ask`, { question: message });
//         return response.data;
//     } catch (error) {
//         console.error('Error sending message:', error);
//         throw error;
//     }
// };

// import axios from 'axios';

// const API_URL = 'http://localhost:8000/api'; // Adjust if needed

// export const sendMessage = async (message) => {
//     try {
//         const response = await axios.post(`${API_URL}/ask`, { question: message });
//         // backend returns { "response": ... } in routes.py
//         return response.data.response;
//     } catch (error) {
//         console.error('Error sending message:', error);
//         throw error;
//     }
// };

// Lightweight fetch-based client (no axios dependency)
const API_BASE = 'http://localhost:8000/api';

export async function sendMessage(question) {
  const res = await fetch(`${API_BASE}/ask`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ question }),
  });
  if (!res.ok) {
    const txt = await res.text();
    throw new Error(`API error: ${res.status} ${txt}`);
  }
  const data = await res.json();
  // expects backend: { response: "..." } or { answer: "..." }
  return data.response ?? data.answer ?? JSON.stringify(data);
}
