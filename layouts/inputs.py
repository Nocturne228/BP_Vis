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
            dbc.Label('链路跳数：', color='white', class_name='mt-2'),
            dbc.Input(id="jumps-button-input", type="number", min=0, max=5, step=1, value=1),
        ],
        class_name='mb-4'
    ),
)


team_select = html.Div(
    [
        dbc.Label("选择分析团伙", class_name='mt-3', color='white'),
        dbc.Select(
            [
                "团伙1",
                "团伙2",
                "团伙3",
                "团伙4",
                "团伙5",
                "团伙6",
                "团伙7",
                "团伙8",
                "团伙9",
                "团伙10",
            ],
            "团伙1",
            id="select-team",
            class_name='mb-4'
        ),
    ],
)


inputs_container = html.Div([
    dbc.Label('选择团伙', color='white', class_name='h2'),
    team_select,
    dbc.Label('图信息选项', color='white', class_name='h3'),
    html.Div([
        # layout_inputs,
        graph_layouts_select,
        jumps_input_group
    ], className="input-box")
])


