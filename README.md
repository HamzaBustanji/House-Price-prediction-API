<img src="https://github.com/HamzaBustanji/House-Price-prediction-App/blob/main/images/header.jpg"  width='60%' height='60%' align="middle">

# House-Price-prediction-App

## 1.Data
The Data was provided in this [Kaggle compitition](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data). 
> The Ames Housing dataset was compiled by Dean De Cock for use in data science education. It's an incredible alternative for data scientists looking for a modernized and expanded version of the often cited Boston Housing dataset.
 
## 2.Approach
The goal of this project is to build an app that can predict house prices from the Ames housing dataset. The app is meant for a more practical
access to the predictive model that we will develop. To acomplish this we will pick only the essential number of features that are necessary to 
build the model, this will be an act of balancing accessibility and accuracy. 

## 3.Data Wrangling
[**The completed notebook is availabe here**](https://github.com/HamzaBustanji/House-Price-prediction-App/blob/3595385762c4b5d61b3ea2d1a47207ce9a6e8d98/notebooks/1-data-wrangling.ipynb)
### Exploring the data
In this notebook we started by exploring our dataset. We displayed the Dataframe and explored the data types of each column. Then we consulted the data descriptions to get a better understanding of each feature and what it stands for, and we displayed a brief description of each feature. 
### Exploring missing values
Next, we explored the missing values in our data, and the five columns with the most missing values were as follows: 
<img src="https://github.com/HamzaBustanji/House-Price-prediction-App/blob/main/images/Screen%20Shot%202023-03-07%20at%2010.58.49%20AM.png"  width='60%' height='60%' align="middle">

Then, we displayed the number of unique values per column. This gave us insight into the categorical features we were dealing with. 
After displaying the unique values per column,  we began to deal with the missing values in our data. For a full view of our methodology in dealing with missing data, please refer to the completed notebook.
## 4.Exploratory Data Analysis
[**The completed notebook is availabe here**](https://github.com/HamzaBustanji/House-Price-prediction-App/blob/main/notebooks/2-exploratory-data-analysis.ipynb)
### Target feature
Our target feature is the sale price of each house, we explored its distribution and examined it for outliers.
### Categorical features 
We used a for loop to produce a bar plot for each of our categorical features, which helped us detect features that lacked variation and therefore provided little information for our goal of predicting the house price.
### Numeric features
For our numeric features, we produced summary statistics, histogram plots, and most importantly a heatmap that displayed the correlation between the features:

<img src="https://github.com/HamzaBustanji/House-Price-prediction-App/blob/main/images/Screen%20Shot%202023-03-07%20at%2011.18.07%20AM.png"  width='60%' height='60%' align="middle">

### Fianl DataFrame

We explored relationships between feature and engineered new features that might be helpful. But, in the end the combination of features that we arrived at is the following: 

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

## Preprocessing and modeling
[**The completed notebook is availabe here**](https://github.com/HamzaBustanji/House-Price-prediction-App/blob/main/notebooks/3-pre-processing-and-4-modeling.ipynb)
### Preprocessing
In the preprocessing step, we loaded our data, created a train/test split, and scaled the predictive features using a standard scaler. The scaler was fit on the training set to avoid data leakage. We also saved the same scaler to be used in our app.
### Modeling
#### Linear models
We trained three linear models; a Linear Regression model, a Polynomial model, and an Elastic Net model. Of which only the Elastic Net model performed relatively well.
#### Support Vector Regression 
The Support Vector Regression model performed similarly to the Elastic Net model. 
#### Random Forrest Regression
The best performing model was the Random Forrest model. Based on our evaluation metrics, we chose to move forward with it. 
#### Evaluation Metrics
<img src="https://github.com/HamzaBustanji/House-Price-prediction-App/blob/main/images/model%20scores.png"  width='60%' height='60%' align="middle">

## 6.App
[The code and all related files to tha app are available here](https://github.com/HamzaBustanji/House-Price-prediction-App/tree/main/app)
We developed the app using the Streamlit open source python framework. Streamlit allowed us to create the app and deploy it online for free. 
