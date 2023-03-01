import streamlit as st
import dill
import numpy as np

def load_model():
    with open('../app/rf.pkl','rb') as f:
        model = dill.load(f)
    return model

model = load_model()

def show_pred_page():
    st.title()