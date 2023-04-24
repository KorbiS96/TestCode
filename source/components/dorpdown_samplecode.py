from dash import Dash, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash import dcc
from . import ids

def render(app: Dash) -> html.Div:
    all_codes = ["2020-0049", "2020-0056", "2020-0076", "2021-0049", "2021-0056", "2021-0076"]

    @app.callback(
        Output(ids.DROPDOWN_SAMPLECODE, "value"),
        Input(ids.BUTTON_SAMPLECODE, "n_clicks"),
    )
    def select_all_codes(_: int) -> list[str]:
        return all_codes
    
    return html.Div(
        children=[
            html.Div([
                dbc.Label("Sample Code"),
                dcc.Dropdown(
                    id= ids.DROPDOWN_SAMPLECODE,
                    options = [{"label": samplecode, "value": samplecode} for samplecode in all_codes],
                    value = all_codes,
                    clearable=True,
                    multi=True,
                    className="mb-2",
                    ),
                dbc.Button("Select All",
                           id= ids.BUTTON_SAMPLECODE,
                           style={'height' : 'auto',"padding": "10px"}) #, color="primary"
                ],
            className="mb-4 ms-2 me-2"
            )   
        ]
    )