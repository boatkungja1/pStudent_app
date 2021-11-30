import streamlit as st
import pandas as pd

st.write("""
# Student Performence Project :
""")

st.sidebar.header('User Input')
st.sidebar.subheader('Please enter your data:')

# v_Sex = st.sidebar.radio('Sex', ['Male','Female','Infant'])
v_MAINGROUP1 = st.sidebar.slider('MAINGROUP', min_value=0.0, max_value=1.0, value = 0.2)
v_MAINGROUP2 = st.sidebar.slider('MAINGROUP', min_value=0.0, max_value=1.0, value = 0.7)
v_MAINGROUP3 = st.sidebar.slider('MAINGROUP', min_value=0.0, max_value=1.0, value = 0.05)
v_MAINGROUP4 = st.sidebar.slider('MAINGROUP', min_value=0.0, max_value=2.0, value = 1.0)

# Change the value of sex to be {'M','F','I'} as stored in the trained dataset


# Store user input data in a dictionary
data = {
    'Maingroup': v_MAINGROUP1,
    'Maingroup' : v_MAINGROUP2,
    'Maingroup' : v_MAINGROUP3,
    'Maingroup' : v_MAINGROUP4,
}



df = pd.DataFrame(data, index=[0])

# st.header('Application of Abalone\'s Age Prediction:')
# st.subheader('User Input:')
# st.write(df)




data_sample = pd.read_csv('Datasample.csv')
df = pd.concat([df, data_sample],axis=1)
st.write(df)

cat_data = pd.get_dummies(df[['MAINGROUP_หมวดวิชาปรับพื้นฐาน']])
st.write(cat_data)


X_new = pd.concat([cat_data, df], axis=1)
X_new = X_new[:1] 

X_new = X_new.drop(columns=['MAINGROUP_หมวดวิชาปรับพื้นฐาน'])
st.subheader('Pre-Processed Input:')
st.write(X_new)

import pickle
load_nor = pickle.load(open('nms.pkl', 'rb'))

# X_new = load_nor.transform(X_new)

# st.subheader('Normalized Input:')
# st.write(X_new)


# load_knn = pickle.load(open('best_knn.pkl', 'rb'))
# prediction = load_knn.predict(X_new)

# st.subheader('Prediction:')
# st.write(prediction)

