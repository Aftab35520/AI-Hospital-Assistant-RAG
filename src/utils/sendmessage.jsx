

export default async function sendmessage(message) {
    try{
        let response=await fetch(`http://127.0.0.1:5000/${message}/${"usderd1ddd0"}`)
        response=await response.json()
        return(response)
    }
    catch(e){
        console.log(e)
        return "e.message"
    }
   
}