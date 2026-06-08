import pandas as pd
from config import RAW_DIR

def read_raw_files() -> dict:
    return {
        'customers': pd.read_csv(RAW_DIR / 'customers.csv'),
        'products': pd.read_csv(RAW_DIR / 'products.csv'),
        'orders': pd.read_csv(RAW_DIR / 'orders.csv'),
        'payments': pd.read_csv(RAW_DIR / 'payments.csv'),
        'refunds': pd.read_csv(RAW_DIR / 'refunds.csv'),
    }
