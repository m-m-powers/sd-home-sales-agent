def filter_sales(records, min_price, cutoff_date):
    return [
        r for r in records
        if r["sale_price"] >= min_price
        and r["sale_date"] >= cutoff_date
    ]
