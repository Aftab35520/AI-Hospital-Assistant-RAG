import { useState, useRef, useEffect } from "react";
import Messages from "./Messages";
import sendmessage from "../utils/sendmessage";

const ChatUI = () => {
  const [messages, setmessages] = useState([]);
  const [isthinking, setthinking] = useState(false);

  const ref = useRef(null);
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages, isthinking]);

  const SendMessage = async () => {
    try {
      const msg = ref.current.value.trim();

      if (!msg) return;

      setthinking(true);

      setmessages((prev) => [
        ...prev,
        {
          role: "user",
          content: msg,
        },
      ]);

      ref.current.value = "";

      const msg_res = await sendmessage(msg);

      setmessages((prev) => [
        ...prev,
        {
          role: "Ai",
          content: msg_res.message,
        },
      ]);
    } catch (e) {
      console.log(e);
    } finally {
      setthinking(false);
    }
  };

  return (
    <div className="h-screen flex items-center rounded justify-center bg-gradient-to-br from-cyan-50 via-white to-blue-100 p-4">
      <div className="w-[500px] max-sm:w-full max-sm:h-dvh h-[90vh] bg-white rounded-3xl  shadow-2xl border border-slate-200 overflow-hidden flex flex-col">

        {/* Header */}
        <div className="h-16 bg-gradient-to-r from-cyan-700 to-blue-700 text-white flex items-center justify-between px-6 shadow-md">
          <div>
            <h1 className="text-lg font-bold">
              Hospital AI Assistant
            </h1>
            <p className="text-xs text-cyan-100">
              Sunrise Multispeciality Hospital
            </p>
          </div>

          <div className="h-10 w-10 rounded-full bg-white/20 flex items-center justify-center text-lg">
            
          </div>
        </div>

        {/* Messages */}
        <div className="flex-1 overflow-y-auto bg-slate-50 px-4 py-5">
          {messages.map((msg, idx) => (
            <Messages
              key={idx}
              msg={msg.content}
              role={msg.role}
              setthinking={setthinking}
              setmessages={setmessages}
            />
          ))}

          {isthinking && (
            <div className="flex items-center gap-2 px-3 py-2">
              <span className="h-2.5 w-2.5 rounded-full bg-cyan-600 animate-bounce"></span>
              <span className="h-2.5 w-2.5 rounded-full bg-cyan-600 animate-bounce [animation-delay:0.15s]"></span>
              <span className="h-2.5 w-2.5 rounded-full bg-cyan-600 animate-bounce [animation-delay:0.3s]"></span>
            </div>
          )}

          {/* Auto Scroll Target */}
          <div ref={bottomRef}></div>
        </div>

        {/* Input */}
        <div className="border-t border-slate-200 bg-white px-4 py-3 ">
          <div className="flex items-center gap-3 bg-slate-100 rounded-2xl p-2">

            <input
              ref={ref}
              type="text"
              placeholder="Ask about doctors, appointments..."
              className="flex-1 bg-transparent px-3 py-2 outline-none text-gray-700 placeholder:text-gray-400"
              onKeyDown={(e) => {
                if (e.key === "Enter") {
                  SendMessage();
                }
              }}
            />

            <button
              onClick={SendMessage}
              className="bg-gradient-to-r from-cyan-600 to-blue-600 hover:from-cyan-700 hover:to-blue-700 text-white px-6 py-2.5 rounded-xl font-medium shadow-md transition-all duration-200 hover:scale-105 active:scale-95"
            >
              Send
            </button>

          </div>
        </div>

      </div>
    </div>
  );
};

export default ChatUI;