import pandas as pd

def extract_data(file_path):
    return pd.read_csv(file_path)

if __name__ == "__main__":
    df = extract_data("../NetflixETLPipeline/Data/Raw/netflix_titles.csv")
    print(df.head())