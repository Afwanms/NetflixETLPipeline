from sqlalchemy import create_engine

def load_data(df):
    engine = create_engine(
        "postgresql://postgres:Draconic@localhost:5432/netflix_db"
    )
    
    df.to_sql(
        "netflix_titles", 
        engine, 
        if_exists="replace", 
        index=False
    )