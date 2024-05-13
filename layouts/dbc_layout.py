from dash import dcc, html
import dash_bootstrap_components as dbc
from graphs.figures import NetworkGraph
from interactions.callbacks import display_tap_node_data, on_form_change

network = NetworkGraph(number=1)
fig = network.plot_network_graph()
cy_graph = network.cyto_graph_plot()

switches = html.Div(
    [
        dbc.Label("Toggle a bunch"),
        dbc.Checklist(
            options=[
                {"label": "显示核心资产", "value": 1},
                {"label": "显示关键链路", "value": 2},
                {"label": "Disabled Option", "value": 3, "disabled": True},
            ],
            value=[1],
            id="switches-input",
            switch=True,
        ),
    ]
)

inputs = html.Div(
    [
        dbc.Form([switches]),
        html.P(id="switches-output"),
    ]
)

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Source Code", href="https://github.com/Nocturne228/BP_Vis")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="黑灰产业网络资产图谱分析",
    brand_href="#",
    color="primary",
    dark=True,
)

body_layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Col(
                            [
                                dbc.Alert(
                                    id='cytoscape-tapNodeData-output',
                                    children='tap to display info of node',
                                    color='secondary',
                                )
                            ],
                        ),
                        dbc.Col(
                            [
                                inputs
                            ],
                        )
                    ],
                    width=2  # 设置 inputs 列的宽度为 3

                ),
                dbc.Col(
                    [
                        cy_graph
                    ],
                    width=10
                ),
            ]
        )

    ],
    style={"marginTop": 20},
)
