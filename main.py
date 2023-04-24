from dash import Dash, html
from source.components.layout import create_layout
import dash_bootstrap_components as dbc

# stylesheet with the .dbc class
server = app.server

def main () -> None:
    app = Dash()
    app.title = "GFCC Database"
    app.layout = create_layout(app)
    app.run()

if __name__ == "__main__":
    main() 
