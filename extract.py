import pandas as pd
import os
from db.connection import get_connection, get_engine

def run_extraction():
    try:
        
        os.makedirs("data", exist_ok=True)

        print("Iniciando extracción de datos...")
        
        conn = get_connection()
        
        print("Conectando a la base de datos...")
        conn = get_connection()
        engine = get_engine()

        print("Conectado a PostgreSQL")

        
        query = "SELECT * FROM cargo;"
        df = pd.read_sql(query, engine)

        print(f"{len(df)} registros extraídos")

        
        output_file = "data/cargo_data.parquet"
        df.to_parquet(output_file, index=False)

        print(f"Datos guardados en {output_file}")

        
        conn.close()

    except Exception as e:
        print(f"Error en extracción: {e}")

