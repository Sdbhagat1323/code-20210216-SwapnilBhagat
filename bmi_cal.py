import json
import pandas as pd
import numpy as np


class Bmi_Calculator:

    def __init__(self):
        self.__data = None

    # load json File

    def connect(self, data_file):
        with open(data_file) as json_file:
            self.__data = json.load(json_file)

    # Extraction required data.
    def extract_data(self):
        self.weight = []
        self.height = []
        for person in self.__data["people"]:
            self.weight.append(person["WeightKg"])
            self.height.append(person["HeightCm"]/100)
        return self.weight, self.height

    # create new dataframe.
    def create_df(self):
        self.df = pd.DataFrame(list(zip(self.weight, self.height)),
                               columns={"WeightKg", "Heightm"})

        return self.df
        

    # Bmi calculator
    # Formula: - BMI(kg/m2) = mass(kg) / height(m)2

    def bmi_cal(self):
        self.df["BMI"] = round(
            (self.df["WeightKg"]/(self.df["Heightm"])**2), 2)
        self.df["BMI Category"] = np.nan
        self.df["Health risk"] = np.nan
        # Fill ing BMI Category columns
        self.df.loc[self.df["BMI"] <= 18.4, "BMI Category"] = "Underweight"
        self.df.loc[(self.df["BMI"] >= 18.5) & (self.df["BMI"] <=
                                                24.9), "BMI Category"] = "Normal weight"
        self.df.loc[(self.df["BMI"] >= 25) & (self.df["BMI"] <=
                                              29.9), "BMI Category"] = "Overweight"
        self.df.loc[(self.df["BMI"] >= 30) & (self.df["BMI"] <=
                                              34.9), "BMI Category"] = "Moderately obese"
        self.df.loc[(self.df["BMI"] >= 35) & (self.df["BMI"] <=
                                              39.9), "BMI Category"] = "Severely obese"
        self.df.loc[(self.df["BMI"] >= 40),
                    "BMI Category"] = "Very Severely obese"

        # Filling BMI Health risk columns
        self.df.loc[self.df["BMI"] <= 18.4,
                    "Health risk"] = "Malnutrition risk"
        self.df.loc[(self.df["BMI"] >= 18.5) & (self.df["BMI"] <=
                                                24.9), "Health risk"] = "Low risk"
        self.df.loc[(self.df["BMI"] >= 25) & (self.df["BMI"] <=
                                              29.9), "Health risk"] = "Enhanced risk"
        self.df.loc[(self.df["BMI"] >= 30) & (self.df["BMI"] <=
                                              34.9), "Health risk"] = "Medium risk"
        self.df.loc[(self.df["BMI"] >= 35) & (self.df["BMI"] <=
                                              39.9), "Health risk"] = "High risk"
        self.df.loc[(self.df["BMI"] >= 40), "Health risk"] = "Very high risk"

        return self.df

    def close(self):
        pass

# for manual testing
#bmi = Bmi_Calculator()
# print(bmi.connect("json_file.json"))
# print(bmi.extract_data())
# print(bmi.create_df())
# print(bmi.bmi_cal())
