from ingestion.load import load_data
from ingestion.clean import clean_data
from ingestion.validate import validate_data
from ingestion.save import save_data

def run_pipeline():
    df = load_data("data/raw/events.csv")
    df = clean_data(df)
    validate_data(df)
    save_data(df)

if __name__ == "__main__":
    run_pipeline()