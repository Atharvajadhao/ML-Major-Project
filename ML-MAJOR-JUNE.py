import streamlit as st
import pickle
import pandas as pd
import numpy as np

Model = open('ML-MAJOR-JUNE_Model_Pkl','rb')
classifier = pickle.load(Model)

st.title("Diabetes Predictor App")
st.write('''
This app predicts that a person is have Diabetes or not.
''')
st.write('''
Please enter the require information in given text box.
''')
st.write('''
**And please do not leave any text box blank.**
''')
st.write('''
**Note:-** The Machine Learning model is trained by diabetes.csv data set and the model has the **accuracy of 82%.** We can't assure that the prediction will always be perfect. Please take doctor's advice before believing on the ML model.
''')
st.write('''
The model is mainly made for **Female patients**.
''')
st.write('''
Click here to access data set [link](https://github.com/Atharvajadhao/ML-MAJOR-JUNE/blob/main/data/diabetes.csv).
''')

st.header("User Input Features")

def user_input_feature():
    Pregnancies = st.text_input("Number of Pregnencies")
    Glucose = st.text_input("Glucose")
    BloodPressure = st.text_input("Blood Pressure")
    SkinThickness = st.text_input("Skin Thickness")
    Insulin = st.text_input("Insulin")
    BMI = st.text_input("BMI")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function")
    Age = st.text_input("Age")
    data = {
        'Pregnancies':Pregnancies,
        'Glucose':Glucose,
        'BloodPressure':BloodPressure,
        'SkinThickness':SkinThickness,
        'Insulin':Insulin,
        'BMI':BMI,
        'DiabetesPedigreeFunction':DiabetesPedigreeFunction,
        'Age':Age
    }
    features = pd.DataFrame(data, index=[0])
    return features
input_df = user_input_feature()

if st.button("Predict"):
    result = classifier.predict(input_df)
    if result == 0:
        st.write('# This person does not have Diabetes')
    elif result == 1:
        st.write('# This person have Diabetes')
