# src/etl/transform.py
"""
Transformaciones básicas:
- limpieza de strings
- casting de tipos
- manejo de nulls
- normalizaciones simples
"""

import pandas as pd
from typing import List


def _strip_string_columns(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.select_dtypes(include=["object", "string"]).columns:
        # Evita transformar columnas datetime que vengan como object a menos que quieras
        df[col] = df[col].astype("string").str.strip()
    return df


def _to_bool_series(s: pd.Series) -> pd.Series:
    # Convierte strings 'true'/'false', 1/0, etc. a boolean
    return s.astype("string").str.lower().map({"true": True, "false": False, "1": True, "0": False})


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Realiza transformaciones comunes y devuelve un DataFrame listo para cargar.
    Cambia tipos, maneja nulos y normaliza algunos campos.
    """
    df = df.copy()

    # 1) Strip en strings
    df = _strip_string_columns(df)

    # 2) Normalizar nombres: capitalizar (opcional)
    if "name" in df.columns:
        df["name"] = df["name"].fillna("").str.title()

    # 3) Cast de edades a int si existe
    if "age" in df.columns:
        # eliminar caracteres no numéricos antes de convertir
        df["age"] = df["age"].astype("string").str.extract(r"(\d+)", expand=False)
        df["age"] = pd.to_numeric(df["age"], errors="coerce").fillna(0).astype(int)

    # 4) Campos booleanos
    if "active" in df.columns:
        df["active"] = _to_bool_series(df["active"]).fillna(False)

    # 5) Fechas
    if "signup_ts" in df.columns:
        df["signup_ts"] = pd.to_datetime(df["signup_ts"], errors="coerce")

    # 6) Eliminar duplicados simples
    df = df.drop_duplicates()

    # 7) Manejo de nulos: ejemplo simple
    df = df.fillna({"name": "Unknown", "age": 0})

    return df
