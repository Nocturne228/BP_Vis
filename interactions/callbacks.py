from dash import Input, Output, callback


@callback(Output('cytoscape-tapNodeData-output', 'children'),
              Input('cytoscape-two-nodes', 'tapNodeData'))
def display_tap_node_data(data):
    if data:
        return "You recently clicked/tapped the city: " + data['label']
