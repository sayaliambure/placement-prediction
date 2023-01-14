import streamlit as st
import pickle
import sklearn


model = pickle.load(open('model.pkl', 'rb'))

st.title("placement prediction")

cgpa = st.number_input('Insert cgpa')
iq = st.number_input('Insert iq')


if st.button('Predict'):
    result = model.predict([[cgpa, iq]])[0]
        
    if result == 1:
        st.header("Yes")
    else:
        st.header("No")




