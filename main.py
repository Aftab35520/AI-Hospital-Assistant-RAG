from flask import Flask,jsonify
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
from controllers.QueryPorcesser import QueryProcesser
@app.route("/<query>/<id>",methods=['GET'])
def Home(query,id):
    response=QueryProcesser(query,id)
    print("d",response)
    return jsonify({"message":response,"status":'success'})

if __name__=='__main__':
    app.run(debug=True)