from dash import dcc, html
import dash_bootstrap_components as dbc
from graphs.figures import NetworkGraph, generate_pie_chart, generate_edge_pie_chart, generate_link_sankey
from layouts.inputs import radio_items
from utils.color_palette import label_colors
from graphs.network_graphs import base_cyto_graph

network = NetworkGraph(number=1)
fig = network.plot_network_graph()
sankey_fig = generate_link_sankey()
pie_chart = generate_pie_chart()
edge_pie_chart = generate_edge_pie_chart()

badges = html.Span(
    [
        dbc.Badge("Domain", pill=True, color=label_colors["Domain"], className="me-1"),
        dbc.Badge("Whois_Phone", pill=True, color=label_colors["Whois_Phone"], className="me-1"),
        dbc.Badge("Whois_Email", pill=True, color=label_colors["Whois_Email"], className="me-1"),
        dbc.Badge("Whois_Name", pill=True, color=label_colors["Whois_Name"], className="me-1"),
        dbc.Badge("IP", pill=True, color=label_colors["IP"], className="me-1"),
        dbc.Badge("IP_C", pill=True, color=label_colors["IP_C"], className="me-1"),
        dbc.Badge("Cert", pill=True, color=label_colors["Cert"], className="me-1"),
        dbc.Badge("ASN", pill=True, color=label_colors["ASN"], className="me-1"),
    ]
)

# switches = html.Div(
#     [
#         dbc.Label("展示关键信息"),
#         dbc.Checklist(
#             options=[
#                 {"label": "显示核心资产", "value": 1},
#                 {"label": "显示关键链路", "value": 2},
#                 {"label": "默认显示", "value": 3, "disabled": True},
#             ],
#             value=[1],
#             id="switches-input",
#             switch=True,
#         ),
#     ]
# )

inputs = html.Div(
    [
        dbc.Form([radio_items]),
    ]
)

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Source Code", href="https://github.com/Nocturne228/BP_Vis")),
        # dbc.DropdownMenu(
        #     children=[
        #         dbc.DropdownMenuItem("More pages", header=True),
        #         dbc.DropdownMenuItem("Page 2", href="#"),
        #         dbc.DropdownMenuItem("Page 3", href="#"),
        #     ],
        #     nav=True,
        #     in_navbar=True,
        #     label="More",
        # ),
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
                                ),
                                dbc.Alert(
                                    id='cytoscape-tapEdgeData-output'
                                ),
                            ],
                        ),
                        dbc.Col(
                            [
                                inputs,
                                # html.P(id='radio-item-output')
                                html.Div(id='radio-item-output', style={'display': 'none'})  # 隐藏的输出组件
                            ],
                        ),
                        dbc.Col(
                            [
                                badges,
                            ]
                        ),
                    ],
                    width=2
                ),
                dbc.Col(
                    [
                        base_cyto_graph,
                        dcc.Graph(figure=sankey_fig)
                    ],
                ),
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dcc.Graph(figure=pie_chart),
                                dcc.Graph(figure=edge_pie_chart),
                            ]
                        ),
                        # dcc.Graph(figure=pie_chart),
                        # dcc.Graph(figure=edge_pie_chart),
                    ],
                    width=4
                )
            ],
        ),
    ],
    style={"marginTop": 20},
)
