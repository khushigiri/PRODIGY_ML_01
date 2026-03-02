import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
from logger import logger

try:
    logger.info("Loading dataset...")
    data = pd.read_csv("../data/house_prices.csv")

    logger.info("Splitting features and target...")
    X = data[["Square_Footage", "Bedrooms", "Bathrooms"]]
    y = data["Price"]

    logger.info("Performing train-test split...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    logger.info("Training model...")
    model = LinearRegression()
    model.fit(X_train, y_train)

    logger.info("Saving model...")
    with open("../models/model.pkl", "wb") as f:
        pickle.dump(model, f)

    logger.info("Model training completed successfully!")

except Exception as e:
    logger.error(f"Error occurred: {e}")
    print("Something went wrong. Check logs/app.log")