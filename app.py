import os
import requests
from flask import Flask, jsonify, render_template, url_for


# Init app
app = Flask(__name__)


CONST_JSONBIN_URL_REQ_STRING = os.environ.get("CONST_JSONBIN_URL_REQ_STRING", None)


# JSON.bin
COLLECTIONS = requests.get(CONST_JSONBIN_URL_REQ_STRING)


# Routing
@app.route("/", methods=["GET"])
@app.route("/index-api", methods=["GET"])
@app.route("/mino-api", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/api/v.1.0/get-collections", methods=["GET"])
@app.route("/api/get-collections", methods=["GET"])
@app.route("/mino-api/get-collections", methods=["GET"])
def get_collections():
    return jsonify({ "collections": COLLECTIONS.json() })


@app.route("/api/v.1.0/get-collections/<int:collection_id>", methods=["GET"])
@app.route("/api/get-collections/<int:collection_id>", methods=["GET"])
@app.route("/mino-api/v.1.0/get-collections/<int:collection_id>", methods=["GET"])
def get_collection(collection_id):
    return COLLECTIONS.json()[collection_id]


# Run app
if __name__ == "__main__": 
    app.run(debug=False)