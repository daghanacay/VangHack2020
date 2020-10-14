import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
#from app import app
import pandas as pd
import os
from pathlib import Path
from datetime import datetime, date

app = dash.Dash(__name__)

folder = os.getcwd()
portfolio_returns_table = pd.read_csv(Path(folder, 'portfolioreturns_maria.csv',parse_dates=[0]))
portfolio_returns_table = portfolio_returns_table.set_index('Unnamed: 0')
name_portfolioID_table = pd.read_csv(Path(folder, 'name_portfolioID.csv'))


def get_leader_board(returnsdata, namedata, date=None, top_n=10):
    if date is None:
        date = datetime.today().date().strftime('%Y-%m-%d')
    datespecificdata = returnsdata.loc[date]
    datespecificdata = datespecificdata.T
    datespecificdata = datespecificdata.sort_values(ascending=False)
    datespecificdata = datespecificdata[:top_n]

    leadederboard = pd.DataFrame(datespecificdata)
    names = []
    for i in datespecificdata.index:
         i =int(i)
         names.append(name_portfolioID_table.iloc[i].item())

    leadederboard['Name'] = names
    return leadederboard



print(get_leader_board(portfolio_returns_table, name_portfolioID_table, date='2020-10-12'  ))

def generate_table(dataframe):
    return html.Table(
        # header
        [html.Tr([html.Td(col) for col in dataframe.columns])] +

        # body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe)))])

layout = html.Div([dcc.DatePickerSingle(
        id='my-date-picker-single',
        min_date_allowed=date(2020, 1, 2),
        max_date_allowed=date(2020, 10, 12),
        initial_visible_month=date(2020, 10, 12),
        date=datetime.today().date()
    ), html.Div(id='output-container-date-picker-single')
])


#@app.callback(
#    Output()


app.layout = layout



#if __name__ == '__main__':
#    app.run_server(debug=True)