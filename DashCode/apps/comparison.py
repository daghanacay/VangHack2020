import os

import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from app import app
from dash.dependencies import Input, Output

from DashCode.apps.helper_methods import get_portfolio_returns

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

asx_ytd_data = pd.read_csv('prices_2020.csv')
asx_ytd_data.set_index('Date', inplace=True)
portfolio_data = pd.read_csv('portfolioreturns.csv')
portfolio_data.set_index('Date', inplace=True)

# get_portfolio_returns()


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
                                                             ['Entire Portfolio', 'VAF.AX', 'QAU.AX', 'MOGL.AX', "OZR.AX", "IOO.AX",
                                                              'GGUS.AX', 'RCB.AX', 'VEU.AX', 'IVV.AX', 'SFY.AX']],
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
def update_output(portfolio, benchmark, category):
    if not benchmark or not portfolio or not category:
        return None

    # print(portfolio)
    # print(benchmark)
    # print(category)

    if portfolio == 'Entire Portfolio':
        portfolio_df = portfolio_data.loc[:, ['4']]
        portfolio_df.rename(columns={'4': portfolio}, inplace=True)
    else:
        portfolio_df = asx_ytd_data.loc[:, [portfolio.replace('.AX', '')]]
    # print(portfolio_df)


    if benchmark == 'Top Portfolio - All Time':
        benchmark_df = portfolio_data.loc[:, ['6']]
        benchmark_df.rename(columns={'6': benchmark}, inplace=True)
    elif benchmark == 'Top Portfolio - Last Year':
        benchmark_df = portfolio_data.loc[:, ['7']]
        benchmark_df.rename(columns={'7': benchmark}, inplace=True)
    elif benchmark ==  'Top Portfolio - Last Quarter':
        benchmark_df = portfolio_data.loc[:, ['8']]
        benchmark_df.rename(columns={'8': benchmark}, inplace=True)
    elif benchmark == 'SPX200':
        benchmark_df = portfolio_data.loc[:, ['9']]
        benchmark_df.rename(columns={'9': benchmark}, inplace=True)
    else:
        benchmark_df = asx_ytd_data.loc[:, [benchmark.replace('.AX', '')]]


    print(benchmark_df)

    # export_dataframe = pd.concat([portfolio_df, benchmark_df], axis=1)
    export_dataframe = portfolio_df.join(benchmark_df, how='outer')
    # export_dataframe = export_dataframe.melt(id_vars='date', value_vars=['sessions', 'cost'])
    export_dataframe = export_dataframe.reset_index()

    print(export_dataframe)

    fig = px.line(export_dataframe, x='Date', y=[portfolio.replace('.AX', ''), benchmark.replace('.AX', '')], title='ETF Performance',
                  labels={'value': 'Price'})

    fig.update_layout(legend_title_text='Ticker', hovermode='x')
    fig.update_traces(hovertemplate="Price: %{y} <br>Date: %{x}")

    return fig
