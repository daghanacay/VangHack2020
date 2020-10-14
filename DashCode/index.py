import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import comparison, app2, etf_create


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
        return app2.layout
    elif pathname == '/createetf':
        return etf_create.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)