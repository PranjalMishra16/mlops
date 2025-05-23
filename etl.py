import pandas as pd


def load_data(path):
    return pd.read_csv("raw_data/avocado_ripening.csv")


def clean_data(df):
    df_clean = df.dropna()
    return df_clean

#def feature_engineering(df)

if __name__ == "main":
    df = load_data("raw_data/avocado_ripening.csv")
    df = clean_data(df)
    df.to_csv("processed_data/avocado_ripening_clean.csv", index =False)
    print("ETL pipeline completed successfully!")