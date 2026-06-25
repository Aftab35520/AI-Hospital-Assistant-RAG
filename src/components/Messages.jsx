import React, { useRef } from 'react'
import sendmessage from '../utils/sendmessage'
export default function Messages({ msg, role, setthinking,setmessages }) {
    return (
        <div className={`w-full flex ${role == "user" ? 'justify-end' : 'justify-start'}`}>
            <div className={`w-[60%] ${role == 'user' ? 'text-end' : 'text-start'}`}>

                {
                    role == "user" ? msg : <AiresponseFormator data={msg} setthinking={setthinking} setmessages={setmessages} />
                }
            </div>
        </div>
    )
}


function AiresponseFormator({ data, setthinking,setmessages }) {
    console.log(data)
    const ref = useRef()
    if (data?.type == "text") return <p>{data.message}</p>
    else {
        const HandleSelect = async (ele, e) => {
            e.target.style.backgroundColor = '#79B6EB'
            ref.current.style.pointerEvents = "None"
            const selection = ele
            try {
                setthinking(true)
                const msg = selection
                setmessages(prev => [...prev, { role: 'user', content: msg }])
                const msg_res = await sendmessage(msg)
                setmessages(prev => [...prev, { role: 'Ai', content: msg_res.message }])
            } catch (e) {
                console.log(e)
            } finally {
                setthinking(false)
            }


        }
        return (
            <div ref={ref} className='bg-gray-300 p-3 rounded-2xl'>
                <p>{data?.message}</p>
                {data?.selections?.map((ele, idx) => (
                    <p key={idx} className='p-2 mt-2 bg-white rounded-2xl cursor-pointer' onClick={(e) => HandleSelect(Object.values(ele).join(" | "), e)}>
                        {Object.values(ele).join(" | ")}
                    </p>
                ))}
            </div>
        )
    }
}
