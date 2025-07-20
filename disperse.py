import pandas as pd
from db.connection import get_connection, get_engine

def run_dispersal():
    try:
        
        conn = get_connection()
        engine = get_engine()

        
        df = pd.read_parquet("data/cargo_data_transformed.parquet")

        with engine.begin() as connection:  

            
            companies_df = df[['company_id', 'company_name']].drop_duplicates(subset=['company_id'])
            companies_df.to_sql('companies', con=connection, if_exists='append', index=False)

   
            charges_df = df[['id', 'company_id', 'amount', 'status', 'created_at', 'updated_at']]
            charges_df.to_sql('charges', con=connection, if_exists='append', index=False)

        print("Datos insertados correctamente en 'companies' y 'charges'.")

        conn.close()

    except Exception as e:
        print(f"Error al insertar datos: {e}")
