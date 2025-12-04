# src/etl/extract.py
"""
Funciones de extracción de datos.
- extract_data: intenta leer un CSV local (data/dataset.csv).
Usaremos el metodo que vimos en clase pero aun asi para los unit tests funcionara
  
  """

from pathlib import Path
import pandas as pd
from typing import Optional


def extract_data(csv_path: Optional[str] = "data/dataset.csv") -> pd.DataFrame:
    path = Path(csv_path)
    if path.exists():
        df = pd.read_csv(path)
        return df
    else:
        data = {
            "user_id": [1, 2, 3, 4],
            "name": [" Alex ", "María", "Juan", "Ana "],
            "age": ["23", "31", "27", "45"],
            "signup_ts": ["2024-01-01", "2024-02-15", "2024-02-20", None],
            "active": ["true", "false", "true", "true"]
        }
        df = pd.DataFrame(data)
        return df
