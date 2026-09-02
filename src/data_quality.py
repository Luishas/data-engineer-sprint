import pandas as pd
import logging

def check_nulls(df: pd.DataFrame, column: str) -> int:
    """Return how many nulls are in a given column of a DataFrame."""
    return df[column].isnull().sum()

def check_duplicates(df : pd.DataFrame, column: str) -> int:
    """Return how many duplicates are in a given column of a DataFrame."""
    return df.duplicated(subset=[column]).sum()

def check_range(df: pd.DataFrame, column: str, min_val=None, max_val=None) -> int:
    """Return how many raws are outside the specified range in a given column of a DataFrame."""    
    mask = pd.Series([False] * len(df))
    if min_val is not None:
        mask = mask | (df[column] < min_val)
    if max_val is not None:
        mask = mask | (df[column] > max_val)
    return mask.sum()

def check_referential_integrity(df_child: pd.DataFrame, df_parent: pd.DataFrame,
                                    key_child: str, key_parent: str) -> int:
    """Return how many rows in the child DataFrame do not have a corresponding row in the parent DataFrame."""
    huerfan = ~df_child[key_child].isin(df_parent[key_parent])
    return huerfan.sum()