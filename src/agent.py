from datetime import date, timedelta
from fetchers.sd_county_recorder import fetch_recent_records
from parsers.recorder_parser import parse_records
from filters import filter_sales
from storage import save_csv
from utils import load_settings, setup_logging

def run_agent():
    settings = load_settings()
    setup_logging(settings)

    cutoff = date.today() - timedelta(days=settings["days_back"])

    raw_records = fetch_recent_records(days_back=settings["days_back"])
    parsed_records = parse_records(raw_records)

    filtered = filter_sales(
        records=parsed_records,
        min_price=settings["min_price"],
        cutoff_date=cutoff
    )

    save_csv(filtered, settings["output"]["path"])
