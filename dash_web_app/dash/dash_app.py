from urllib.error import HTTPError

import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
from dash import Dash
from dash.dependencies import Input, Output
from flask import Flask

url_base = '/dash_application/app1/'


def read_covid_data() -> pd.DataFrame:
    today = (pd.to_datetime('today') - pd.to_timedelta('0 days')).strftime('%Y-%m-%d')
    link = f'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-{today}.xls'
    print(f"\n*** Retrieving file {link}...")

    try:
        link = f'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-{today}.xls'
        df = pd.read_excel(link)
    except HTTPError as err:
        link = f'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-{today}.xlsx'
        df = pd.read_excel(link)

    print(df.head())

    return df


def make_table_from_df(df: pd.DataFrame):
    arr = ['This is an example Plotly Dash App.']

    table_preview = dash_table.DataTable(
        id='table_covid',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("rows"),
        sort_action="native",
        sort_mode='single'
    )
    arr.append(table_preview)

    return arr


def make_line_from_df(df: pd.DataFrame):
    arr = ['This is an example Plotly Graph.']

    plot = dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                dict(
                    x=df[df['continent'] == i]['gdp per capita'],
                    y=df[df['continent'] == i]['life expectancy'],
                    text=df[df['continent'] == i]['country'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.continent.unique()
            ],
            'layout': dict(
                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
    arr.append(plot)

    return arr


layout = html.Div([
    html.Div('This is dash app1'), html.Br(),
    dcc.Input(id='input_text'), html.Br(), html.Br(),
    html.Div(id="output"), html.Br(), html.Br(),
    html.Div(id='target', className='w3-container w3-green w3-text-black w3-table',
             children=make_table_from_df(read_covid_data()))
])


def Add_Dash(server: Flask):
    external_stylesheets = ["https://www.w3schools.com/w3css/4/w3.css", ]

    app = Dash(
        server=server,
        url_base_pathname=url_base,
        external_stylesheets=external_stylesheets,
    )

    app.layout = layout

    @app.callback(
        Output('output', 'children'),
        [Input('input_text', 'value')])
    def callback_fun(value):
        return f'Your input is: {value}'

    return app.server

# def register_dashapp(server: Flask, layout, name: str):
#     external_stylesheets = ["https://www.w3schools.com/w3css/4/w3.css", ]
#
#     dashapp = Dash(server=server,
#                    url_base_pathname=f'/{name}/',
#                    # external_scripts=external_scripts,
#                    # routes_pathname_prefix='/dash_app/',
#                    external_stylesheets=external_stylesheets,
#                    )
#
#     with server.app_context():
#         dashapp.index_string = html_layout
#         dashapp.layout = layout(get_covid_dataset)
#
#         # @dashapp.callback(Output('dash-container', 'children'), [Input(None, None)])
#         # def callback():
#         #     return get_covid_dataset()
#
#         return dashapp.server
