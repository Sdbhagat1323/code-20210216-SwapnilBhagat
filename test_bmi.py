from bmi_cal import Bmi_Calculator
import pytest
from random import randint
import os


@pytest.fixture(scope='module')
def db():
    print('----------------setup---------------------')
    db = Bmi_Calculator()
    db.connect('data.json')
    yield db
    print('----------------teardown---------------------')
    db.close()


def test_extract_data(db):
    df = db.extract_data()
    assert len(df[0]) == len(df[1])
    assert type(df[0]) == type(df[1])


def test_create_df(db):
    df = db.create_df()
    assert len(df["Heightm"]) == len(df["WeightKg"])


def test_bmi_cal(db):
    df = db.bmi_cal()
    assert len(df["BMI"]) == len(df["Heightm"]) == len(df["WeightKg"])
    assert(type(df).__name__ == 'DataFrame')
    for num in df["BMI"]:
        assert(type(num) is float)

    for char in df["Health risk"]:
        assert(type(char) is str)

    for char in df["BMI Category"]:
        assert(type(char) is str)

    print(df)
