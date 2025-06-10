import { useState } from "react";

export const ChatInputBar = ({ onSend }) => {
    const [input, setInput] = useState(null);
  
    const handleKeyDown = (e) => {
      if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        if (input.trim()) {
          onSend(input.trim());
          setInput("");
        }
      }
    };
  
    return (
        <div className="fixed bottom-0 left-0 right-0 flex justify-center px-4 pb-4">
        <div className="max-w-3xl w-full flex items-end bg-gray-200 border border-gray-300 py-5 px-4 rounded-lg shadow-lg">
          <textarea
            className="flex-grow resize-none rounded-md border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white"
            rows={1}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Type your message..."
            style={{ maxHeight: "150px", overflowY: "auto" }}
          />
          <button
            onClick={() => {
              if (input.trim()) {
                onSend(input.trim());
                setInput("");
              }
            }}
            className="ml-2 px-4 py-2 text-sm bg-blue-600 text-white rounded-md hover:bg-blue-700 transition"
          >
            Send
          </button>
        </div>
      </div>
      
    );
  };
  