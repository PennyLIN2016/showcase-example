import React, { useEffect, useRef } from 'react';

const MessageList = ({ messages = [] }) => {
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  return (
    <div className="message-list">
      {messages.map((m) => (
        <div key={m.id} className={`message ${m.sender}`}>
          <div className="message-text">{m.text}</div>
        </div>
      ))}
      <div ref={bottomRef} />
    </div>
  );
};

export default MessageList;
