// import React, { useState } from 'react';
// import ChatWindow from './components/ChatWindow';
// import MessageInput from './components/MessageInput';
// import './styles/main.css';


// const App = () => {
//     const [messages, setMessages] = useState([]);

//     const handleSendMessage = async (message) => {
//         const userMessage = { text: message, sender: 'user' };
//         setMessages((prevMessages) => [...prevMessages, userMessage]);

//         const response = await fetch('http://localhost:8000/api/chat', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//             body: JSON.stringify({ question: message }),
//         });

//         const data = await response.json();
//         const botMessage = { text: data.answer, sender: 'bot' };
//         setMessages((prevMessages) => [...prevMessages, botMessage]);
//     };

//     return (
//         <div className="app">
//             <ChatWindow messages={messages} />
//             <MessageInput onSendMessage={handleSendMessage} />
//         </div>
//     );
// };

// export default App;
import React, { useState } from 'react';
import ChatWindow from './components/ChatWindow';
import { sendMessage } from './services/api';
import './styles/main.css';

const App = () => {
  const [messages, setMessages] = useState([]);

  const handleSendMessage = async (text) => {
    const userMsg = { id: Date.now(), text, sender: 'user' };
    setMessages((m) => [...m, userMsg]);

    try {
      const botText = await sendMessage(text);
      const botMsg = { id: Date.now() + 1, text: botText, sender: 'bot' };
      setMessages((m) => [...m, botMsg]);
    } catch (err) {
      const errMsg = { id: Date.now() + 2, text: 'Error: failed to get response', sender: 'bot' };
      setMessages((m) => [...m, errMsg]);
      console.error(err);
    }
  };

  return (
    <div className="app-container">
      <h1 className="app-title">Agentic Agent Chat</h1>
      <ChatWindow messages={messages} onSendMessage={handleSendMessage} />
    </div>
  );
};

export default App;