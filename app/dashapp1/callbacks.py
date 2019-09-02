from datetime import datetime as dt
from dash.dependencies import Input, Output
import pandas_datareader as pdr

# register callbacks will update the output which is the graph interactively based on the input of the the dropdown.
# Essentially,it will update the graph on update of choice of the value from the dropdown.

def register_callbacks(dashapp):
    """
    This function takes the Plotly dash application as input and returns the callback of the updation as output.
    
    """
    # It is the standard callback 
    @dashapp.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
    def update_graph(selected_dropdown_value):
        df = pdr.get_data_yahoo(selected_dropdown_value, start=dt(2017, 1, 1), end=dt.now())
        return {
            'data': [{
                'x': df.index,
                'y': df.Close
            }],
            'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
        }
