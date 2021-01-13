from jupyter_dash import JupyterDash
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__)

app.layout = html.Div([

    html.Label('Multi-Select Dropdown'),

    dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': u'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
        ],
    value= ['MTL','SF'],
    multi = True ),

    html.Label('Radio Items'),
	
    dcc.RadioItems(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': u'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
        ],
    value='MTL'),

    html.Label('Checkboxes'),

    dcc.Checklist(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
            ],
        values=['MTL', 'SF']),

    html.Label('Text Box'),

    dcc.Input(value='MTL', type='text')
])

if __name__ == '__main__':
    app.run_server()
