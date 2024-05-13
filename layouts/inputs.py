from dash import html, dcc

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