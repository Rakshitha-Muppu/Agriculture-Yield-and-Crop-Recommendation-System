import pandas as pd

crop_df = pd.read_csv("../dataset/crop_recommendation.csv")
yield_df = pd.read_csv("../dataset/yield_prediction.csv")

print(crop_df.head())
print(crop_df.info())

print(yield_df.head())
print(yield_df.info())