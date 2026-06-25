import { useState, useRef } from "react";
import Messages from "./Messages";
import sendmessage from "../utils/sendmessage";

const ChatUI = () => {
  const [messages, setmessages] = useState([])
  const [isthinking,setthinking]=useState(false)
  const ref = useRef()
  
  const SendMessage = async () => {
    try{
      setthinking(true)
    const msg = (ref.current.value)
    setmessages(prev => [...prev, { role: 'user', content: msg }])
    ref.current.value = ""
    const msg_res = await sendmessage(msg)
    setmessages(prev => [...prev, { role: 'Ai', content: msg_res.message }])
    }catch(e){
      console.log(e)
    }finally{
      setthinking(false)
    }

  }



  return (
    <div className="h-screen flex items-center justify-center ">
      <div className="w-[500px] max-sm:w-full max-sm:h-dvh max-sm:m-1 h-[90vh] bg-white rounded-2xl shadow-2xl flex flex-col overflow-hidden border border-cyan-100">
        <div className="h-16 bg-cyan-700 text-white flex items-center px-5">
          <h1 className="text-lg font-semibold">
            Hospital AI Assistant
          </h1>
        </div>

        <div className="flex-1 bg-white p-3 overflow-y-scroll">
          {
            messages.map((msg, idx) => <Messages msg={msg.content} role={msg.role} setthinking={setthinking} setmessages={setmessages}/>)
          }
          {isthinking&&<div className="flex items-center gap-1">
            <span className="h-2 w-2 rounded-full bg-gray-500 animate-bounce"></span>
            <span className="h-2 w-2 rounded-full bg-gray-500 animate-bounce [animation-delay:0.15s]"></span>
            <span className="h-2 w-2 rounded-full bg-gray-500 animate-bounce [animation-delay:0.3s]"></span>
          </div>
}
        </div>

        <div className={`h-20 border-t border-slate-200 flex items-center px-4 gap-3 ${messages[messages.length-1]?.content?.type=="selector"?'pointer-events-none opacity-30':''}`}>
          <input
            ref={ref}
            className="flex-1 border border-slate-200 rounded-lg px-4 py-2 outline-none focus:border-cyan-500"
            placeholder="Type your message..."
          />
          <button className="bg-cyan-700 hover:bg-cyan-800 text-white px-5 py-2 rounded-lg transition" onClick={SendMessage}>
            Send
          </button>
        </div>

      </div>
    </div>
  );
};

export default ChatUI;