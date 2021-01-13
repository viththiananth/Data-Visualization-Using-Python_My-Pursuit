import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.DataFrame({
"Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
"Amount": [4, 1, 2, 2, 4, 5],
"City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
	html.H1('Hello Dash'),

	html.Div('''
		Dash: Here comes the first layout with dash
	'''),

	dcc.Graph(
		id='example-graph',
		figure=fig
	)
])

if __name__ == '__main__':
	app.run_server(debug=True)



