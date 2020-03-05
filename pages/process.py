# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app


# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
row1 = dbc.Row(
    [
        dcc.Markdown(
            """
        
            ## Process


            """,
            className= 'mb-5'
        ),

    ],
)

row2 = dbc.Row(
    [
        dcc.Markdown(
            """
            Price was chosen as a natural target because it is information that would be most applicable to the user. Whether someone is looking to sell or buy a car, price is the bottom line.

            Started with a baseline of 8613.48 MAE of a mean baseline or  a 7829.12 MAE of the simplest linear regression based on ‘year’. Quickly beat these scores with a 
            decision tree:  

            MAE: 4046.073483860394  
            R^2: 0.662591542690196

            And eventually tuned a Random Forest Regression:  

            MAE: 2239.446412036939  
            R^2: 0.8332063700252051

            And an Gradient Boost Regression, tuned for early stopping with 200 trees with max_depth = 35:  

            MAE: 2034.08  
            R^2: 0.8427885081293791

            All great, decent metrics, but then it’s time to pickle. Using  import pickle, with open, pickle.dump lead to a 1.86GB file. Thankfully there was compression techniques from joblib import dump. 727MB, nowhere near the 100MB git CLI push limit. Furthermore, Heroku only has a 500MB ram allowance so it wouldn’t be wise to utilize such a big file even if I could get it over there. 

            The compromise: 
            Immediately, I could see that I could downgrade to a random forest model without losing much predictive power. Tweak max depth and trim the number of trees significantly: 236 MB. Much warmer but now we’ve dropped to 


            MAE: 3740.12  
            R^2: 0.7143381

            Finally, realizing that inputs into our model must be user friendly, I had to drop the majority of my features, including which ‘model’ of the car for feasibility.  

            MAE: 2886.2397449386103  
            R^2: 0.7651232850307356

            """

        )

    ]
)

layout = dbc.Col([row1, row2])