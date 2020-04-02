from urllib.error import HTTPError

import dash_core_components as dcc
import dash_html_components as html
import dash_table
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash
from dash.dependencies import Input, Output
from flask import Flask

url_base = '/dash/app1/'

countriesTag = 'countriesAndTerritories'
countries = ['China', 'South_Korea', 'Japan',
             # ' Singapore',
             #  'Austria',
             'France', 'Germany',
             'Italy', 'Switzerland', 'United_Kingdom', 'United_States_of_America']


def read_covid_data() -> pd.DataFrame:
    # today = (pd.to_datetime('today') - pd.to_timedelta('0 days')).strftime('%Y-%m-%d')
    # link = f'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-{today}.xls'

    try:
        today = (pd.to_datetime('today') - pd.to_timedelta('0 days')).strftime('%Y-%m-%d')
        link = f'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-{today}.xlsx'
        print(f"\n*** Retrieving file {link}...")
        df = pd.read_excel(link)
    except HTTPError as err:
        today = (pd.to_datetime('today') - pd.to_timedelta('1 days')).strftime('%Y-%m-%d')
        link = f'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-{today}.xlsx'
        print(f"\n*** Retrieving file {link}...")
        df = pd.read_excel(link)

    print(df.head())

    ##
    countries = df[countriesTag].unique()
    print(countries)

    # Filter
    ix = list(map(lambda c: c in countries, df[countriesTag]))
    df = df[ix]
    da = df.copy()

    da["AccumulatedCases"] = 0
    for cn in countries:
        ix = da[countriesTag] == cn
        da["AccumulatedCases"][ix] = da.cases[ix][::-1].cumsum()

    # %% Fine adjustments
    limit = 100
    t0 = pd.to_datetime("2020-01-15")
    da = da.loc[da['AccumulatedCases'] > limit]

    return da


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

    ix = np.any([c == df[countriesTag] for c in countries], axis=0)
    df = df[ix]
    fig: go.Figure = px.scatter(df, x="dateRep", y="AccumulatedCases", color=countriesTag).update_traces(
        mode='lines+markers')
    print(type(fig))
    for trace in fig.data:
        trace.name = trace.name.split('=')[1]
    plot = dcc.Graph(
        id='graph-covid-overview',
        figure=fig,
    )
    # plot = dcc.Graph(
    #     id='graph-covid-overview',
    #     figure={
    #         'data': [
    #             dict(
    #                 x=df[df[countriesTag] == i]['dateRep'],
    #                 y=df[df[countriesTag] == i]['AccumulatedCases'],
    #                 text=df[df[countriesTag] == i][countriesTag],
    #                 name=i,
    #                 mode='line',
    #                 opacity=0.7,
    #                 marker={
    #                     'size': 15,
    #                     'line': {'width': 2},  # , 'color': 'white'}
    #                 },
    #             ) for i in countries
    #         ],
    #         'layout': dict(
    #             xaxis={'type': 'linear', 'title': 'Time after cross 100'},
    #             yaxis={'type': 'linear', 'title': 'Covid-19 cases'},
    #             # margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
    #             legend={'x': 0, 'y': 1},
    #             hovermode='closest'
    #         )
    #     }
    # )
    arr.append(plot)

    return arr


layout = html.Div([
    html.Div('This is dash app1'), html.Br(),
    dcc.Input(id='input_text'), html.Br(), html.Br(),
    html.Div(id="output"), html.Br(), html.Br(),
    html.Div(id='target', className='w3-container w3-green w3-text-black w3-table',
             children=make_line_from_df(read_covid_data()))
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
