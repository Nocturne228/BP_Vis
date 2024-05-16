# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
from dash import Dash, html
from layouts.layout import app_layout
from layouts.dbc_layout import body_layout, navbar
import dash_bootstrap_components as dbc


app = Dash(external_stylesheets=[dbc.themes.VAPOR])

# app.layout = app_layout
app.layout = html.Div([navbar, body_layout])

if __name__ == '__main__':
    app.run(debug=True)
