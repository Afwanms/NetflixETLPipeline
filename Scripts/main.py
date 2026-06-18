from extract import extract_data
from transform import transform_data
from load import load_data

df = extract_data("../NetflixETLPipeline/Data/Raw/netflix_titles.csv")
df = transform_data(df)
load_data(df)
print("ETL process completed successfully.")