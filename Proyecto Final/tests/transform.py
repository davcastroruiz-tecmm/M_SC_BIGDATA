import pandas as pd
from src.etl.transform import transform_data

def test_transform_schema():
    raw = pd.DataFrame({
        "name": [" ALEX ", " MARIA "],
        "age": ["23", "31"]
    })

    df = transform_data(raw)

    assert "name" in df.columns
    assert "age" in df.columns
    assert df["name"].str.contains(" ").sum() == 0, "Names must be stripped"
    assert df["age"].dtype in [int, "int64"], "Age must be converted to integer"

def test_transform_no_nulls():
    raw = pd.DataFrame({
        "name": ["Alex", None],
        "age": ["23", "31"]
    })
    df = transform_data(raw)
    assert df["name"].isna().sum() == 0, "Transform should handle nulls"
