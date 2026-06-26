export default async function sendmessage(message) {
  let userId = localStorage.getItem("userId");

  if (!userId) {
    userId = crypto.randomUUID(); 
    localStorage.setItem("userId", userId);
  }

  try {
    const response = await fetch(
      `https://ai-hospital-assistant-rag-1.onrender.com/${encodeURIComponent(message)}/${userId}`
    );

    const data = await response.json();
    return data;
  } catch (e) {
    console.error(e);
    return e.message;
  }
}