import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../data/house_prices.csv")

plt.scatter(data["Square_Footage"], data["Price"])
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.title("Square Footage vs Price")
plt.show()