import React, { useState } from 'react';
import axios from 'axios';
import './Chatbot.css';

const Chatbot = () => {
  const [messages, setMessages] = useState([]);
  const [userInput, setUserInput] = useState('');

  const sendMessage = async () => {
    if (!userInput) return; // avoids sending empty messages

    try {
      const response = await axios.post('http://34.122.16.145:5000/predict', {
        text: userInput,
      });

      // use functional setState to ensure we use the latest state
      setMessages(prevMessages => [
        ...prevMessages,
        { text: userInput, isUser: true },
        { text: response.data.response, isUser: false },
      ]);

      setUserInput('');
    } catch (error) {
      console.error('Error fetching response:', error);
      // Show an error message in the chat
      setMessages(prevMessages => [
        ...prevMessages,
        { text: 'Error: Could not connect to the server.', isUser: false },
      ]);
    }
  };

  return (
    <div className="chatbot-container">
         <div className="messages">
        {messages.map((msg, index) => (
          <div key={index} className={msg.isUser ? 'user-message' : 'bot-message'}>
            {msg.text}
          </div>
        ))}
      </div>
      <input
        type="text"
        value={userInput}
        onChange={(e) => setUserInput(e.target.value)}
        placeholder="Type a message..."
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
};

export default Chatbot;