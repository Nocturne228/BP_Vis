from dash import dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc

from graphs.figures import NetworkGraph, generate_pie_chart, generate_edge_pie_chart, generate_link_sankey
from layouts.components import button_group, badges, node_card, edge_card
from graphs.network_graphs import base_cyto_graph
from layouts.inputs import layout_inputs

network = NetworkGraph(number=1)
# fig = network.plot_network_graph()
sankey_fig = generate_link_sankey()
pie_chart = generate_pie_chart()
edge_pie_chart = generate_edge_pie_chart()



navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Source Code", href="https://github.com/Nocturne228/BP_Vis")),
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
                        layout_inputs
                    ],
                    width=2
                ),
                dbc.Col(
                    [
                        button_group,
                        base_cyto_graph,
                        # dcc.Graph(figure=sankey_fig)
                    ],
                    width=6
                ),
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        node_card,
                                        edge_card
                                    ]
                                ),
                            ]
                        ),
                    ],
                    width=4,
                )
            ],
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Graph(figure=sankey_fig),
                    ],
                    width=4,
                ),
                dbc.Col(
                    [
                        dcc.Graph(figure=pie_chart),
                    ],
                    width=4,
                ),
                dbc.Col(
                    [
                        dcc.Graph(figure=edge_pie_chart),
                    ],
                    width=4,
                ),
            ]
        ),
    ],
    style={"marginTop": 20},
)
