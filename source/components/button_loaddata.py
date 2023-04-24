from dash import Dash, html
import dash_bootstrap_components as dbc
from . import ids

def render(app: Dash) -> html.Div:
    return html.Div(
        children=[
            html.Div([
                    dbc.Button(
                    "Reload Data",
                    id= ids.BUTTON_LOADDATA,
                    #color="primary",
                    style={'width': '100%','height' : 'auto',"padding": "10px"},
                    n_clicks=0,
                    ),
                ],
            className="mb-4 ms-2 me-2"
            )   
        ]
    )
