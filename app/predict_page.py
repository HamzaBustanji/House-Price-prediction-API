import streamlit as st
import dill
import numpy as np


def load_model():
    with open('../app/rf.pkl', 'rb') as f:
        model = dill.load(f)
    return model


model = load_model()


def show_pred_page():
    st.title('House Price Prediction for the Ames Housing Dataset')

Neighborhoods = (
    'Blmngtn',
    'Blueste',	
    'BrDale'	,
    'BrkSide',	
    'ClearCr',	
    'CollgCr',	 
    'Crawfor',	
    'Edwards',	
    'Gilbert',	
    'IDOTRR',
    'MeadowV',	
    'Mitchel',	
    'Names',
    'NoRidge',	
    'NPkVill',	
    'NridgHt',	
    'NWAmes',
    'OldTown',	
    'SWISU',
    'Sawyer',
    'SawyerW',	 
    'Somerst',	
    'StoneBr',	 
    'Timber',
    'Veenker'
)
Conditions = (
    'Average',      
    'Above Average',     
    'Good',              
    'Very Good',         
    'Below Average',     
    'Excellent',          
    'Fair',               
    'Very Excellent ',    
    'Poor',                
    'very poor',           
)

HouseStyles = (
    'One story',               
    'Two story',               
    'One and a half story',
    'Split Level',              
    'Split Foyer',              
    'Two and a half story',
    )

BuildingTypes = (
    'Single-family',    
    'Townhouse',         
    'Duplex',             
    'Two-family'
    )

Exterior1stValues = (
    'VinylSd',    
    'HdBoard',   
    'MetalSd',    
    'Wd Sdng',   
    'Plywood',    
    'CemntBd',     
    'BrkFace',     
    'WdShing',     
    'Stucco',      
    'AsbShng',
    'BrkComm',      
    'Stone',        
    'AsphShn',      
    'ImStucc',      
    'CBlock'
    )

YearBuilt = st.number_input('What year was the house built?')
Neighborhood = st.selectbox('Which neighborhood is the house in?',Neighborhoods)
GarageCars = st.slider('How many cars fit in the garage?', 0, 6, 2)
Fireplace = st.slider('How many fireplaces does the house have?', 0, 3, 1)
Condition = st.selectbox('What is the condition of the house?',Conditions)
HouseStyle = st.selectbox('What is the house style?',HouseStyles)
BuildingType = st.selectbox('What is the building type?',BuildingTypes)
HalfBath = st.number_input('How many half-bathrooms are in the house?')
FullBath = st.number_input('How many full-bathrooms are in the house?')
Bedrooms = st.number_input('How many bedrooms are in the house?')
HouseArea = st.number_input('What is the house area in square feet?')
LotArea = st.number_input('What is the lot area in square feet?')
MasVnrArea = st.number_input('What is the masonry veneer area in square feet')
Exterior1st = st.selectbox('What is the exterior covering the house?',Exterior1stValues)
ok = st.button('Calculate House Price')

 