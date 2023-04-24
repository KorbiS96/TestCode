import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from . import ids

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        dcc.Checklist(
            id= ids.CHECKLIST_TESTMETHOD,
            options=[
                {'label': 'Card 1', 'value': 'card1'},
                {'label': 'Card 2', 'value': 'card2'},
            ],
            value=['card1', 'card2'],
        ),
    ], style={'width': '30%'}),

    html.Div([
        html.Div([
            html.H3('Card 1'),
            html.P('This is the content of Card 1'),
        ], id='card1', style={'display': 'block'}),

        html.Div([
            html.H3('Card 2'),
            html.P('This is the content of Card 2'),
        ], id='card2', style={'display': 'block'}),
    ]),
])

@app.callback(
    Output('card1', 'style'),
    Output('card2', 'style'),
    Input('checklist', 'value'),
)
def update_cards(selected):
    card1_style = {'display': 'none'}
    card2_style = {'display': 'none'}
    if 'card1' in selected:
        card1_style = {'display': 'block'}
    if 'card2' in selected:
        card2_style = {'display': 'block'}
    return card1_style, card2_style

if __name__ == '__main__':
    app.run_server(debug=True)
