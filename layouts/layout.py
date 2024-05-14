from dash import html, dcc
from interactions.callbacks import display_tap_node_data
from graphs.figures import NetworkGraph
import dash_bootstrap_components as dbc
from layouts.inputs import layout_inputs

colors = {
    'background': '#FFFFFF',
    'text': '#7FDBFF'
}


network = NetworkGraph(number=1)
fig = network.plot_network_graph()
# cy_graph = network.cyto_graph_plot()


app_layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    # 大标题
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    # 展示散点图绘制的网络图
    html.Div(children='Dash: A web application framework for your data.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-network-graph-scatter',
        figure=fig
    ),

    # 使用cytoscape绘图
    # 添加 cy_graph 到布局中
    html.Div(children=[
        html.H2("Cytoscape Graph"),
        html.Div([
            # cy_graph,
            html.P(id='cytoscape-tapNodeData-output')
        ], className='cyto-network-graph-container'),

        html.Div([
            layout_inputs,
        ], className='input-container')

    ]),


])
