import pandas as pd
import numpy as np
import os
from sqlalchemy import text
from db.connection import get_connection, get_engine

def run_transformation():
    try:
        input_path = "data/cargo_data.parquet"
        output_path = "data/cargo_data_transformed.parquet"
        table_name = "cargo"

 
        df = pd.read_parquet(input_path)
        print(f"Datos cargados: {len(df)} registros")

        df['id'] = df['id'].astype(str).str.slice(0, 24)

    
        df['id'] = df['id'].replace(['None', 'nan'], None)

    
        null_id_indices = df[df['id'].isnull()].index
        for i, idx in enumerate(null_id_indices, start=1):
            df.at[idx, 'id'] = f"NULL_ID_{i}"
        
        df['company_id'] = df['company_id'].astype(str).str.slice(0, 24)
        df['company_id'] = df['company_id'].replace('nan', None)
        

        

        df['company_name'] = df['company_name'].astype(str).replace('nan', None)
        df['company_name'] = df['company_name'].apply(lambda x: x[:130] if pd.notnull(x) else x)

        df['amount'] = pd.to_numeric(df['amount'], errors='coerce').round(2)
        df.loc[df['amount'].abs() >= 1e14, 'amount'] = -1


        df['status'] = df['status'].astype(str).str.slice(0, 30).replace('nan', None)

        df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
        df['updated_at'] = pd.to_datetime(df['updated_at'], errors='coerce')


        campos_a_validar = df.columns.difference(['updated_at'])
        columnas_con_nulos = df[campos_a_validar].columns[df[campos_a_validar].isnull().any()].tolist()

        if columnas_con_nulos:
            raise ValueError(f"Se encontraron valores nulos en columnas no permitidas: {columnas_con_nulos}")


        df.to_parquet(output_path, index=False)
        print(f"Transformación completada y guardada en '{output_path}'")


        conn = get_connection()
        engine = get_engine()

        with engine.begin() as connection:
            print("Eliminando registros existentes...")
            connection.execute(text(f"DELETE FROM {table_name}"))

            print("Insertando datos transformados en base de datos...")
            df.to_sql(table_name, connection, if_exists='append', index=False)

        print(f"Datos reemplazados exitosamente en la tabla '{table_name}'")

    except Exception as e:
        print(f"Error en transformación e inserción: {e}")
