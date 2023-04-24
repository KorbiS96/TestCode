from dash import Dash, html
import dash_bootstrap_components as dbc
from . import ids
from dash import Dash, dcc, html, Input, Output
from dash.dependencies import Input, Output, State
import dash

def render(app: Dash) -> html.Div:
    
    return html.Div(
            children=[
                html.Div([
                    dbc.Label("Testmethods"),
                    dcc.Checklist(
                        id= ids.CHECKLIST_TESTMETHOD,
                        options=[
                            {'label': 'Tensile Test', 'value': ids.CHECKLIST_CARD_TT},
                            {'label': 'SFP', 'value': ids.CHECKLIST_CARD_SFP},
                            {'label': 'Beam Test', 'value': ids.CHECKLIST_CARD_BT},
                            {'label': 'Pictures', 'value': ids.CHECKLIST_CARD_PICS}
                            ],
                        value=[ids.CHECKLIST_CARD_TT, ids.CHECKLIST_CARD_SFP, ids.CHECKLIST_CARD_BT, ids.CHECKLIST_CARD_PICS],
                        inline=True,
                        labelStyle={'padding-right': '15px'}
                        ),
                        ],
                        className="mb-4 ms-2 me-2"        
                    ),
            ])

    # all_tests = ["Tensile Test", "SFP", "Beam Test"]

    # return html.Div(
    #     children=[
    #         html.Div([
    #             dbc.Label("Testmethods"),
    #             dbc.Checklist(
    #                 id= ids.CHECKLIST_TESTMETHOD,
    #                 options = [{"label": test, "value": test} for test in all_tests],
    #                 value = all_tests,
    #                 inline=True,
                    
    #                 ),
    #             ],
    #         className="mb-4 ms-2 me-2"
    #         )   
    #     ]
    # )
