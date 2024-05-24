from dash import dcc, html
import dash_bootstrap_components as dbc

from layouts.components import button_group, node_card, edge_card, navbar, legend_html_component
from graphs.network_graphs import base_cyto_graph
from layouts.inputs import inputs_container
from figures.fig_collections import pie_chart, edge_pie_chart

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
                        # 存储图例显示状态的组件
                        html.Div(
                            [
                                # base_cyto_graph,
                                # 将图例添加到 base_cyto_graph 的内部
                                legend_html_component,
                            ],
                            id="legend-html-component",
                            style={
                                "position": "absolute",
                                "top": "110px",  # 调整图例距离顶部的距离
                                "left": "985px",  # 调整图例距离左侧的距离
                                "z-index": 9999,  # 确保图例在最顶层显示
                                "background-color": "transparent",  # 背景颜色
                                "padding": "10px",  # 内边距
                                "border-radius": "5px",  # 边框圆角
                                "border": "1px solid transparent",  # 边框样式
                            }
                        ),
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
            style={"height": "600px"}  # 设置高度为 300px
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Graph(
                            id='sankey-fig',
                        ),
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
        dbc.Row(
            dbc.Label("test")
        )
    ],
    style={"marginTop": 20},
)
