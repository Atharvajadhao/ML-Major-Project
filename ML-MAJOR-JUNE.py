import streamlit as st
import pickle

Model = open('ML-MAJOR-JUNE_Model_Pkl','rb')
classifier = pickle.load(Model)

st.title("Diabetes Predictor App")
st.write('''
This app predicts that a person is have Diabetes or not.
''')

st.sidebar.header("User Input Features")

st.sidebar.markdown("""
[Example CSV input file](https://github.com/Atharvajadhao/ML-MAJOR-JUNE/blob/main/diabetes_example.csv)
""")

uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
  def user_input_feature():
    Pregnancies = st.sidebar.text_input("Number of Pregnencies", "type here")
    Glucose = st.sidebar.text_input("Glucose", "type here")
    BloodPressure = st.sidebar.text_input("Blood Pressure", "type here")
    SkinThickness = st.sidebar.text_input("Skin Thickness", "type here")
    Insulin = st.sidebar.text_input("Insulin", "type here")
    BMI = st.sidebar.text_input("BMI", "type here")
    DiabetesPedigreeFunction = st.sidebar.text_input("Diabetes Pedigree Function", "type here")
    Age = st.sidebar.text_input("Age", "type here")

df = st.selectbox("Select Data",("Iris", "Wine"))
st.write(df)