import pandas as pd
import os

def save_csv(records, path):
    if not records:
        return

    os.makedirs(os.path.dirname(path), exist_ok=True)

    df = pd.DataFrame(records)
    df.sort_values("sale_date", ascending=False, inplace=True)
    df.to_csv(path, index=False)
