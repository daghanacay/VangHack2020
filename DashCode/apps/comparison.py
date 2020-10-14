import os

import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from app import app
from dash.dependencies import Input, Output

folder = os.getcwd()

path = '/home/manveer/hackathon/VangHack2020/asx-data/asx_etf_list.csv'
df = pd.read_csv(path)

df['ASX Code'] = df['ASX Code'].astype(str) + '.AX'

benchmark_options = [{'label': i, 'value': i} for i in ['Top Portfolio - All Time',
                                                             'Top Portfolio - Last Year',
                                                             'Top Portfolio - Last Quarter',
                                                             'SPX200',
                                                             ]]

benchmark_options.extend([{'label': i, 'value': i} for i in df['ASX Code']])

print(benchmark_options)



layout = html.Div([html.H1('VANGUARD FANTASY ETF EXCHANGE',
                           style={'textAlign': 'center', 'fontSize': 30, 'color': 'maroon',
                                  'border': '3px black solid'}),

                   html.Div([
                       # dcc.DatePickerRange(id='date_range', min_date_allowed=dt.today(),
                       #                          max_date_allowed=dt.today(),
                       #                          start_date=dt.today(),
                       #                          end_date=dt.today(),
                       #                          initial_visible_month=dt.today(),
                       #                          display_format='Y-MM-DD', end_date_placeholder_text="End Date",
                       #                          clearable=True),

                       html.H3('Compare'),
                       dcc.Dropdown(id='portfolio', options=[{'label': i, 'value': i} for i in
                                                             ['Entire Portfolio', 'VAF', 'QAU', 'MOGL', "OZR", "IOO",
                                                              'GGUS', 'RCB', 'VEU', 'IVV', 'SFY']],
                                    value=[], multi=False,
                                    placeholder='Entire Portfolio'),
                       html.H3('against'),
                       dcc.Dropdown(id='benchmark', options=benchmark_options,
                                    value=[], multi=False,
                                    # style={'float': 'right', 'position': 'relative', 'display': 'inline-block',
                                    #        'height': '47px', 'width': '50%', 'margin-top': '-5px',
                                    #        'fontSize': 20, 'padding-right': '5px'},
                                    placeholder='Select Comparison')]),
                   html.H3('on'),
                   dcc.Dropdown(id='category',
                                options=[{'label': i, 'value': i} for i in ['YTD%', 'Return since Inception',
                                                                            'Investment Amount',
                                                                            'Number of Investors']],
                                value=[], multi=False,
                                # style={'float': 'right', 'position': 'relative', 'display': 'inline-block',
                                #        'height': '47px', 'width': '50%', 'margin-top': '-5px',
                                #        'fontSize': 20, 'padding-right': '5px'},
                                placeholder='Select Tickers'),
                   dcc.Graph(id='graph')])

app.layout = layout


@app.callback(Output('graph', 'figure'), [Input('portfolio', 'value'), Input('benchmark', 'value'),
                                          Input('category', 'value')])
def update_output(benchmark, against, value):
    if not benchmark or not against or not value:
        return None

    print(benchmark)
    print(against)
    print(value)
    return None
    # sd  = start_date.split('T')[0]
    # ed = end_date.split('T')[0]
    # print(tickers, sd, ed)
    # stock_df = yf.download(tickers=tickers, start=start_date.split('T')[0], end=end_date.split('T')[0], progress=False)
    # df_close = stock_df.Close
    #
    # fig = px.line(df_close, x=df_close.index, y=[tickers], title='ETF Performance',
    #               labels={'value': 'Price'})  # .for_each_trace(lambda t: t.update(name = t.name.replace('.AX','')))
    #
    # fig.update_layout(legend_title_text='Ticker', hovermode='x')
    # fig.update_traces(hovertemplate="Price: %{y} <br>Date: %{x}")
    #
    # return fig
