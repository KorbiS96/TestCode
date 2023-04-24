from dash import Dash
from source.components.layout import create_layout
import dash_bootstrap_components as dbc

app = Dash(__name__)
server = app.server
app.title = "GFCC Database"
app.layout = create_layout(app)

if __name__ == "__main__":
    app.run_server()
