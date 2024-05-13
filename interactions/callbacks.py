from dash import Input, Output, callback


@callback(Output('cytoscape-tapNodeData-output', 'children'),
          Input('cytoscape-two-nodes', 'tapNodeData'))
def display_tap_node_data(data):
    if data:
        return "Node: " + data['label']


@callback(
    Output("switches-output", "children"),
    [
        Input("switches-input", "value"),
    ],
)
def on_form_change(switches_value):
    template = "switch{} selected."

    n_switches = len(switches_value)

    output_string = template.format(
        n_switches,
        "es" if n_switches != 1 else "",
    )
    return output_string
