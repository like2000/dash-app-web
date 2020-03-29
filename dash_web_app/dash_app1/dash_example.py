"""Create a Dash app within a Flask app."""
from pathlib import Path
from urllib.error import HTTPError

import dash_html_components as html
import dash_table
import pandas as pd
from flask import Flask


def Add_Dash(server: Flask):
    ...


def layout(callback):
    return html.Div(
        id='dash-container',
        className='w3-container w3-green w3-text-black w3-table',
        children=callback(),
    )

    # return dash_app.server


def get_covid_dataset():
    arr = ['This is an example Plot.ly Dash App.']
    arr.append('{% extends "layout.html" %}')

    # {% block body %}
    #
    # {{ super() }}
    #
    # <!-- padding-right = 10% + 10% / 0.8 -->
    # <div class="w3-container w3-light-gray w3-medium">
    #
    #     <br>
    #
    #     <button class="w3-button w3-centering w3-blue-gray material-icons"
    #             style="width: 180px; height: 40px; border: solid 1px darkslategray; margin: auto; display: block;">home
    #     </button>
    #
    #     <br>
    #
    #     <nav>
    #         <a href="/"><i class="fas fa-home"></i> Home</a>
    #         <a href="/dash_app/"><i class="fas fa-chart-line"></i> Embdedded Plotly Dash</a>
    #     </nav>
    # </div>
    #
    # {% endblock %}

    today = pd.to_datetime('today').strftime('%Y-%m-%d')
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


def get_datasets():
    """Return previews of all CSVs saved in /data directory."""
    p = Path('.')
    data_filepath = list(p.glob('data/*.csv'))
    arr = ['This is an example Plot.ly Dash App.']
    for index, csv in enumerate(data_filepath):
        df = pd.read_csv(data_filepath[index]).head(10)
        table_preview = dash_table.DataTable(
            id='table_' + str(index),
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict("rows"),
            sort_action="native",
            sort_mode='single'
        )
        arr.append(table_preview)
    return arr
