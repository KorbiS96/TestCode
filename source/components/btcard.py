from dash import Dash, html
import dash
from dash.dependencies import Input, Output,State
import dash_bootstrap_components as dbc
from dash import dcc
from . import ids
from . import bt_table
import pandas as pd
import dash.exceptions 


def render(app: Dash) -> html.Div:
    return html.Div(
        children=[
            html.Div(
            dbc.CardBody([
            html.H4("Beam Bending Test", className="card-title text-center mb-3"),
            html.Hr(),
            html.H5("Test Results", className="mb-1"),
            dbc.Row([
                dcc.Graph(
                id= ids.GRAPH_BT,
                style={"height": '800px', 'width': '1000px',"margin": "auto"},
                className="mb-3"
                ),
                html.Hr(className="mb-3",
                        style={'width': '98.5%',"margin": "auto"}),
                html.H5("Statistics", className="mb-3"),
                bt_table.render(app),
                    ],
                )   
            ]
            ),
            )
        ],

    )