from dash import Dash, dcc, html, Input, Output
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
from dash import dash_table
from . import ids

file_path = "mean_results_tensile_test.txt"
# Daten als DataFrame importieren
df = pd.read_csv(file_path, sep=";")
df = df.round(3)

def render(app: Dash) -> html.Div:


    @app.callback(
    Output(ids.CARD_BT, 'children'),
    [Input(ids.BUTTON_BT, 'n_clicks')]
    )
    def update_card(n_clicks):
        return html.Div(
            dash_table.DataTable(
            id=ids.TABLE_BT,
            columns=[{"name": i, "id": i, "hideable": True} for i in df.columns],
            data=df.to_dict("records"),
            sort_action="native",
            #page_size=100,
            style_as_list_view=True,
            fixed_rows={'headers': True},
            style_table={'overflowY': 'auto','overflowX': 'auto',  "max-height" : "400px", 'textOverflow': 'ellipsis', 'minWidth': '100%' },
            style_cell={},
            style_header={
                'textAlign': 'left',
                'font-size': '18px',
                'backgroundColor': 'white',
                'fontWeight': '900',
                'border': '3px solid black'
             },
            style_cell_conditional=[
            {'if': {'column_id': 'Sample Code'},                'width': '160px', 'textAlign': 'right'},
            {'if': {'column_id': 'Fibername'},                  'width': '150px', 'textAlign': 'right'}, 
            {'if': {'column_id': 'max Elongation [%]'},         'width': '170px', 'textAlign': 'right'}, 
            {'if': {'column_id': 'UTS [MPa]'},                  'width': '150px', 'textAlign': 'right'}, 
            {'if': {'column_id': 'E-M (10-30%) [GPa]'},         'width': '170px', 'textAlign': 'right'}, 
            {'if': {'column_id': 'Länge [mm]'},                 'width': '150px', 'textAlign': 'right'}, 
            {'if': {'column_id': 'D_max [mm]'},                 'width': '150px', 'textAlign': 'right'}, 
            {'if': {'column_id': 'D_min [mm]'},                 'width': '150px', 'textAlign': 'right'}, 
            {'if': {'column_id': 'D_eq [mm]'},                  'width': '150px', 'textAlign': 'right'}, 
            {'if': {'column_id': 'Weight [g]'},                 'width': '150px', 'textAlign': 'right'}, 
            {'if': {'column_id': 'A_cs [mm²]'},                 'width': '150px', 'textAlign': 'right'},              
            ],
            ),
            
        )


    return html.Div(
        children = [
        html.Div([
        html.Div(
        id = ids.CARD_BT,
        children= [
            dash_table.DataTable(
            id=ids.TABLE_BT,
            columns=[{"name": i, "id": i, "hideable": True} for i in df.columns],
            data=df.to_dict("records"),
            sort_action="native",
            style_as_list_view=True,
            fixed_rows={'headers': True, 'data': 1},
            style_table={'overflowY': 'auto','overflowX': 'auto',  "max-height" : "400px", 'textOverflow': 'ellipsis', 'minWidth': '100%'},
            style_cell={},
            style_header={
                'textAlign': 'left',
                'font-size': '18px',
                'backgroundColor': 'white',
                'fontWeight': '900',
                'border': '3px solid black'
             },
            style_cell_conditional=[
            {'if': {'column_id': 'Sample Code'},                'width': '160px', 'textAlign': 'right'},
            {'if': {'column_id': 'Fibername'},                  'width': '150px', 'textAlign': 'right'}, 
            {'if': {'column_id': 'max Elongation [%]'},         'width': '170px', 'textAlign': 'right'}, 
            {'if': {'column_id': 'UTS [MPa]'},                  'width': '150px', 'textAlign': 'right'}, 
            {'if': {'column_id': 'E-M (10-30%) [GPa]'},         'width': '170px', 'textAlign': 'right'}, 
            {'if': {'column_id': 'Länge [mm]'},                 'width': '150px', 'textAlign': 'right'}, 
            {'if': {'column_id': 'D_max [mm]'},                 'width': '150px', 'textAlign': 'right'}, 
            {'if': {'column_id': 'D_min [mm]'},                 'width': '150px', 'textAlign': 'right'}, 
            {'if': {'column_id': 'D_eq [mm]'},                  'width': '150px', 'textAlign': 'right'}, 
            {'if': {'column_id': 'Weight [g]'},                 'width': '150px', 'textAlign': 'right'}, 
            {'if': {'column_id': 'A_cs [mm²]'},                 'width': '150px', 'textAlign': 'right'},  
            ],
            ),
            ]),
        
    html.Div(
        dbc.Button(
            "Reset Table",
            id= ids.BUTTON_BT,
            color="primary",
            style={'width': '150px','height' : 'auto',"padding": "10px"}
                ),
                className="mt-4",
                style={'text-align': 'right'}
            ),
            
        ])
    ])

