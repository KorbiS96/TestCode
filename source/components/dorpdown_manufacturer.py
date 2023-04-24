from dash import Dash, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash import dcc
from . import ids

def render(app: Dash) -> html.Div:
    all_manufacturers = ["MBS", "Adril", "Mighty Shield"]

    @app.callback(
        Output(ids.DROPDOWN_MANUFACTURER, "value"),
        Input(ids.BUTTON_MANUFACTURER, "n_clicks"),
    )
    def select_all_manufacturers(_: int) -> list[str]:
        return all_manufacturers

    return html.Div(
        children=[
            html.Div([
                dbc.Label("Manufacturer"),
                dcc.Dropdown(
                    id= ids.DROPDOWN_MANUFACTURER,
                    options = [{"label": manufacturer, "value": manufacturer} for manufacturer in all_manufacturers],
                    value = all_manufacturers,
                    clearable=True,
                    multi=True,
                    className="mb-2",
                    ),
                dbc.Button("Select All",
                           id= ids.BUTTON_MANUFACTURER,
                           style={'height' : 'auto',"padding": "10px"}) #, color="primary"
                ],
            className="mb-4 ms-2 me-2"
            )   
        ]
    )