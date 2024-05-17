from dash import dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc

from graphs.figures import NetworkGraph, generate_pie_chart, generate_edge_pie_chart, generate_link_sankey
from layouts.inputs import radio_items
from layouts.components import button_group, badges
from graphs.network_graphs import base_cyto_graph

network = NetworkGraph(number=1)
# fig = network.plot_network_graph()
sankey_fig = generate_link_sankey()
pie_chart = generate_pie_chart()
edge_pie_chart = generate_edge_pie_chart()

inputs = html.Div(
    [
    ]
)

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
                        dbc.Alert(
                            id='cytoscape-tapNodeData-output',
                            children='tap to display info of node',
                            color='secondary',
                        ),
                        dbc.Alert(
                            id='cytoscape-tapEdgeData-output'
                        ),
                        inputs,
                        # html.P(id='radio-item-output')
                        badges,
                    ],
                    width=2
                ),
                dbc.Col(
                    [
                        button_group,
                        base_cyto_graph,
                        # dcc.Graph(figure=sankey_fig)
                    ],
                ),
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dcc.Graph(figure=pie_chart),
                                    ],
                                    className='no-gutters',
                                ),
                                dbc.Col(
                                    [
                                        # dcc.Graph(figure=sankey_fig),
                                        dcc.Graph(figure=edge_pie_chart),
                                    ],
                                    className='no-gutters',
                                )
                            ]
                        ),
                        # dcc.Graph(figure=pie_chart),
                        # dcc.Graph(figure=edge_pie_chart),
                    ],
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
