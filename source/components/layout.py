from dash import Dash, html
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output
from . import dorpdown_samplecode
from . import dorpdown_fibername
from . import dorpdown_manufacturer
from . import checklist_testmethod
from . import button_fulltestseries
from . import button_loaddata
from . import ttcard
from . import spocard
from . import btcard
from . import picscard1
from . import picscard2
from . import ids




def create_layout(app: Dash)  -> html.Div:

    @app.callback(
    Output(ids.CHECKLIST_CARD_TT, 'style'),
    Output(ids.CHECKLIST_CARD_SFP, 'style'),
    Output(ids.CHECKLIST_CARD_BT, 'style'),
    Output(ids.CHECKLIST_CARD_PICS, 'style'),
    Input(ids.CHECKLIST_TESTMETHOD, 'value'),
    )
    def update_cards(selected):
        card_tt_style = {'display': 'none'}
        card_sfp_style = {'display': 'none'}
        card_bt_style = {'display': 'none'}
        card_pics_style = {'display': 'none'}
        if ids.CHECKLIST_CARD_TT in selected:
            card_tt_style = {'display': 'block'}
        if ids.CHECKLIST_CARD_SFP in selected:
            card_sfp_style = {'display': 'block'}
        if ids.CHECKLIST_CARD_BT in selected:
            card_bt_style = {'display': 'block'}
        if ids.CHECKLIST_CARD_PICS in selected:
            card_pics_style = {'display': 'block'}
        return card_tt_style, card_sfp_style, card_bt_style, card_pics_style

    return html.Div(
        className="app-div",
        children=[
                dbc.Container([
                    dbc.Row([
                        html.H2(app.title, className="bg-primary text-white p-2 mb-2 text-center"),
                        ]
                        ),
                    dbc.Row([
                        dbc.Col([
                            dbc.Card([
                                html.Div(
                                    dbc.CardHeader("Filter"),
                                    className="mb-4"
                                    ),
                                html.Div(
                                    className= "button-container",
                                    children= [button_loaddata.render(app)]
                                    ),
                                html.Div(
                                    className= "button-container",
                                    children= [button_fulltestseries.render(app)]
                                    ),
                                html.Div(
                                    className= "checklist-container",
                                    children= [checklist_testmethod.render(app)]
                                    ),
                                html.Div(
                                    className= "dropdown-container",
                                    children= [dorpdown_samplecode.render(app)]
                                    ),
                                html.Div(
                                    className= "dropdown-container",
                                    children= [dorpdown_fibername.render(app)]
                                    ),
                                html.Div(
                                    className= "dropdown-container",
                                    children= [dorpdown_manufacturer.render(app)]
                                    ),
                                ],
                            style={'position': 'fixed', "width": "24%", "height": "90%", "overflowY": "auto"}
                                )
                                ],
                                width=3,
                            ),
                        dbc.Col([
                            dbc.Card(      
                                    id = ids.CHECKLIST_CARD_TT,
                                    style={'display': 'block'},
                                    className= "tt-container mb-3",
                                    children= [ttcard.render(app)]
                                    ),
                            dbc.Card(  
                                    id = ids.CHECKLIST_CARD_SFP,
                                    style={'display': 'block'},          
                                    className= "spo-container mb-3",
                                    children= [spocard.render(app)]
                                    ),
                            dbc.Card(
                                    id = ids.CHECKLIST_CARD_BT,
                                    style={'display': 'block'}, 
                                    className= "bt-container mb-3",
                                    children= [btcard.render(app)]
                                    ),
                            dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H4("Visual Assessment", className="card-title mb-3 text-center"),
                                    html.Hr(),
                                    dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                            html.Div(
                                               className= "upload-image1",
                                               children= [picscard1.render(app)]
                                               ),
                                            ],
                                            width=6
                                        ),
                                        dbc.Col(
                                            [
                                            html.Div(
                                               className= "upload-image2",
                                               children= [picscard2.render(app)]
                                               ),
                                            ],
                                            width=6
                                        ),
                                    ],
                                )

                                ]
                            ),
                            className="mb-4",
                            id = ids.CHECKLIST_CARD_PICS,
                            style={'display': 'block'},
                        ),
                    ],
                    width=9,
                ),
            ]
        ),
    ],
    fluid=True,
    className="dbc",
)
        ]
    )

