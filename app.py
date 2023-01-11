import streamlit as st
import datetime
import numpy as np
import pandas as pd
import string
import pickle
from sklearn.preprocessing import StandardScaler
import haversine as hs
import countries

st.set_page_config(layout="wide")

uber_model=pickle.load((open('finalized_model.sav','rb')))
scaler_model=pickle.load((open('Scaler.pkl','rb')))


def fare(inputs):
    scaled = scaler_model.transform(np.array([inputs]).reshape(1, -1))
    input_data_reshaped = scaled.reshape(1, -1)
    prediction = uber_model.predict(input_data_reshaped)
    return prediction



def main():
        st.header('**UBER fare** prediction app.')
        st.sidebar.text('THIS WEB COMPUTES THE TRAVEL FARE ')
        st.sidebar.text('-> Enter the LOCATION ,DESTINATION CO-ORDINATES and NUMBER \n\tOF PEOPLE  and find the fare ')

        # Location Details

        Country = st.selectbox(
            'Select the Country',
            countries.l, index=0, label_visibility="visible")
        Street = st.text_input('Present Street:')
        District = st.text_input('Present District:')
        state = st.text_input('Present State:')
        address1, lat1, lon1 = countries.location(Street, District, state, Country)

        st.write(f'Current loc \t\t\t{address1}')

        # Destination Details

        Street1 = st.text_input('Destination Street:')
        District1 = st.text_input('Destination District:')
        state1 = st.text_input('Destination State:')
        address2, lat2, lon2 = countries.location(Street1, District1, state1, Country)

        st.write(f'Desination loc\t\t\t\ {address2}')

        current_time = datetime.datetime.now()
        passenger_count = st.slider('Input no of passengers', 1, 8)

        loc1=(lat1, lon1)
        loc2 =(lat2, lon2)






        if st.button('Compute Fare'):
                pred=fare([[lon1,lat1,lon2,lat2,current_time.hour,current_time.year,current_time.month]])
                if(passenger_count==1):
                       st.write(f'The total fare for {passenger_count} person is $',str(np.round(pred * 1,2)))
                       st.write('\nDistance :',str(round(hs.haversine(loc1,loc2))),'km')
                       st.write('Total duration of travel will be approx',str(np.round(hs.haversine(loc1, loc2) / 50)),'hrs')
                else:
                    st.write(f'The total fare for {passenger_count} people is $', str(np.round(pred * passenger_count, 2)))
                    st.write('\nDistance :',str(round(hs.haversine(loc1,loc2))),'km')
                    st.write('Total duration of travel will be approx',str(np.round(hs.haversine(loc1,loc2)/50)),'hrs')

if __name__=="__main__":
    main()




