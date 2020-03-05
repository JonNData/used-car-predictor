# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## What's that car worth?
           """,
           className= 'mb-5'
        ),
        dcc.Markdown(
            """
            Interested in knowing the price people are actually selling their car for?
            Use this app to predict selling prices based on actual craigslist ads!


            """
        ),
        dcc.Link(dbc.Button('Find that price', color='primary'), href='/predictions')
    ],
    md=5,
)



column2 = dbc.Col(
    [
        html.Div(
            html.Img(src='assets/bmw-example.jpg')
        )
    ],
     md=5,
)

layout = dbc.Row([column1, column2])