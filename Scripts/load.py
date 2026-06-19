from sqlalchemy import create_engine

def load_data(df):
    engine = create_engine(
        "postgresql://airflow:airflow@postgres:5432/airflow"
    )
    
    df.to_sql(
        "netflix_titles", 
        engine, 
        if_exists="replace", 
        index=False
    )