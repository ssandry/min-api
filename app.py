import os
import requests
import json
from flask import Flask, jsonify, render_template


# Init app
__APP = Flask(__name__)


# Use Environment variable from Heroku
CONST_JSONBIN_URL_REQ_STRING = os.environ.get("CONST_JSONBIN_URL_REQ_STRING", None)


# Defining the mode
if CONST_JSONBIN_URL_REQ_STRING == None:
    MODE = "dev"
else:
    MODE = "prod"


# Fetch data
if MODE == "dev":
    with open("./data/collections.dev.json", encoding="utf-8") as json_res:
        COLLECTIONS = json.load(json_res)
elif MODE == "prod":
    COLLECTIONS = requests.get(CONST_JSONBIN_URL_REQ_STRING)
else:
    print("MODE undefined")


# Routing
@__APP.route("/", methods=["GET"])
@__APP.route("/index-api", methods=["GET"])
@__APP.route("/mino-api", methods=["GET"])
def index():
    return render_template("index.html")


@__APP.route("/api/v.1.0/get-collections", methods=["GET"])
@__APP.route("/api/get-collections", methods=["GET"])
@__APP.route("/mino-api/get-collections", methods=["GET"])
def get_collections():

    if MODE == "prod":
        return jsonify({ "collections": COLLECTIONS.json() })
    elif MODE == "dev":
        return jsonify({ "collections": COLLECTIONS })


@__APP.route("/api/v.1.0/get-collections/<int:collection_id>", methods=["GET"])
@__APP.route("/api/get-collections/<int:collection_id>", methods=["GET"])
@__APP.route("/mino-api/v.1.0/get-collections/<int:collection_id>", methods=["GET"])
def get_collection(collection_id):

    if MODE == "prod":
        return COLLECTIONS.json()[collection_id]
    elif MODE == "dev":
        return COLLECTIONS[collection_id]


# Run app
if __name__ == "__main__": 
    __APP.run(debug=False)