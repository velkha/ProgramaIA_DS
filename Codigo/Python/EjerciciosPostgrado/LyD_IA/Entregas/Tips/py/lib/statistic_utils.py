### WORK IN PROGRESS ###

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
def normalize_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize a DataFrame
    """
    df = (df - df.min()) / (df.max() - df.min())
    return df

def standardize_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize a DataFrame
    """
    df = (df - df.mean()) / df.std()
    return df

def scale_df(df: pd.DataFrame, scaler) -> pd.DataFrame:
    """
    Scale a DataFrame using a scaler
    """
    df = scaler.fit_transform(df)
    return df

def inverse_scale_df(df: pd.DataFrame, scaler) -> pd.DataFrame:
    """
    Inverse scale a DataFrame using a scaler
    """
    df = scaler.inverse_transform(df)
    return df

def encode_categorical(df: pd.DataFrame, columns) -> pd.DataFrame:
    """
    Encode categorical columns in a DataFrame
    """
    df = pd.get_dummies(df, columns=columns)
    return df

def encode_categorical_label(df: pd.DataFrame, column) -> pd.DataFrame:
    """
    Encode a categorical column in a DataFrame using Label Encoding
    """
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    return df
