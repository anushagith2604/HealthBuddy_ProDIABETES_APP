# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 03:14:01 2024

@author: Preshani
"""

import numpy as np
import pickle 
import streamlit as st

#loading 
loaded_model = pickle.load(open('C:/Users/Preshani/Desktop/deploy/trained_model.sav','rb'))

#creating a function
def diabetes_prediction(input_data):
   

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)


    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The patient is not diabetic'
    else:
      return'The patient is diabetic'


def main():
    
    st.title('A1C Pathology Test Prediction')
    
    #getting input 
    
    Pregnancies = st.text_input('Number Of pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure= st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin= st.text_input('Insulin value')
    BMI = st.text_input('BMI index')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree function value')
    Age = st.text_input('Age of Patient')
    
    #code
    diagnosis= ''
    #creating
    if st.button('A1c test RESULT'):
        diagnosis= diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    st.success(diagnosis)
   
   if__name__=='__main__'
   main()
        
        
        
        
        
    
    
    
