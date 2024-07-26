# Fake-note-prediction-api
This repository contains a FastAPI application for banknote authentication. The application utilizes a pre-trained Random Forest model to classify banknotes as "Fake" or "Real" based on their features. The model is trained to predict the authenticity of banknotes based on various characteristics, such as variance, skewness, curtosis, and entropy.

MODEL FILE:

import necessary libraries and load named BankNote_Authentication.csv into a DataFrame.
Basic data exploration is performed
A pair plot is created using Seaborn to visualize the relationships between features in the dataset, with the class column used as a hue to differentiate between classes.
Features are standardized using StandardScaler to ensure that they have zero mean and unit variance.
A Random Forest classifier is initialized and trained on the standardized training data.
The model's performance is evaluated using accuracy, confusion matrix, and classification report
The trained model is saved to a file named classifier.pkl using the pickle library, allowing for future reuse without retraining.
Model Prediction:
The model is used to make predictions on new data points, which are standardized before being fed into the model.
The prediction is checked and a classification label is assigned based on whether the predicted value exceeds 0.5.

APP FILE:

API Endpoints:
GET /: Returns a simple "hello, world" message for testing.
POST /predict: Accepts banknote feature data and returns a prediction of whether the banknote is "Fake" or "Real".
Model Integration:

The application uses a Random Forest classifier, which has been trained and saved in the classifier.pkl file.
The model predicts authenticity based on features like variance, skewness, curtosis, and entropy.
Input data is validated using a Pydantic model to ensure it adheres to the expected format before making predictions.

Setup:
Load the pre-trained Random Forest model using pickle.
Define the API endpoints using FastAPI.
  GET /: Provides a basic endpoint to confirm the API is running.
  POST /predict: Processes incoming JSON data, makes predictions using the loaded model, and returns whether the banknote is "Fake" or "Real".
  Usage:
Users send feature data for banknotes to the /predict endpoint.
The API returns a prediction based on the model's output.

Installation and Running:
Clone the repository and install dependencies.
Run the FastAPI application using uvicorn.
Make POST requests to /predict with appropriate feature data to get predictions.
This API provides an accessible interface for integrating banknote authentication into various applications, leveraging machine learning for accurate predictions.
