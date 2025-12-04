from unittest.mock import MagicMock
from src.etl.load import load_to_postgres

def test_load_called_correctly():
    mock_conn = MagicMock()
    mock_engine = MagicMock()
    df = MagicMock()

    load_to_postgres(df, mock_engine)

    assert mock_engine.connect.called, "load_to_postgres debe intentar conectar"
