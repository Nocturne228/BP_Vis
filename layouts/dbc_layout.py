from dash import dcc, html
import dash_bootstrap_components as dbc
from graphs.figures import NetworkGraph, generate_pie_chart
from layouts.inputs import radio_items
from utils.color_palette import label_colors

network = NetworkGraph(number=1)
fig = network.plot_network_graph()
cy_graph = network.cyto_graph_plot()
pie_chart = generate_pie_chart()

badges = html.Span(
    [
        dbc.Badge("Domain", pill=True, color=label_colors["Domain"], className="me-1"),
        dbc.Badge("Whois_Phone", pill=True, color=label_colors["Whois_Phone"], className="me-1"),
        dbc.Badge("Whois_Email", pill=True, color=label_colors["Whois_Email"], className="me-1"),
        dbc.Badge("WWhois_Name", pill=True, color=label_colors["Whois_Name"], className="me-1"),
        dbc.Badge("IP", pill=True, color=label_colors["IP"], className="me-1"),
        dbc.Badge("IP_C", pill=True, color=label_colors["IP_C"], className="me-1"),
        dbc.Badge("Cert", pill=True, color=label_colors["Cert"], className="me-1"),
        dbc.Badge("ASN", pill=True, color=label_colors["ASN"], className="me-1"),
        dbc.Badge(
            "Light",
            pill=True,
            color="light",
            text_color="dark",
            className="me-1",
        ),
        dbc.Badge("Dark", pill=True, color="dark"),
    ]
)

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
        dbc.Form([radio_items, switches]),
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
                    width=2
                ),
                dbc.Col(
                    [
                        cy_graph,
                    ],
                ),
                dbc.Col(
                    [
                        dbc.Alert(
                            id='cytoscape-tapEdgeData-output'
                        ),
                        badges,
                        dcc.Graph(figure=pie_chart)
                    ],
                    width=4
                )
            ],
        ),
        dbc.Row(
            [
                badges
            ]
        )
    ],
    style={"marginTop": 20},
)
