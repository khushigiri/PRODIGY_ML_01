
# House Price Prediction using Linear Regression

This project implements a Multiple Linear Regression model to predict house prices based on:

- Square Footage
- Number of Bedrooms
- Number of Bathrooms

The project follows an industry-standard modular structure including model training, prediction, visualization, logging, and exception handling.

## Features

- Multiple Linear Regression using Scikit-Learn
- Train-Test Split
- Model Serialization using Pickle
- Logging using Python logging module
- Exception Handling
- Data Visualization using Matplotlib
- Modular Project Structure

## Model Details

The model learns the equation:

Price = b0 + b1*(Square_Footage) + b2*(Bedrooms) + b3*(Bathrooms)

Where:
- b0 = Intercept
- b1, b2, b3 = Coefficients

## Evaluation Metrics

- Mean Squared Error (MSE)
- R² Score

## Technologies Used

- Python 3.x
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Pickle
- Logging Module