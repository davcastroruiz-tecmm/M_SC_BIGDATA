import pandas as pd
from src.etl.extract import extract_data

def test_extract_returns_dataframe():
    df = extract_data()
    assert isinstance(df, pd.DataFrame), "extract_data() must return a DataFrame"

def test_extract_not_empty():
    df = extract_data()
    assert len(df) > 0, "Extracted DataFrame should not be empty"
