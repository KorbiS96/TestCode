from dash import Dash, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash import dcc
from . import ids

def render(app: Dash) -> html.Div:
     
    all_fibers = ["Fiber A", "Fiber B", "Fiber C", "Fiber D", "Fiber E", "Fiber F", "Fiber G", "Fiber H", "Fiber I", "Fiber J", "Fiber K", "Fiber L", "Fiber M", "Fiber N", "Fiber O", "Fiber P", "Fiber Q", "Fiber R", "Fiber S", "Fiber T", "Fiber U", "Fiber V", "Fiber W", "Fiber X", "Fiber Y", "Fiber Z"]


    @app.callback(
        Output(ids.DROPDOWN_FIBERNAME, "value"),
        Input(ids.BUTTON_FIBERNAME, "n_clicks"),
    )
    def select_all_fibers(_: int) -> list[str]:
        return all_fibers

    return html.Div(
        children=[
            html.Div([
                dbc.Label("Fibername"),
                dcc.Dropdown(
                    id= ids.DROPDOWN_FIBERNAME,
                    options = [{"label": fibername, "value": fibername} for fibername in all_fibers],
                    value = all_fibers,
                    clearable=True,
                    multi=True,
                    className="mb-2", 
                    style= {}
                    ),
                dbc.Button("Select All",
                           id= ids.BUTTON_FIBERNAME,
                           style={'height' : 'auto',"padding": "10px"}) #, color="primary"
                ],
            className="mb-4 ms-2 me-2"
            )   
        ]
    )