# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
import dash_daq as daq


# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

# Load pipeline
pipeline = load('notebooks/rfsmall_pipeline.joblib')


column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Fill out the car specifications

            """
        ),
         html.Div(children='Odometer', style={
        'textAlign': 'left'
    }),
        dcc.Input(
                id='input1',
                placeholder='Enter a value...',
                type='number',
                value='20000'
) 
    ],
    md=4,
)

column2 = dbc.Col(
    [   
        html.H2("Output"),
        daq.LEDDisplay(
                    id='my-daq-leddisplay',
                    value="10000",
                    className= 'mt-5'
                    )  

    ]
)

layout = dbc.Row([column1, column2])

@app.callback(
    Output(component_id='my-daq-leddisplay', component_property='value'),
    [Input(component_id='input1', component_property='value')]
)
def update_output_div(input_value):
    return input_value