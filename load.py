import json
import pandas as pd
import numpy as np

# load json File

with open("json_file.json", 'r') as f:
    data = json.load(f)


# Extraction required data.
weight = []
height = []
for person in data["people"]:
    weight.append(person["WeightKg"])
    height.append(person["HeightCm"] / 100)

# create new dataframe.
df = pd.DataFrame(list(zip(weight, height)), columns={"WeightKg", "Heightm"})


# Bmi calculator
# Formula: - BMI(kg/m2) = mass(kg) / height(m)2


def bmi_cal(df):
    df["BMI"] = round((df["WeightKg"]/(df["Heightm"])**2), 2)
    df["BMI Category"] = np.nan
    df["Health risk"] = np.nan
    # Fill ing BMI Category columns
    df.loc[df["BMI"] <= 18.4, "BMI Category"] = "Underweight"
    df.loc[(df["BMI"] >= 18.5) & (df["BMI"] <=
                                  24.9), "BMI Category"] = "Normal weight"
    df.loc[(df["BMI"] >= 25) & (df["BMI"] <=
                                29.9), "BMI Category"] = "Overweight"
    df.loc[(df["BMI"] >= 30) & (df["BMI"] <=
                                34.9), "BMI Category"] = "Moderately obese"
    df.loc[(df["BMI"] >= 35) & (df["BMI"] <=
                                39.9), "BMI Category"] = "Severely obese"
    df.loc[(df["BMI"] >= 40), "BMI Category"] = "Very Severely obese"

    # Fill ing BMI Health risk columns
    df.loc[df["BMI"] <= 18.4, "Health risk"] = "Malnutrition risk"
    df.loc[(df["BMI"] >= 18.5) & (df["BMI"] <=
                                  24.9), "Health risk"] = "Low risk"
    df.loc[(df["BMI"] >= 25) & (df["BMI"] <=
                                29.9), "Health risk"] = "Enhanced risk"
    df.loc[(df["BMI"] >= 30) & (df["BMI"] <=
                                34.9), "Health risk"] = "Medium risk"
    df.loc[(df["BMI"] >= 35) & (df["BMI"] <=
                                39.9), "Health risk"] = "High risk"
    df.loc[(df["BMI"] >= 40), "Health risk"] = "Very high risk"

    # if (bmi > 30), df["BMI Category"], df["Health risk"] = "Underweight", "Malnutrition risk"

    return df


print(bmi_cal(df))
# https: // www.youtube.com/watch?v = bbp_849-RZ4
