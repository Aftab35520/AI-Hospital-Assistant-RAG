

export default async function sendmessage(message) {
    try{
        let response=await fetch(`https://ai-hospital-assistant-rag-1.onrender.com/${message}/${"usderd1ddd0"}`)
        response=await response.json()
        return(response)
    }
    catch(e){
        console.log(e)
        return "e.message"
    }
   
}