import pandas as pd

def transform_data(df):
    df = df.drop_duplicates()
    df["director"] = df["director"].fillna("Unknown")
    df["cast"] = df["cast"].fillna("Unknown")
    df["country"] = df["country"].fillna("Unknown")
    df = df.rename(
        columns={"cast": "cast_members"}
    )
    df['date_added'] = pd.to_datetime(
        df['date_added'], errors='coerce'
    )

    return df