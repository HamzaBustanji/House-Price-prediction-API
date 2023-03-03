import streamlit as st
import dill
import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd
import streamlit 

st.title('House Price Prediction App for the Ames Housing Dataset')

model = dill.load(open('/hamzabustanji/house-price-prediction-api/main/app/rf.pkl', 'rb'))

scaler = dill.load(open('/hamzabustanji/house-price-prediction-api/main/app/scaler.pkl', 'rb'))



Neighborhoods = (
    'Blmngtn',
    'Blueste',	
    'BrDale',
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
Neighborhoods_wo = [
    'Blueste',	
    'BrDale',
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
]

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

Conditions_wo = [
    'Average',
    'Below Average',
    'Excellent',
    'Fair',
    'Good',
    'Poor',
    'Very Excellent',
    'Very Good',
    'very poor'
]

HouseStyles = (
    'One story',               
    'Two story',               
    'One and a half story',
    'Split Level',              
    'Split Foyer',              
    'Two and a half story',
    )
HouseStyles_wo = [
    'One story',
    'Split Foyer',
    'Split Level',
    'Two and a half story',
    'Two story',
]

BuildingTypes = (
    'Single-family',    
    'Townhouse',         
    'Duplex',             
    'Two-family'
    )
BuildingTypes_wo = [
    'Single-family',
    'Townhouse',
    'Two-family'
]

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
Exterior1stValues_wo = [
    'AsphShn',
    'BrkComm',
    'BrkFace',
    'CBlock',
    'CemntBd',
    'HdBoard',
    'ImStucc',
    'MetalSd',
    'Plywood',
    'Stone',
    'Stucco',
    'VinylSd',
    'Wd Sdng',
    'WdShing'
]

X = pd.DataFrame(columns =['YearBuilt', 'Fireplaces', 'HalfBath', 'FullBath', 'Bedrooms',
       'HouseArea', 'LotArea', 'GarageCars', 'MasVnrArea', 'YearRemodAdd',
       'Blueste', 'BrDale', 'BrkSide',
       'ClearCr', 'CollgCr', 'Crawfor',
       'Edwards', 'Gilbert', 'IDOTRR',
       'MeadowV', 'Mitchel', 'Names',
       'NPkVill', 'NWAmes', 'NoRidge',
       'NridgHt', 'OldTown', 'SWISU',
       'Sawyer', 'SawyerW', 'Somerst',
       'StoneBr', 'Timber', 'Veenker',
       'Average', 'Below Average', 'Excellent',
       'Fair', 'Good', 'Poor',
       'Very Excellent', 'Very Good','very poor',
       'One story', 'Split Foyer',
       'Split Level', 'Two and a half story',
       'Two story',
       'Single-family',
       'Townhouse', 'Two-family',
       'AsphShn', 'BrkComm', 'BrkFace',
       'CBlock', 'CemntBd', 'HdBoard',
       'ImStucc', 'MetalSd', 'Plywood',
       'Stone', 'Stucco', 'VinylSd',
       'Wd Sdng', 'WdShing'] )


YearBuilt = st.number_input('What year was the house built?')
X.loc[0,'YearBuilt'] = int(YearBuilt)

Fireplaces = st.slider('How many fireplaces does the house have?', 0, 3, 1)
X.loc[0,'Fireplaces'] = int(Fireplaces)

HalfBath = st.number_input('How many half-bathrooms are in the house?')
X.loc[0,'HalfBath'] = int(HalfBath)

FullBath = st.number_input('How many full-bathrooms are in the house?')
X.loc[0,'FullBath'] = int(FullBath)

Bedrooms = st.number_input('How many bedrooms are in the house?')
X.loc[0,'Bedrooms'] = int(Bedrooms)

HouseArea = st.number_input('What is the house area in square feet?')
X.loc[0,'HouseArea'] = int(HouseArea)

LotArea = st.number_input('What is the lot area in square feet?')
X.loc[0,'LotArea'] = int(LotArea)

GarageCars = st.slider('How many cars fit in the garage?', 0, 6, 2)
X.loc[0,'GarageCars'] = int(GarageCars)

MasVnrArea = st.number_input('What is the masonry veneer area in square feet')
X.loc[0,'MasVnrArea'] = float(MasVnrArea)

YearRemodAdd = st.number_input('What year was the house remodeled?')
X.loc[0,'YearRemodAdd'] = int(YearRemodAdd)



Neighborhood = st.selectbox('Which neighborhood is the house in?',Neighborhoods)
if (Neighborhood == 'Blmngtn'):
    X.loc[0,Neighborhoods_wo] = 0
else:
    for i in Neighborhoods_wo:
        if i == Neighborhood:
            X.loc[0,Neighborhoods_wo] = 0
            X.loc[0,i] = 1



Condition = st.selectbox('What is the condition of the house?',Conditions)
if (Condition == 'Above Average'):
    X.loc[0,Conditions_wo] = 0
else:
    for i in Conditions_wo:
        if i == Condition:
            X.loc[0,Conditions_wo] = 0
            X.loc[0,i] = 1



HouseStyle = st.selectbox('What is the house style?',HouseStyles)
if (HouseStyle == 'One and a half story'):
    X.loc[0,HouseStyles_wo] = 0
else:
    for i in HouseStyles_wo:
        if i == HouseStyle:
            X.loc[0,HouseStyles_wo] = 0
            X.loc[0,i] = 1



BuildingType = st.selectbox('What is the building type?',BuildingTypes)
if (BuildingType == 'Duplex'):
    X.loc[0,BuildingTypes_wo] = 0
else:
    for i in BuildingTypes_wo:
        if i == BuildingType:
            X.loc[0,BuildingTypes_wo] = 0
            X.loc[0,i] = 1

        

Exterior1st = st.selectbox('What is the exterior covering the house?',Exterior1stValues)
if (Exterior1st == 'AsbShng'):
    X.loc[0,Exterior1stValues_wo] = 0
else:
    for i in Exterior1stValues_wo:
        if i == Exterior1st:
            X.loc[0,Exterior1stValues_wo] = 0
            X.loc[0,i] = 1




ok = st.button('Calculate House Price')
if ok:
    X = np.array(X)
    X_scaled = scaler.transform(X)
    prediction = model.predict(X_scaled)
    st.subheader(f"The house price is predicted to be ${prediction[0]:.0f}")
