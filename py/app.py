import dash
import dash_core_components as dcc
import dash_html_components as html
import flask
from sqlalchemy import create_engine
import pandas as pd
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

mysql_conn_str = "mysql+pymysql://pc2project:password@mysql/pc2project"
engine = create_engine(mysql_conn_str)
df = pd.read_sql_table("runningdata", engine)

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server,external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True

fig = px.histogram(df, x="Average Heart Rate (bpm)", title='Average Heart Rate (bpm) Count')
fig2 = px.box(df, x="Average Speed (km/h)", title='Average of Average Speed (km/h)', points="all")
fig3 = px.scatter(df, y="Calories Burned", x="Distance (km)", color="Type", title='Calories Burned by Distance Traveled')

app.layout = html.Div(children=[
    html.H1('Dash web app - PC2 Project'),

    html.Div(children='''
        Dash App presentado por Manuel Cabrera, Carla Duran, Miguel Lombardi
    '''),

    dcc.Graph(
        id='graph-one',
        figure=fig
    ),
    dcc.Graph(
        id='graph-two',
        figure=fig2
    ),
    dcc.Graph(
        id='graph-three',
        figure=fig3
    )
])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0',debug=True, port=8050)