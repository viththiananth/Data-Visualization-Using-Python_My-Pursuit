import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

from dash.dependencies import Input, Output

app = dash.Dash()
df = pd.read_csv('finance-charts-apple.csv')

# Step 3. Create a plotly figure
fig = px.scatter(df, x="Date", y="AAPL.High",title="Apple stock prices")

features = df.columns[1:-1]
print(features)

opts = [{'label' : i, 'value' : i} for i in features]
print(opts)

# Step 4. Create a Dash layout
app.layout = html.Div([

# adding a header and a paragraph
    html.Div([
        html.H1("This is my first dashboard"),
        html.P("Learning Dash is so interesting!!")],
        style = {'padding' : '50px', 'backgroundColor' : '#3aaab2'}),

    dcc.Graph(id = 'plot', figure = fig),

#lets add the dropdown now
    html.Label("Choose a feature"),

    dcc.Dropdown(id = 'opt',
                 options = opts,
                 value = 'AAPL.High')
])


@app.callback(
    Output('plot', 'figure'),
    [Input('opt', 'value')])


def update_figure(X):
    fig = px.scatter(df, x=df['Date'], y = df[X], title="AAPL HIGH")
    return fig

if __name__ == '__main__':
    app.run_server(debug = True)