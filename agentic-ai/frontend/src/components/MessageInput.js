// import React, { useState } from 'react';

// const MessageInput = ({ onSend }) => {
//     const [inputValue, setInputValue] = useState('');

//     const handleChange = (event) => {
//         setInputValue(event.target.value);
//     };

//     const handleSubmit = (event) => {
//         event.preventDefault();
//         if (inputValue.trim()) {
//             onSend(inputValue);
//             setInputValue('');
//         }
//     };

//     return (
//         <form onSubmit={handleSubmit} className="message-input">
//             <input
//                 type="text"
//                 value={inputValue}
//                 onChange={handleChange}
//                 placeholder="Type your question..."
//                 className="input-field"
//             />
//             <button type="submit" className="send-button">Send</button>
//         </form>
//     );
// };

// export default MessageInput;
import React, { useState } from 'react';

const MessageInput = ({ onSendMessage }) => {
  const [value, setValue] = useState('');

  const submit = (e) => {
    e.preventDefault();
    const trimmed = value.trim();
    if (!trimmed) return;
    onSendMessage(trimmed);
    setValue('');
  };

  return (
    <form className="message-input" onSubmit={submit}>
      <input
        className="input-field"
        placeholder="Type your question..."
        value={value}
        onChange={(e) => setValue(e.target.value)}
      />
      <button className="send-button" type="submit">Send</button>
    </form>
  );
};

export default MessageInput;