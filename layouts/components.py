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
