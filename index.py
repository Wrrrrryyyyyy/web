import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template, request, make_response, jsonify
from datetime import datetime, timezone, timedelta
app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    # build a request object
    req = request.get_json(force=True)
    # fetch queryResult from json
    action =  req.get("queryResult").get("action")
    #msg =  req.get("queryResult").get("queryText")
    #info = "動作：" + action + "； 查詢內容：" + msg
   if (action == "rateChoice"):
    rate =  req.get("queryResult").get("parameters").get("rate")
    info = "您選擇的電影分級是：" + rate
    return make_response(jsonify({"fulfillmentText": info}))

if __name__ == "__main__":
    app.run()