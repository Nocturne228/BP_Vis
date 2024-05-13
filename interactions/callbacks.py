from dash import Input, Output, callback


@callback(Output('cytoscape-tapNodeData-output', 'children'),
          Input('cyto-network-graph', 'tapNodeData'))
def display_tap_node_data(data):
    if data:
        return "Node: " + data['label']


@callback(
    Output("inputs-output", "children"),
    [
        Input("radioitems-input", "value"),
    ],
)
def on_form_change(radio_items_value):
    return radio_items_value


# TODO 根据radio item的值显示不同的图像.
# @callback(
#     Output('cyto-network-graph', 'elements'),
#     Input('inputs-output', 'children')
# )
# def update_graph(n_clicks):
#
#         return new_elements