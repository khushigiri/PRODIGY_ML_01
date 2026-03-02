import pandas as pd
import pickle
from logger import logger

try:
    logger.info("Loading trained model...")
    with open("../models/model.pkl", "rb") as f:
        model = pickle.load(f)

    logger.info("Preparing input data...")
    new_house = pd.DataFrame({
        "Square_Footage": [2000],
        "Bedrooms": [4],
        "Bathrooms": [3]
    })

    prediction = model.predict(new_house)

    logger.info("Prediction successful!")
    print("Predicted Price:", prediction[0])

except Exception as e:
    logger.error(f"Prediction failed: {e}")
    print("Prediction failed. Check logs/app.log")