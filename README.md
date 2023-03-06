<img src="https://github.com/HamzaBustanji/House-Price-prediction-App/blob/main/header.jpg"  width='60%' height='60%' align="middle">

# House-Price-prediction-App

## 1.Data
The Data was provided in this [Kaggle compitition](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data). 
> The Ames Housing dataset was compiled by Dean De Cock for use in data science education. It's an incredible alternative for data scientists looking for a modernized and expanded version of the often cited Boston Housing dataset.
 
## 2.Approach
The goal of this project is to build an app that can predict house prices from the Ames housing dataset. The app is meant for a more practical
access to the predictive model that we will develop. To acomplish this we will pick only the essential number of features that are necessary to 
build the model, this will be an act of balancing accessibility and accuracy. 

## 3.Data Wrangling:




The combination of features that we arrived at is the following: 
| Feature | Description |
| --- | ----------- |
| SalePrice | the property's sale price in dollars. This is the target variable that you're trying to predict. |
| Neighborhood | Physical locations within Ames city limits |
| YearBuilt | Original construction date |
| Fireplaces | Number of fireplaces |
| Condition | Overall condition rating |
| HouseStyle | Style of dwelling |
| BuildingType | Type of dwelling |
| HalfBath | Half baths above grade |
| FullBath | Full bathrooms above grade |
| Bedrooms | Number of bedrooms above basement level |
| HouseArea | The area of the inside of the house |
| LotArea | Lot size in square feet |
| GarageCars | Size of garage in car capacity |
| MasVnrArea | Masonry veneer area in square feet |
| Exterior1st | Exterior covering on house |
| YearRemodAdd | Remodel date |

The way we arrived at these features is by picking the ones that showed the most potential in predicting the sale price. Although a 

