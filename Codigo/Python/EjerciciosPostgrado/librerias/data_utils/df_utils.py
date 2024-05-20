import numpy as np
from scipy import stats

def calc_missing (df):
    """
    Calculate the percentage of missing values in a DataFrame
    """
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    missing_percentage = missing / len(df)
    missing_percentage = missing_percentage.sort_values(ascending=False)
    return missing_percentage

def drop_missing (df, threshold=0):
    """
    Drop columns with missing values above a certain threshold
    """
    missing = calc_missing(df)
    to_drop = missing[missing > threshold].index
    df = df.drop(to_drop, axis=1)
    return df

def fill_missing (df, value):
    """
    Fill missing values with a certain value
    """
    df = df.fillna(value)
    return df

def drop_duplicates (df):
    """
    Drop duplicate rows in a DataFrame
    """
    df = df.drop_duplicates()
    return df


def remove_outliers (df, column, threshold=3):
    """
    Remove outliers from a column in a DataFrame
    """
    if df[column].dtype != np.number:
        return df
    z_scores = np.abs(stats.zscore(df[column]))
    df = df[z_scores < threshold]
    return df

def remove_outliers_iqr (df, column):
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

def remove_all_outliers (df, threshold=3):
    """
    Remove outliers from all numerical columns in a DataFrame
    """
    #The include parameter is used to specify the data types to be included while selecting the columns
    #so that we can remove outliers from only numerical columns
    for column in df.select_dtypes(include=[np.number]).columns:
        df = remove_outliers(df, column, threshold)
    return df