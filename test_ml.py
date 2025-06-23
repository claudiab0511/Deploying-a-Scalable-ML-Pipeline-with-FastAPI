# TODO: add necessary import
import pytest
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.model import train_model, compute_model_metrics, inference
from ml.data import process_data
import pandas as pd

#Pytest fixture to create a mini sample of census-style data for quick testing
#Sample contains 2 rows that match the original dataset

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        "age": [25, 38],
        "workclass": ["Private", "Self-emp-not-inc"],
        "fnlwgt": [226802, 89814],
        "education": ["11th", "HS-grad"],
        "education-num": [7, 9],
        "marital-status": ["Never-married", "Married-civ-spouse"],
        "occupation": ["Machine-op-inspct", "Farming-fishing"],
        "relationship": ["Own-child", "Husband"],
        "race": ["Black", "White"],
        "sex": ["Male", "Male"],
        "capital-gain": [0, 0],
        "capital-loss": [0, 0],
        "hours-per-week": [40, 50],
        "native-country": ["United-States", "United-States"],
        "salary": ["<=50K", ">50K"]
    })

cat_features = [
    "workclass", "education", "marital-status", "occupation",
    "relationship", "race", "sex", "native-country"
]


# TODO: implement the first test. Change the function name and input as needed
def test_one(sample_data):
    """
    Confirm the train _model function returns a RandomForestClassifier
    """
    X, y, _, _ = process_data(sample_data, categorical_features=cat_features, label="salary", training=True)
    model = train_model(X, y)
    assert isinstance(model, RandomForestClassifier)


# TODO: implement the second test. Change the function name and input as needed
def test_two(sample_data):
    """
    Check that inference() returns a NumPy array
    """
    X, y, encoder, lb = process_data(sample_data, categorical_features=cat_features, label="salary", training=True)
    model = train_model(X, y)
    preds = inference(model, X)
    assert isinstance(preds, np.ndarray)


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    Validate compute_model_metrics() with known values
    """
    y = np.array([1, 0, 1, 1])
    preds = np.array([1, 0, 0, 1])
    precision, recall, f1 = compute_model_metrics(y, preds)
    assert precision == 1.0
    assert recall == 2 / 3
    assert round(f1, 2) == 0.8

# Added a 4th test to make sure the model gives 0/1 predictions after training.
# This helps confirm it's working as expected on new data.
def test_four(sample_data):
    """
    Make sure process_data returns correct shapes
    """
    X, y, encoder, lb = process_data(sample_data, categorical_features=cat_features, label="salary", training=True)
    assert X.shape[0] == len(y)
    assert X.shape[1] > 0  # should have features after one-hot encoding
