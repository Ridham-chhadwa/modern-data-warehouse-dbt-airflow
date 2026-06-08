from sqlalchemy import create_engine
from config import DB_CONFIG, PROCESSED_DIR

def get_engine():
    return create_engine(f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}")

def save_csv(clean):
    PROCESSED_DIR.mkdir(exist_ok=True)
    for table, df in clean.items():
        df.to_csv(PROCESSED_DIR / f'{table}.csv', index=False)

def load_postgres(clean):
    engine = get_engine()
    for table, df in clean.items():
        df.to_sql(f'raw_{table}', engine, if_exists='replace', index=False)
    print('Loaded raw_* tables into PostgreSQL.')
