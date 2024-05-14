from dash import html, dcc
import dash_bootstrap_components as dbc

# Input layouts
layout_inputs = html.Div([
    html.H3("Inputs"),
    html.Div(children=[
        # Average
        html.Div(children=[
            html.Label("Mean"),
            dcc.Input(id="input-mean", type="number", className="form-control", value=0)
        ]),
    ], className="row"),
    html.Div(children=[
        # Standard Deviation
        html.Div(children=[
            html.Label("Standard Deviation"),
            dcc.Input(id="input-stdv", type="number", className="form-control", value=1)
        ]),
    ], className="row"),
])


radio_items = html.Div(
    [
        dbc.Label("Choose one"),
        dbc.RadioItems(
            options=[
                {"label": "显示核心资产", "value": 1},
                {"label": "显示关键链路", "value": 2},
                {"label": "Disabled Option", "value": 3},
            ],
            value=3,
            id="radio-items-input",
        ),
    ]
)

