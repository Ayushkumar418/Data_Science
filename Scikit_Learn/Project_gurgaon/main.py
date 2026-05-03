import os
import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit, cross_val_score
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error

MODEL_FILE = "model.pkl"
PIPELINE_FILE = "pipeline.pkl"

def build_pipeline(num_attribs, cat_attribs):
    # For numercial attributes
    num_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    # For Categorical attributes
    cat_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy=("most_frequent"))),
        ("one_hot_encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    # Contruct the full Pipeline 
    full_pipeline = ColumnTransformer([
        ("num", num_pipeline, num_attribs),
        ("cat", cat_pipeline, cat_attribs)
    ])
    
    return full_pipeline

if not os.path.exists(MODEL_FILE) or not os.path.exists(PIPELINE_FILE):
    # lets Trian the model
    
    # 1. Load the dataset
    housing = pd.read_csv("housing.csv")

    # 2. Create a statified test set
    housing["income_cat"] = pd.cut(housing["median_income"],
                                bins = [0, 1.5, 3.0, 4.5, 6.0, np.inf],
                                labels = [1, 2, 3, 4, 5])

    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

    for train_index, test_index in split.split(housing, housing["income_cat"]):
        housing.loc[test_index].drop("income_cat", axis = 1).to_csv("input.csv", index = False)
        housing = housing.loc[train_index].drop("income_cat", axis=1)
        
    # 3. Separate the labels from the features
    housing_labels = housing["median_house_value"].copy()
    housing_features = housing.drop("median_house_value", axis = 1)
    
    # 4. List the numerical and categorical columns
    num_attribs = housing_features.select_dtypes(include=[np.number]).columns.tolist()
    cat_attribs = ["ocean_proximity"]
    
    Pipeline = build_pipeline(num_attribs, cat_attribs)
    housing_prepared = Pipeline.fit_transform(housing_features)
    # print(housing_prepared)
    # print(housing_prepared.shape)
    
    model = RandomForestRegressor()
    model.fit(housing_prepared, housing_labels)
    
    joblib.dump(model, MODEL_FILE)
    joblib.dump(Pipeline, PIPELINE_FILE)
    print("Model and Pipeline saved successfully.")
else:
    print("Model already exists. Loading the model and pipeline.")
    # lets do inference 
    model = joblib.load(MODEL_FILE)
    Pipeline = joblib.load(PIPELINE_FILE)
    
    input_data = pd.read_csv("input.csv")
    transformed_data = Pipeline.transform(input_data)
    predictions = model.predict(transformed_data)
    input_data["Predicted_House_Value"] = predictions
    input_data.to_csv("output.csv", index=False)
    print("Inference completed. Predictions saved to output.csv.")
    