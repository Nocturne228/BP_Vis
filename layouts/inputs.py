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

graph_layouts_select = html.Div(
    [
        dbc.Label("图谱布局", class_name='mt-3', color='white'),
        dbc.Select(
            [
                "cose",
                "random",
                "concentric",
                "circle",
                "grid",
                "breadthfirst",
            ],
            "cose",
            id="dropdown-update-layout",
            class_name='mb-4'
        ),
    ],
)

jumps_input_group = html.Div(
    dbc.InputGroup(
        [
            dbc.Label('查询邻居节点和链路', color='white'),
            dbc.Button("查询", id="check-node-subgraph-button", n_clicks=0),
            dbc.Input(id="jumps-button-input", type='number', placeholder="输入跳数", class_name='form-control'),
        ],
        class_name='mb-4'
    ),
)

inputs_container = html.Div([
    dbc.Label('图信息选项', color='white', class_name='h3'),
    html.Div([
        # layout_inputs,
        graph_layouts_select,
        jumps_input_group
    ], className="input-box")
])
