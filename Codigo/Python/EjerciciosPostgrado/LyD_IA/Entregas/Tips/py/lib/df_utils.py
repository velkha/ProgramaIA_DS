from typing import List
import numpy as np
from scipy import stats
import pandas as pd

def calc_missing(df: pd.DataFrame) -> pd.Series:
    """
    Calculate the percentage of missing values in a DataFrame
    """
    missing: pd.Series = df.isnull().sum()
    missing = missing[missing > 0]
    missing_percentage: pd.Series = missing / len(df)
    missing_percentage = missing_percentage.sort_values(ascending=False)
    return missing_percentage


def drop_missing(df: pd.DataFrame, threshold: float = 0) -> pd.DataFrame:
    """
    Drop columns with missing values above a certain threshold
    """
    missing: pd.Series = calc_missing(df)
    to_drop: pd.Index = missing[missing > threshold].index
    df = df.drop(to_drop, axis=1)
    return df


def fill_missing(df: pd.DataFrame, value) -> pd.DataFrame:
    """
    Fill missing values with a certain value
    """
    df = df.fillna(value)
    return df


def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drop duplicate rows in a DataFrame
    """
    df = df.drop_duplicates()
    return df


def remove_outliers(df: pd.DataFrame, column: str, threshold: float = 3) -> pd.DataFrame:
    """
    Remove outliers from a column in a DataFrame
    """
    if df[column].dtype != np.number:
        return df
    z_scores = np.abs(stats.zscore(df[column]))
    df = df[z_scores < threshold]
    return df


def remove_outliers_iqr(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Remove outliers from a column in a DataFrame using IQR (Interquartile Range)
    """
    if df[column].dtype != np.number:
        return df
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    df = df[(df[column] > lower_bound) & (df[column] < upper_bound)]
    return df


def remove_all_outliers(df: pd.DataFrame, threshold: float = 3) -> pd.DataFrame:
    """
    Remove outliers from all numerical columns in a DataFrame
    """
    for column in df.select_dtypes(include=[np.number]).columns:
        df = remove_outliers(df, column, threshold)
    return df


def transform_to_categorical(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """
    Transform columns to categorical type
    """
    for column in columns:
        df[column] = df[column].astype('category')
    return df

def remove_corr_with_less_than(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    """
    Remove columns with correlation less than a certain threshold in negatives and positives
    """
    corr_matrix = df.corr().abs()
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))
    to_drop_neg = [column for column in upper.columns if any(upper[column] < -threshold)]
    to_drop_pos = [column for column in upper.columns if any(upper[column] > threshold)]
    to_drop = to_drop_neg + to_drop_pos
    df = df.drop(to_drop, axis=1)
    return df

def get_outliers(df, column, threshold=1.5):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - threshold * IQR
    upper_bound = Q3 + threshold * IQR
    
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers

def get_outliers_multiple(df, columns, threshold=1.5):
    all_outliers_indices = set()
    
    for column in columns:
        column_outliers = get_outliers(df, column, threshold)
        all_outliers_indices.update(column_outliers.index)
    
    all_outliers = df.loc[list(all_outliers_indices)]
    return all_outliers