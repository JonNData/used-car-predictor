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

            For metrics, I chose R^2 for variance explainability and MAE for simple error comparison.

            I started with a mean baseline of 8613.48 MAE or  a 7829.12 MAE of the simplest linear regression based on ‘year’. Quickly beat these scores with a 
            decision tree:  

            MAE: 4046.073483860394  
            R^2: 0.662591542690196

            And eventually tuned a Random Forest Regression:  

            MAE: 2239.446412036939  
            R^2: 0.8332063700252051

            And an Gradient Boost Regression, tuned for early stopping with 200 trees with max_depth = 35:  

            MAE: 2034.08  
            R^2: 0.8427885081293791

            This was all great, provided decent metrics, but then it was time to pickle the model. Pickling the model 
            would allow us to save it as an object and use it in an online-hosted app. 
            Pickle.dump lead to a staggering **1.86GB** file. Thankfully there was a compression technique from joblib.dump. 
            727MB, nowhere near the 100MB git CLI push limit. Furthermore, Heroku only has a 500MB ram allowance 
            so it wouldn’t be wise to utilize such a big file even if I could get it over there. 

            
            #### The lesson: Compromise!
            Immediately, I could see that I could downgrade to a *random forest* model without losing much predictive power.
             Tweaking max depth and trimming the number of trees significantly lead to a substantial size decrease: 236 MB.
            Much warmer but now we’ve dropped to evaluation metrics of:

            MAE: 3740.12  
            R^2: 0.7143381

            Further tweaking and realizing that inputs into our model must be user friendly, 
            I had to drop the majority of my features, including the ‘model’ of the car for feasibility. 
            I settled on a random forest model with  n_estimators = 35 and max_depth = 18, with 5 features. 57MB.

            MAE: 2886.2397449386103  
            R^2: 0.7651232850307356

            A big lesson learned here was that although you may use all your resources and time to get the model with the
             best evaluation metrics, in practice you'll have to consider practicality--and that means taking tradeoffs.


            #### Limitations: The model is mostly useful for a quick price estimation on used cars.
             Getting a specific model or sale price can be done on the larger original used cars dataset scraped from craigslist.

             #### Looking ahead: Going forward, this model could be improved by including the model of the car as a feature.
               That would ideally entail a dropdown menu dependent upon the manufacturer selected. 
               Also, a more elegant solving of the filesize issue would leave space for a more thorough model. 
               A primary objective would be dealing with the tough distribution of prices near the lower end.
            """

        )

    ]
)

layout = dbc.Col([row1, row2])