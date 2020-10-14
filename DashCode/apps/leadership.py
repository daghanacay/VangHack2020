import os
from datetime import datetime as dt
from pathlib import Path

import dash_core_components as dcc
import dash_html_components as html
import dash_table
# from app import app
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

from app_holder import app

top_10_df = pd.read_csv('top_10_ranks.csv')


layout = html.Div([html.H1('FANTASY ETF - Leadership Board',
                           style={'textAlign': 'center', 'fontSize': 30, 'color': 'maroon',
                                  'border': '3px black solid'}),
html.Div(html.H3('Select Period'),style={'width': '11%', 'display': 'inline-block'}),
html.Div(dcc.Dropdown(id='range', options=[{'label': i, 'value': i} for i in
                                                             ['YTD%', 'QoQ%', 'YoY%', 'Custom Date Range']],
                                    value=['YTD%'], multi=False,
                                    placeholder='YTD%'),style={'textAlign': 'left', 'width': '15%', 'display': 'inline-block'}),
    dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in top_10_df.columns],
    data=top_10_df.to_dict('records')),
    html.Div(dcc.Graph(id='leadership-graph'))]
)

app.layout = layout