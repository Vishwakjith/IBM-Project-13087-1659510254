import json
from flask import Flask,jsonify
app = Flask("Demo-Server")


@app.route('/get',methods=["GET"])
def get_method():
    return jsonify({
        'name':'alice',
        'email':'alice@outlook.com',
        'method':'GET'
    })
@app.route('/post',methods=["POST"])
def post_method():
    return jsonify({
        'name':'alice',
        'email':'alice@outlook.com',
        'method':'POST'
    })
@app.route('/put',methods=["PUT"])
def put_method():
    return jsonify({
        'name':'alice',
        'email':'alice@outlook.com',
        'method':'PUT'
    })
@app.route('/delete',methods=["DELETE"])
def delete_method():
    return jsonify({
        'name':'alice',
        'email':'alice@outlook.com',
        'method':'DELETE'
    })

if __name__ == "__main__":
    app.run()