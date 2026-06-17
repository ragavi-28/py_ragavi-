import pandas as pd
import numpy as np

df = pd.read_csv("used_car_price_prediction_1M.csv")

price = df["Price"].to_numpy()
engine = df["Engine_CC"].to_numpy()
horsepower = df["Horsepower"].to_numpy()
mileage = df["Mileage_kmpl"].to_numpy()

print("Mean Price:", np.mean(price))
print("Max Price:", np.max(price))
print("Min Price:", np.min(price))
print("Sum Price:", np.sum(price))
print("Std Price:", np.std(price))
print("Median Price:", np.median(price))

print("Mean Engine_CC:", np.nanmean(engine))
print("Max Engine_CC:", np.nanmax(engine))
print("Min Engine_CC:", np.nanmin(engine))

print("Mean Horsepower:", np.nanmean(horsepower))
print("Max Horsepower:", np.nanmax(horsepower))
print("Min Horsepower:", np.nanmin(horsepower))

print("Mean Mileage:", np.nanmean(mileage))
print("Max Mileage:", np.nanmax(mileage))
print("Min Mileage:", np.nanmin(mileage))

print("Unique Brands:", df["Brand"].unique())
print("Number of Brands:", df["Brand"].nunique())

a = np.array([1, 2, 3, 4, 5, 6])
print(a.reshape(2, 3))

print(np.random.rand(5))
print(np.random.randint(1, 10, 5))

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(np.dot(x, y))