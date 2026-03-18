// import React, { useState } from 'react';
// import MessageList from './MessageList';
// import MessageInput from './MessageInput';
// import './ChatWindow.css';

// const ChatWindow = () => {
//     const [messages, setMessages] = useState([]);

//     const handleSendMessage = async (message) => {
//         const newMessages = [...messages, { text: message, sender: 'user' }];
//         setMessages(newMessages);

//         const response = await fetch('/api/chat', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//             body: JSON.stringify({ question: message }),
//         });

//         const data = await response.json();
//         setMessages([...newMessages, { text: data.answer, sender: 'bot' }]);
//     };

//     return (
//         <div className="chat-window">
//             <MessageList messages={messages} />
//             <MessageInput onSendMessage={handleSendMessage} />
//         </div>
//     );
// };

// export default ChatWindow;

import React from 'react';
import MessageList from './MessageList';
import MessageInput from './MessageInput';

const ChatWindow = ({ messages = [], onSendMessage }) => {
  return (
    <div className="chat-window">
      <MessageList messages={messages} />
      <MessageInput onSendMessage={onSendMessage} />
    </div>
  );
};

export default ChatWindow;