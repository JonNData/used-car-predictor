# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
# First section
row1 = dbc.Row(
        dcc.Markdown(
            """
        
            ## Insights


            """,
            className = 'mb-4'
        ),

        )

# 2nd Section
col1 = dbc.Col(
            dcc.Markdown(
                """
                Visualizing the prices on craigslist we can immediately see the odd distribution.
                 There is a pricing convention on Craigslist to either not include the price or even list it as $1
                  to get more clicks on the ad.
                   Additionally if it’s a dealership posting a listing they may include several
                 cars in one listing and omit the price or display the cheapest.  

                """
            ), 
        )

col2 = dbc.Col(
            html.Div(html.Img(src='assets/raw-price-dist.png', className= 'img-fluid'))
        )

row2 = dbc.Row([col1,col2], align = 'center')

# 3rd section
col3 = dbc.Col(
            dcc.Markdown(
                """
                After dropping NaNs which would not help predict price, trimming a 
                some of the outliers, the distribution somewhat normalizes. There’s still
                 a moderate right skew, but taking the log function turns it into a left skew 
                 so the transformation was not worth it.


                """
            ), 
        )

col4 = dbc.Col(
            html.Div(html.Img(src='assets/prices_dist.png', className= 'img-fluid'))
        )

row3 = dbc.Row([col4,col3], align = 'center', justify = 'end')

# 4th section
col5 = dbc.Col(
            dcc.Markdown(
                """
                Using early stopping with XGBoost we can find an efficient stopping point 
                with a max number of trees.  
                
                Even with a relatively low learning rate of 0.1, the mean absolute error drops 
                quickly around 35 rounds or epochs.  This helped me decide which n_estimators to play around with
                 for the final model.



                """
            ), 
        )

col6 = dbc.Col(
            html.Div(html.Img(src='assets/xgboost_iters.png', className= 'img-fluid'))
        )

row4 = dbc.Row([col5,col6], align = 'center')

# 5th section
col7 = dbc.Col( 
            html.Div(html.Img(src='assets/PDP_year.png', className= 'img-fluid'))
        )

col8 = dbc.Col(
            html.Div(html.Img(src='assets/eli5_feature_import.jpg', className= 'ml-5')), align = 'end'
        )

row5 = dbc.Row([col7,col8])

# 6th section
col9 = dbc.Col(
            dcc.Markdown(
                """
                A partial dependence plot of the price vs the year reflects the kind of cars 
                people put on sale on craigslist. There aren’t many cars for sale older than 
                20 years. But there are some vintage cars that are highly priced for their 
                collectability. This makes creating a model particularly challenging. 


                """
            ), 
        )

col10 = dbc.Col(
                dcc.Markdown(
                """
                Using the eli5 library we can find the permutation importances. 
                These were the variables that have the greatest effect on the model’s
                 performance metrics. 


                """
            ),
            
        )

row6 = dbc.Row([col9,col10])

# 7th section
row7 = dbc.Row(
    [
            html.Div(html.Img(src= 'assets/Shapley.jpg', className = 'img-fluid')),

            dcc.Markdown(
                """
                Shapley plots allow us to explain tree ensembles  by each feauture.
                 In this observation the particular model of the car was highly valued,
                  pushing the price higher than the base value (average price).

                  """
            )
            ]        )
layout = dbc.Col([row1, row2, row3, row4, row5, row6, row7])