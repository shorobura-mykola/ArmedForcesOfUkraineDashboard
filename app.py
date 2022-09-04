import os
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

df = pd.read_csv('ukr_stats.csv')
fig = px.bar(df, x="Month", y="Quantity", text_auto="")
fig.update_layout(legend=go.layout.Legend(x=1, y=1, traceorder='normal', font=dict(family='Verdana', size=22, color='black')))
fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)


app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])
app.title = 'Шо по русні?!'.upper()
app.layout = html.Div([
  dbc.Row([
    html.H3("Графік кількісті \"хороших\" рускіх.".upper(),
            style={
              'text-align': 'center',
              'marginTop': 15
            })
  ]),
  dcc.Graph(id="graph", figure=fig),
  dbc.Row([
    html.H3("Наша русофобія недостатня!".upper(),
            style={
              'text-align': 'center',
              'marginTop': 15
            })
  ]),
])


if __name__ == '__main__':
  server_port = os.environ.get('PORT', '8080')
  app.run(debug=False, port=server_port, host='0.0.0.0')