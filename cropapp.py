# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pickle
import streamlit as st
kn_classifier = pickle.load(open('C:/Users/suwin/Desktop/_Temoprary_/Tri nit/kn_classifier.pk1','rb'))

def crop_prediction(input_data):
    newdata=kn_classifier.predict([input_data])
    return newdata
def main():
    st.tilte('Crop prediction web-app')
    N = st.text_input('Nitrogen Value')
    P = st.text_input('Phosphorous Value')
    K = st.text_input('Potassium Value')
    temperature = st.text_input('Temperature')
    humidity = st.text_input('Humidity')
    ph = st.text_input('ph')
    rainfall = st.text_input('rainfall')
    
    result = ''
    if st.button('Result'):
        result = crop_prediction([N,P,K,temperature,humidity,ph,rainfall])
    st.success(result)
    
if __name__=='__main__':
    main()