import dash
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from apps import comparison, leadership

from app_holder import app

application = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/comparison':
        return comparison.layout
    elif pathname == '/leadership':
        return leadership.layout
    else:
        return '404'

if __name__ == '__main__':
    application.run(debug=True)