from urllib.error import HTTPError

import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
from dash import Dash
from dash.dependencies import Input, Output
from flask import Flask

url_base = '/dash/app1/'


def get_covid_dataset():
    arr = ['This is an example Plotly Dash App.']

    today = pd.to_datetime('today').strftime('%Y-%m-%d')
    today = (pd.to_datetime('today') - pd.to_timedelta('1 days')).strftime('%Y-%m-%d')
    link = f'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-{today}.xls'
    print(f"\n*** Searching file {link}...")

    try:
        link = f'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-{today}.xls'
        df = pd.read_excel(link)
    except HTTPError as err:
        link = f'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-{today}.xlsx'
        df = pd.read_excel(link)

    print(f"\n*** Successfully read file {link} from ecdc.")
    print(df.head())

    table_preview = dash_table.DataTable(
        id='table_covid',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("rows"),
        sort_action="native",
        sort_mode='single'
    )
    arr.append(table_preview)

    return arr


layout = html.Div([
    html.Div('This is dash app1'), html.Br(),
    dcc.Input(id='input_text'), html.Br(), html.Br(),
    html.Div(id="output"), html.Br(), html.Br(),
    html.Div(id='target', className='w3-container w3-green w3-text-black w3-table', children=get_covid_dataset())
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
