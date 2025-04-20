import streamlit as st

import numpy as np
import pandas as pd
import datetime
import requests

# pass count
pass_count = st.number_input('How many passenger you are?', step=1, min_value=1, max_value=40)
st.write(pass_count)

# date and time of the ride
d = str(st.date_input(
    "When's your taxi ride?",
    datetime.date(2019, 7, 6)))
st.write('Your ride is on:', d)

t = str(st.time_input('Time of your ride', datetime.time(8, 45)))
st.write("You're taking a taxi at the following time:", t)

date_and_time = d + ' ' + t

date_and_time = datetime.datetime.strptime(date_and_time, '%Y-%m-%d %H:%M:%S')

st.write(date_and_time)

#pickup latitude
pickup_latitude = st.number_input("Pickup Latitude")
st.write(pickup_latitude)
#dropoff latitude
dropoff_latitude = st.number_input("Dropoff Latitude")
st.write(dropoff_latitude)
#pick up longitude
pickup_longitude = st.number_input("pickup Longitude")
st.write(pickup_longitude)
#dropoff longitude
dropoff_longitude = st.number_input("Dropoff Longitude")
st.write(dropoff_longitude)


 #add other params expected by the API


if st.button('Predict Fare'):

    params = {'pickup_datetime' : date_and_time,
          'passenger_count': pass_count,
           'pickup_latitude':pickup_latitude,
           'dropoff_latitude':dropoff_latitude,
            'pickup_longitude':pickup_longitude,
            'dropoff_longitude':dropoff_longitude}
    response = requests.get('https://taxifare.lewagon.ai/predict', params=params)

    if response.status_code == 200:
        prediction = response.json()
        st.success(f"Estimated Fare: ${prediction['fare']:.2f}")
    else:
        st.error("Error while fetching prediction. Try again.")
