import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

app = dash.Dash()

df = pd.DataFrame([[1,2,3],[1,2,3]], columns=['x','y','z'])



fig = px.scatter(
    df,
    x='x',
    y='y'
)

app.layout = html.Div([dcc.Graph(id="life-exp-vs-gdp", figure=fig)])


if __name__ == "__main__":
    app.run_server(debug=True)