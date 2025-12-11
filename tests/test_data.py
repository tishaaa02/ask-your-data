# tests/test_data.py
from src.data import load_sample

def test_load_sample():
    df = load_sample()
    assert df is not None
    assert df.shape[0] > 0
