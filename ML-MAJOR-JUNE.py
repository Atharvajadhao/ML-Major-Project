import streamlit as st
import pickle

Model = open('ML-MAJOR-JUNE_Model_Pkl','rb')
classifier = pickle.load(Model)

st.title("Diabetes Predictor App")
st.write('''
This app predicts that a person is have Diabetes or not.
''')

st.sidebar.header("User Input Features")

def user_input_feature():
    Pregnancies = st.text_input("Number of Pregnencies")
    Glucose = st.text_input("Glucose")
    BloodPressure = st.text_input("Blood Pressure")
    SkinThickness = st.text_input("Skin Thickness")
    Insulin = st.text_input("Insulin")
    BMI = st.text_input("BMI")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function")
    Age = st.text_input("Age")
    features = pd.DataFrame(data, index=[0])
    return features
input_df = user_input_features()

if st.button("Predict"):
    result = classifier.predict(input_df)
    if result == 0:
        st.write('This person does not have Diabetes')
    elif result == 1:
        sty.write('This person have Diabetes')
