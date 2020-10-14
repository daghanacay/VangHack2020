import dash
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = dash.Dash(__name__, suppress_callback_exceptions=False)
server = app.server

@server.route('/ticker_data')
def ticker_data():
    ticker = request.args.get('ticker')
    start_date = request.args.get('start-date')
    end_date = request.args.get('end-date')
    print(ticker, start_date, end_date)
    return jsonify({'message': 'this is the first route'})