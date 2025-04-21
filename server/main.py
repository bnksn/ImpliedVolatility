import os
import sys

# This is a workaround to add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from server.marketData import getVolSurface, isValidTicker
from server.volCache import VolCache
import logging
import server.constants as constants
from typing import Any

app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

volCache = VolCache(expirationSeconds=constants.volCacheExpirationSeconds)


@app.route("/getImpliedSurface", methods=["GET"])
def getVolSurfaceApi() -> dict[str, Any] | tuple[Response, int]:
    ticker = request.args.get("ticker").upper()  # type: ignore
    if not isValidTicker(ticker):
        return jsonify({"error": f"Invalid ticker {ticker}"}), 400

    return volCache.get(ticker) or volCache.set(ticker, getVolSurface(ticker).toDict())


if __name__ == "__main__":
    app.run()
