import pandas as pd
import warnings
import numpy as np
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')
import streamlit as st
import joblib

data = pd.read_csv('Heart Attack Data Set.csv')
model = joblib.load('heartdisease_model.pkl')


st.markdown("<h1 style = 'color: #FEFDFD; text-align: center; font-family: helvetica'>Heart Disease PREDICTOR</h1>", unsafe_allow_html = True)
st.markdown("<h4 style = 'margin: -30px; color: #2E86C1; text-align: center; font-family: cursive '>Project By Raphael IK Madugu </h4>", unsafe_allow_html = True)
st.markdown("<br>", unsafe_allow_html= True)

st.image('pngwing.com (8).png')

st.markdown("<h4 style = 'margin: -30px; color: #5DADE2 ; text-align: center; font-family: helvetica '>Project Overview</h4>", unsafe_allow_html = True)

st.write("The goal of this project is to thoroughly analyze the factors contributing to heart disease, forecasting potential outcomes associated with the condition and further use the prediction to advise patients.")

st.markdown("<br>", unsafe_allow_html= True)
st.dataframe(data, use_container_width= True)


st.sidebar.subheader('MY STORY')
st.sidebar.divider()
st.sidebar.image('raphie 2.jpg', caption = ' Raphael Madugu is a multifaceted individual blending his entrepreneurial acumen with a passion for data science. As a businessman, I demonstrated a keen sense of market trends and an ability to capitalize on emerging opportunities, driving growth and innovation within my space. Alongside my business pursuits, Raphael is also dedicated to advancing his knowledge in data science, pursuing a degree in the field. The unique combination of business insight and analytical skills will positions me as a valuable asset, leveraging data-driven strategies for success in both business entrepreneurial endeavors and career pursuits.')




col1, col2, col3, col4 = st.columns(4)
with col1:
  ag = col1.number_input('age')
  sex = col1.number_input('sex')
  cp = col1.number_input('chestpain')
  trestbps = col1.number_input('resting_blood_sugar')
  chol = col1.number_input('serum_cholesterol')
with col2 :
  fbs = col2.number_input('fasting_blood_suger')
  restecg = col2.number_input('resting_electrocardiogram_results')
  thalach = col2.number_input('thalach')
  exang = col2.number_input('excercise_induced_angina')
with col3 :
  op = col3.number_input('oldpeak')
  slope = col3.number_input('slope')
  ca = col3.number_input('number_of_vessels')
  thal =col3.number_input('thal')
with col4 :
  col4.image('pngwing.com (5).png', caption = ' Hi! Its Amazing to have you here')


st.markdown("<br>", unsafe_allow_html= True)
st.markdown("<br>", unsafe_allow_html= True)
st.markdown("<br>", unsafe_allow_html= True)

st.markdown("<h4 style = 'margin: -30px; color: #5DADE2 ; text-align: center; font-family: helvetica '>Input Variable</h4>", unsafe_allow_html = True)

inputs = pd.DataFrame()
inputs['age'] = [ag]
inputs['sex'] = [sex]
inputs['chestpain'] = [cp]
inputs['resting_blood_sugar'] = [trestbps]
inputs['serum_cholesterol'] = [chol]
inputs['fasting_blood_suger'] = [fbs]
inputs['resting_electrocardiogram_results'] = [restecg]
inputs['thalach'] = [thalach]
inputs['excercise_induced_angina'] = [exang]
inputs['oldpeak'] = [op]
inputs['slope'] = [slope]
inputs['number_of_vessels'] = [ca]
inputs['thal'] = [thal]


st.dataframe(inputs, use_container_width = True)

Prediction_button = st.button('Predict heart ')
if Prediction_button:
  predicted = model.predict(inputs)

  if predicted[0] == 0:
    st.success(f'You are free of any heart disease')
  else:
    st.error(f'Please consult your cardiologist')
  