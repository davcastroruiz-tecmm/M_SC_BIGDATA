# src/etl/load.py
"""
Funciones para cargar DataFrame a PostgreSQL usando SQLAlchemy.
- load_to_postgres(df, table_name, db_uri=None, engine=None, if_exists='append')
"""

import os
import logging
from typing import Optional

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_engine_from_env(env_var: str = "DATABASE_URL") -> Engine:
    """
    Crea un engine de SQLAlchemy leyendo la variable de entorno DATABASE_URL.
    Ejemplo de DATABASE_URL:
      postgresql+psycopg2://postgress:airflow@host.docker.interl:5433/airflow
    """
    db_uri = os.getenv(env_var)
    if not db_uri:
        raise RuntimeError(f"Variable de entorno {env_var} no definida. Define la connection string de Postgres.")
    engine = create_engine(db_uri, pool_pre_ping=True)
    return engine


def load_to_postgres(
    df: pd.DataFrame,
    table_name: str,
    db_uri: Optional[str] = None,
    engine: Optional[Engine] = None,
    if_exists: str = "append",
) -> None:
    """
    Inserta un DataFrame en Postgres.
    - df: DataFrame a insertar
    - table_name: nombre de la tabla destino
    - db_uri: opcional, si no pasas engine
    - engine: si ya tienes un engine, pásalo (útil para tests / reuse)
    - if_exists: 'append' | 'replace' | 'fail'
    """
    local_engine = engine
    created_engine = False

    try:
        if local_engine is None:
            if db_uri:
                local_engine = create_engine(db_uri, pool_pre_ping=True)
                created_engine = True
            else:
                local_engine = get_engine_from_env()
                created_engine = True

        # Usar to_sql con método multi para inserciones más rápidas
        logger.info("Iniciando carga a Postgres: table=%s, rows=%d", table_name, len(df))
        # Si df está vacío no hacemos nada
        if df.empty:
            logger.warning("DataFrame vacío: no se inserta nada")
            return

        df.to_sql(name=table_name, con=local_engine, if_exists=if_exists, index=False, method="multi")
        logger.info("Carga finalizada correctamente.")
    except Exception as e:
        logger.exception("Error cargando DataFrame a Postgres: %s", e)
        raise
    finally:
        if created_engine and local_engine is not None:
            try:
                local_engine.dispose()
            except Exception:
                pass
