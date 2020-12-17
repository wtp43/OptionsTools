from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate


app = Flask(__name__)
CORS(app)

@app.route('/tickers')
def get_tickers():

	return jsonify(tickers)


@app.route('/tickers/<ticker>', methods=['POST'])
def add_ticker(ticker):
	
	return jsonify(new_ticker), 201

if __name__ == '__main__':
    app.run(debug=True)

#fuser -n tcp -k 5000
#curl http://0.0.0.0:5000/tickers
#./bootstrap.sh &