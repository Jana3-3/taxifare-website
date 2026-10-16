import streamlit as st
import datetime
import requests

#'''
# TaxiFareModel front
'''
# Taxi Fare
'''

#st.markdown('''
#Remember that there are several ways to output content into your web page...

#Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
#''')

#'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

#1. Let's ask for:
#- date and time
#- pickup longitude
#- pickup latitude
#- dropoff longitude
#- dropoff latitude
#- passenger count
#'''

'Please insert:'
pickup_date = st.date_input(
                    "pickup date",
                    datetime.datetime.now())

pickup_time = st.time_input(
                    "pickup time",
                    datetime.datetime.now())

pickup_datetime = str(datetime.datetime.combine (pickup_date, pickup_time))
f'pickup datetime: {pickup_datetime}'
pickup_latitude = st.number_input('pickup latitude', value=-73.950655, format="%.6f", min_value=-74.3, max_value=-73.7)
pickup_longitude = st.number_input('pickup longitude', value=40.783282, format="%.6f", min_value=40.5, max_value=40.9)
dropoff_latitude = st.number_input('dropoff latitude', value=-73.950655, format="%.6f", min_value=-74.3, max_value=-73.7)
dropoff_longitude = st.number_input('dropoff longitude', value=40.769802, format="%.6f", min_value=40.5, max_value=40.9)
passenger_count = st.number_input('number of passengers', value=1, format="%.0f", min_value=1, max_value=20)


#'''
## Once we have these, let's call our API in order to retrieve a prediction

#See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

#🤔 How could we call our API ? Off course... The `requests` package 💡
#'''

url = 'https://taxifare.lewagon.ai/predict' #

#if url == 'https://taxifare.lewagon.ai/predict':

#    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

#'''

#2. Let's build a dictionary containing the parameters for our API...

#3. Let's call our API using the `requests` package...

#4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
#'''
X_new = dict(pickup_datetime=pickup_datetime,
             pickup_latitude=pickup_latitude,
             pickup_longitude=pickup_longitude,
             dropoff_latitude=dropoff_latitude,
             dropoff_longitude=dropoff_longitude,
             passenger_count=passenger_count)

def predict(params: dict):
    response = requests.get(url, params=params)
    fare = response.json()['fare']
    f'# Your predicted fare will be {fare:.2f} $.'

if st.button('predict'):
    predict(X_new)
