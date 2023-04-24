from dash import Dash, html
import dash_bootstrap_components as dbc

def render(app: Dash) -> html.Div:
    return html.Div(
        children=[
            dbc.Card(
            dbc.CardBody([
            html.H4("Single Fiber Pull-out", className="card-title text-center mb-3"),
            html.Hr(),
            html.H5("Test Results", className="mb-1"),
            dbc.Row([
                html.H4("Platzhalter dbcGraph SPO"),
                html.Hr(style={'width': '98.5%',"margin": "auto"}),
                html.H5("Statistics", className="mb-3"),
                html.H6("Platzhalter dbcGraph dash_table.DataTable"),
                html.Div(
                    dbc.Button(
                        "Reset Table",
                        color="primary",
                        style={'width': '200px'}
                            ),
                            style={'text-align': 'right'}
                        ),
                    ],
                )   
            ]
            ),
            width=3,

            className="mb-3",
            )
        ],

    )