# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
from dash import Dash
from layouts.layout import app_layout


app = Dash(__name__)

app.layout = app_layout

if __name__ == '__main__':
    app.run(debug=True)
