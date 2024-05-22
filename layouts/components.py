from dash import html, dcc
import dash_bootstrap_components as dbc

from utils.color_palette import label_colors

button_group = html.Div(
    [
        dbc.RadioItems(
            id="radios-button-group",
            className="btn-group",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "资产子图", "value": 1},
                {"label": "关键链路", "value": 2},
                {"label": "核心资产", "value": 3},
                {"label": "违法产业", "value": 4},
                {"label": "邻居查询", "value": 5},
            ],
            value=1,
        ),
    ],
    className="radio-group",
)

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

node_card = dbc.Card(
    [
        dbc.CardHeader("资产节点信息"),
        dbc.CardBody([
            dbc.ListGroup(id='cytoscape-tapNodeData-output')
        ])
    ],
    color='primary',
    outline=True,
)

edge_card = dbc.Card(
    [
        dbc.CardHeader("资产链路信息"),
        dbc.CardBody([
            dbc.ListGroup(id='cytoscape-tapEdgeData-output')
        ])
    ],
    color='secondary',
    outline=True,
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

legend_html = """
<div style="padding: 10px; border: 1px solid transparent; border-radius: 5px; background-color: transparent;">
    <div style="display: flex; align-items: center;">
        <div style="width: 20px; height: 20px; background-color: #fcff00; border: 1px solid #ccc; border-radius: 5px;"></div>
        <div style="margin-left: 5px;">涉黄</div>
    </div>
    <div style="display: flex; align-items: center; margin-top: 5px;">
        <div style="width: 20px; height: 20px; background-color: #fa3586; border: 1px solid #ccc; border-radius: 5px;"></div>
        <div style="margin-left: 5px;">涉赌</div>
    </div>
    <div style="display: flex; align-items: center; margin-top: 5px;">
        <div style="width: 20px; height: 20px; background-color: #5733FF; border: 1px solid #ccc; border-radius: 5px;"></div>
        <div style="margin-left: 5px;">诈骗</div>
    </div>
    <div style="display: flex; align-items: center; margin-top: 5px;">
        <div style="width: 20px; height: 20px; background-color: #acff1a; border: 1px solid #ccc; border-radius: 5px;"></div>
        <div style="margin-left: 5px;">涉毒</div>
    </div>
    <div style="display: flex; align-items: center; margin-top: 5px;">
        <div style="width: 20px; height: 20px; background-color: #FF33FF; border: 1px solid #ccc; border-radius: 5px;"></div>
        <div style="margin-left: 5px;">涉枪</div>
    </div>
    <div style="display: flex; align-items: center; margin-top: 5px;">
        <div style="width: 20px; height: 20px; background-color: #33FFFF; border: 1px solid #ccc; border-radius: 5px;"></div>
        <div style="margin-left: 5px;">黑客</div>
    </div>
    <div style="display: flex; align-items: center; margin-top: 5px;">
        <div style="width: 20px; height: 20px; background-color: #FF8C00; border: 1px solid #ccc; border-radius: 5px;"></div>
        <div style="margin-left: 5px;">非法交易平台</div>
    </div>
    <div style="display: flex; align-items: center; margin-top: 5px;">
        <div style="width: 20px; height: 20px; background-color: #9eb9ff; border: 1px solid #ccc; border-radius: 5px;"></div>
        <div style="margin-left: 5px;">非法支付平台</div>
    </div>
    <div style="display: flex; align-items: center; margin-top: 5px;">
        <div style="width: 20px; height: 20px; background-color: #00FA9A; border: 1px solid #ccc; border-radius: 5px;"></div>
        <div style="margin-left: 5px;">其他</div>
    </div>
</div>
"""

legend_html_component = dcc.Markdown(legend_html, dangerously_allow_html=True)
