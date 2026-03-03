import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pickle
from logger import logger

try:
    logger.info("Loading dataset...")
    data = pd.read_csv("../data/house_prices.csv")

    X = data[["Square_Footage", "Bedrooms", "Bathrooms"]]
    y = data["Price"]

    logger.info("Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    logger.info("Training model...")
    model = LinearRegression()
    model.fit(X_train, y_train)

    logger.info("Making predictions...")
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("Mean Squared Error:", mse)
    print("R2 Score:", r2)

    logger.info(f"MSE: {mse}")
    logger.info(f"R2 Score: {r2}")

    logger.info("Saving model...")
    with open("../models/model.pkl", "wb") as f:
        pickle.dump(model, f)

    logger.info("Training completed successfully!")

except Exception as e:
    logger.error(f"Error occurred: {e}")
    print("Something went wrong. Check logs/app.log")