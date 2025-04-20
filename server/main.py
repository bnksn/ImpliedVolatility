from flask import Flask, request, jsonify
from flask_cors import CORS  # type: ignore
from server.marketData import getVolSurface, isValidTicker
from server.volCache import VolCache
import logging
import server.constants as constants

app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

volCache = VolCache(expirationSeconds=constants.volCacheExpirationSeconds)


@app.route("/getImpliedSurface", methods=["GET"])
def getVolSurfaceApi():
    ticker = request.args.get("ticker").upper()
    if not isValidTicker(ticker):
        return jsonify({"error": f"Invalid ticker {ticker}"}), 400

    return volCache.get(ticker) or volCache.set(ticker, getVolSurface(ticker).toDict())


if __name__ == "__main__":
    app.run()
