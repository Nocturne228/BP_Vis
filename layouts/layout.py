from dash import html, dcc
from graphs.figures import NetworkGraph

colors = {
    'background': '#FFFFFF',
    'text': '#7FDBFF'
}


network = NetworkGraph(number=1)
fig = network.plot_network_graph()
cy_graph = network.cyto_graph_plot()


app_layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for your data.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-network-graph-scatter',
        figure=fig
    ),

    # 添加 cy_graph 到布局中
    html.Div(children=[
        html.H2("Cytoscape Graph"),
        cy_graph
    ])

])
