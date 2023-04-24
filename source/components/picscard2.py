from dash import Dash, html
from dash import dcc
from dash.dependencies import Input, Output,State
import dash_bootstrap_components as dbc
from . import ids
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image
from io import BytesIO
import base64

def render(app: Dash) -> html.Div:

    alert = dbc.Alert("Invalid file type. Please upload only PNG or JPG image files.", color="danger", dismissable=True, style= {'width': '99%',
                    'height': 'auto',
                    'borderRadius': '5px',
                    'margin': '10px'})

    def parse_contents(contents, filename):
        btns = [
            "drawline",
            "drawopenpath",
            "drawclosedpath",
            "drawcircle",
            "drawrect",
            "eraseshape",
        ]
        if 'png' in filename or 'jpg' in filename:
                content_type, content_string = contents.split(',')
                image_data = BytesIO(base64.b64decode(content_string))
                img = Image.open(image_data).convert("RGBA")

                fig_img = go.Figure(px.imshow(img))
                fig_img.add_trace(
                    go.Scatter(
                        mode="markers",
                        marker_opacity=0,
                    )
                )
                fig_img.update_xaxes(visible=False)
                fig_img.update_yaxes(visible=False)
                fig_img.update_layout(
                    margin={"l": 0, "r": 0, "t": 0, "b": 0},
                    hovermode=False
                )

                return dcc.Graph(figure=fig_img,
                                 style={
                    'width': '99%',
                    'object-fit': 'contain',
                    'margin': '10px'
                    },
                    config={"modeBarButtonsToAdd": btns})
        else:
            return alert

    @app.callback(Output(ids.SHOW_IMAGE2, 'children'),
                  [Input(ids.UPLOAD_IMAGE2, 'contents')],
                  State(ids.UPLOAD_IMAGE2, 'filename'),
                  )
    def update_output(list_of_contents, list_of_names):
        if list_of_contents is not None:
            children = [
                parse_contents(c, n) for c, n in
                zip(list_of_contents, list_of_names)]
            return children

    @app.callback(
        Output(ids.PICS_CARD2, "children"),
        [Input(ids.BUTTON_CLEARPICS2, "n_clicks")])
    def clear_pics(n_clicks):
        return html.Div(
        id = ids.PICS_CARD2,
        children=[

                    dcc.Upload(
                        id= ids.UPLOAD_IMAGE2,
                        children=html.Div([
                        'Drag and Drop or ',
                        html.A('Browse Image', href='javascript:void(0)', style={'fontWeight': '900', 'color': 'blue', 'textDecoration': 'underline'})
                            ]),
                        style={
                            'width': '99%',
                            'height': 'auto',
                            'lineHeight': '40px',
                            'borderWidth': '1px',
                            'borderStyle': 'dashed',
                            'borderRadius': '5px',
                            'textAlign': 'center',
                            'margin': '10px'
                        },
                            multiple=True
            ),
            
            html.Div(id= ids.SHOW_IMAGE2, children= []),
            html.Div(id= ids.PICS_ALERT2, children= []),
            html.Div(dbc.Button("Clear Pictures",
                           id= ids.BUTTON_CLEARPICS2,
                           style={'height' : 'auto','width': '99%',"padding": "10px",'margin': '10px'}),
                
                #className="mt-4 mb-4",
                #style={'text-align': 'right'}
                ),

        ],

    )

    


    return html.Div(
        id = ids.PICS_CARD2,
        children=[
                    
                    dcc.Upload(
                        id= ids.UPLOAD_IMAGE2,
                        children=html.Div([
                        'Drag and Drop or ',
                        html.A('Browse Image(s)', href='javascript:void(0)', style={'fontWeight': '900', 'color': 'blue', 'textDecoration': 'underline'})
                            ]),
                        style={
                            'width': '99%',
                            'height': 'auto',
                            'lineHeight': '40px',
                            'borderWidth': '1px',
                            'borderStyle': 'dashed',
                            'borderRadius': '5px',
                            'textAlign': 'center',
                            'margin': '10px'
                        },
                            multiple=True
            ),
            
            html.Div(id= ids.SHOW_IMAGE2, children= []),
            html.Div(id= ids.PICS_ALERT2, children= []),
            html.Div(dbc.Button("Clear Pictures",
                           id= ids.BUTTON_CLEARPICS2,
                           style={'height' : 'auto','width': '99%',"padding": "10px",'margin': '10px'}),
                
                #className="mt-4 mb-4",
                #style={'text-align': 'right'}
                ),

        ],

    )