from flask import Flask,jsonify,request,send_from_directory
from flask_cors import CORS
from route.chat import chatRoute
app=Flask(__name__,static_folder="AI-Hospital-Assistant-RAG/dist",
    static_url_path="")

CORS(app)
@app.route("/",methods=["GET"])
def home():
    return send_from_directory(app.static_folder, "index.html")
@app.route("/chat",methods=["POST"])
def chat():
    data = request.get_json()
    result=chatRoute(data)

    return jsonify({"message":result,"success":"TRUE"})
if __name__=="__main__":
    app.run(debug=True)