from dateutil.parser import parse

def parse_records(raw_records):
    records = []

    for row in raw_records:
        try:
            records.append({
                "address": row["Property Address"],
                "sale_price": int(row["Sale Amount"]),
                "sale_date": parse(row["Recording Date"]).date(),
                "parcel": row.get("APN"),
                "property_type": row.get("Property Type")
            })
        except Exception:
            continue

    return records
