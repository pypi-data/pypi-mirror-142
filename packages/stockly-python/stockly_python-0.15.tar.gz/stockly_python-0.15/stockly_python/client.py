import requests
import json
from flask import Flask, jsonify, request
import asyncio
from sendMessage import SendMessage


app = Flask(__name__)

@app.route("/python-package", methods=["POST"])
def GetMessage():
    try:
        message_dict = json.loads(request.get_json())
        print(message_dict)
        notification = message_dict['notification']
        room_id = message_dict['room_id']
        asyncio.run(SendMessage(notification, room_id))
        return ("SuccessResponse")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5001)