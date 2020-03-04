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
        
          html.Div(children='Year', style={
        'textAlign': 'center'}),


        dcc.Input(
                id='input_year',
                placeholder='Enter a year...',
                type='number',
                value='1999',
                className = 'mb-4',
                ),

        html.Div(children='Manufacturer', style={
        'textAlign': 'center'}),

         dcc.Dropdown(
            id='input_manufacturer', 
            options= [
                {'label': 'Acura', 'value': 'acura'},
                {'label': 'Alfa-Romeo', 'value': 'alfa-romeo'},
                {'label': 'Aston-Martin ', 'value': 'aston-martin'},
                {'label': 'Audi', 'value': 'audi'},
                {'label': 'Bmw', 'value': 'bmw'},
                {'label': 'Buick ', 'value': 'buick'},
                {'label': 'Cadillac ', 'value': 'cadillac'},
                {'label': 'Chevrolet ', 'value': 'chevrolet'},
                {'label': 'Chrysler', 'value': 'chrysler'},
                {'label': 'Datsun ', 'value': 'datsun'},
                {'label': 'Dodge ', 'value': 'dodge'},
                {'label': 'Ferrari ', 'value': 'ferrari'},
                {'label': 'Fiat', 'value': 'fiat'},
                {'label': 'Ford ', 'value': 'ford'},
                {'label': 'Gmc ', 'value': 'gmc'},
                {'label': 'Harley-Davidson ', 'value': 'harley-davidson'},
                {'label': 'Hennessey', 'value': 'hennessey'},                
                {'label': 'Honda ', 'value': 'honda'},
                {'label': 'Hyundai ', 'value': 'hyundai'},
                {'label': 'Infiniti ', 'value': 'infiniti'},
                {'label': 'Jaguar ', 'value': 'jaguar'},
                {'label': 'Jeep ', 'value': 'jeep'},
                {'label': 'Kia', 'value': 'kia'},
                {'label': 'Land Rover ', 'value': 'land rover'},
                {'label': 'Lexus ', 'value': 'lexus'},
                {'label': 'Lincoln ', 'value': 'lincoln'},
                {'label': 'Mazda', 'value': 'mazda'},
                {'label': 'Mercedes-Benz', 'value': 'mercedes-benz'},
                {'label': 'Mercury', 'value': 'mercury'},
                {'label': 'Mini ', 'value': 'mini'},
                {'label': 'Mitsubishi', 'value': 'mitsubishi'},
                {'label': 'Morgan ', 'value': 'morgan'},
                {'label': 'Nissan ', 'value': 'nissan'},
                {'label': 'Pontiac ', 'value': 'pontiac'},
                {'label': 'Porche', 'value': 'porche'},
                {'label': 'Ram ', 'value': 'ram'},
                {'label': 'Rover ', 'value': 'rover'},
                {'label': 'Saturn ', 'value': 'saturn'},
                {'label': 'Subaru', 'value': 'subaru'},
                {'label': 'Tesla ', 'value': 'tesla'},
                {'label': 'Toyota ', 'value': 'toyota'},
                {'label': 'Volkswagen ', 'value': 'volkswagen'},
                {'label': 'Volvo', 'value': 'volvo'},
                {'label': 'Other', 'value': 'nan'}
            ],
            className = 'mb-3',
            value=1
        ),

         html.Div(children='Odometer', style={
        'textAlign': 'center'
    }),
        dcc.Input(
                id='input_odometer',
                placeholder='Enter a value in miles...',
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
    [Input(component_id='input_odometer', component_property='value')]
)
def update_output_div(input_value):
    return input_value