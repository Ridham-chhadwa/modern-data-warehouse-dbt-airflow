from ingest import read_raw_files
from clean import clean_all
from quality import create_quality_report
from load import save_csv, load_postgres

def run_pipeline(load_to_db=False):
    print('Starting modern data warehouse ingestion pipeline...')
    raw = read_raw_files()
    clean = clean_all(raw)
    save_csv(clean)
    report_path = create_quality_report(raw, clean)
    if load_to_db:
        load_postgres(clean)
    else:
        print('Database load skipped. Set load_to_db=True after configuring PostgreSQL.')
    print(f'Pipeline completed. Quality report: {report_path}')

if __name__ == '__main__':
    run_pipeline(load_to_db=False)
