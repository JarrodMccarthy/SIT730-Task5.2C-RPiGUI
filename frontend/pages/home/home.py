import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_daq as daq
# import assets
# from app import app
# import pandas as pd
# import os
# import plotly.graph_objects as go
# import plotly.express as px
from pages.home import home_callbacks
# from pages.home import home_data
# #from utils.constants import optimiser_page_location, location_page_location, schedule_page_location, cooke_report_page_location
# import base64


layout = dbc.Container([
    dbc.Row(
        [
            html.H6("Power"),
            html.Hr(),
            dbc.Col(
            [
                daq.PowerButton(id='green', on=False),
                daq.PowerButton(id='amber', on=False),
                daq.PowerButton(id='red', on=False),
            ],
        ),
    ],
    justify="between"
    ),
    html.Hr(),
    dbc.Row(
        [
            dbc.Col(html.Div(id='overview-div', children=[]), width=12)
        ],
        justify="between",
    ),
    html.Div(id='dummy-display', children = [])
])
