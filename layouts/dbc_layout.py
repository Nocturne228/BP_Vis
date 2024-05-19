from dash import dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc

from layouts.components import button_group, badges, node_card, edge_card, navbar
from graphs.network_graphs import base_cyto_graph
from layouts.inputs import inputs_container
from figures.fig_collections import sankey_fig, pie_chart, edge_pie_chart


body_layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        inputs_container,
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
