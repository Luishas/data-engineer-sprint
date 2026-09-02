import pandas as pd
import sys 
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))
from data_quality import check_nulls, check_duplicates, check_range, check_referential_integrity

def test_check_nulls_correctly_working():
    df = pd.DataFrame({"id": [1, 2, None, 4]})
    assert check_nulls(df,"id") == 1

def test_check_duplicates_correctly_working():
    df = pd.DataFrame({"id" :[1, 2, 2, 3]})
    assert check_duplicates(df, "id") == 1

def test_check_range_correctly_working():
    df = pd.DataFrame({"price": [10, -5, 20, 0]})
    assert check_range(df, "price", min_val=0) == 1

def test_check_referential_integrity_correctly_working():
    df_child = pd.DataFrame({"order_id": [1, 2, 3, 99]})
    df_parent = pd.DataFrame({"order_id": [1, 2, 3]})
    assert check_referential_integrity(df_child, df_parent, "order_id", "order_id") == 1   