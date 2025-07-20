# Pipeline de Datos en Python y PostgreSQL

Este proyecto implementa un pipeline ETL (Extract, Transform, Load) que permite procesar, limpiar y cargar datos de transacciones desde archivos `.csv` hacia una base de datos PostgreSQL. El flujo completo incluye:

1. **Extracción:** Conversión de archivos `.csv` a formato `.parquet`.
2. **Transformación:** Limpieza y normalización de los datos para cumplir un esquema definido.
3. **Carga:** Inserción de los datos transformados en una base de datos PostgreSQL con tablas normalizadas.

---

## Requisitos

- Python 3.9 o superior
- PostgreSQL
- Entorno virtual (recomendado)

---

## Instalación y ejecución

1. Clona el repositorio:
   ```bash
   git clone <url-del-repositorio>
   cd PipeLine
   ```

2. Crea y activa un entorno virtual:

   **Linux/macOS:**
   ```bash
   python -m venv env
   source env/bin/activate
   ```

   **Windows:**
   ```cmd
   python -m venv env
   env\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Crea la base de datos llamada `Ventas` en PostgreSQL y ejecuta el script `schema/first schema.sql` para crear la tabla `Cargos`. Además dentro de db/connection.py cambia la cadena de conexión a la tuya.

5. Ejecuta el menú principal:
   ```bash
   python menu.py
   ```

6. Desde el menú, selecciona la opción de extracción de datos. Esto generará un archivo `.parquet` en la carpeta `data`.

7. Ejecuta la opción de transformación. Esta generará un nuevo archivo `.parquet` con los datos ya limpios y transformados, además de sustituir los datos existentes en la tabla `Cargos`.

8. Elimina la tabla `Cargos` manualmente o desde PostgreSQL y ejecuta el script `schema/schema.sql` para crear dos tablas relacionadas: `companies` y `charges`.

9. Ejecuta la opción de dispersión de datos. Esta cargará los datos transformados en las dos nuevas tablas.

10. Ejecuta el script SQL `schema/view.sql` (si aplica) para crear la vista `total_transacciones_diarias`.

11. Realiza consultas `SELECT` sobre la vista para validar los resultados.

---

##  Reporte técnico

### 1.1 ¿Por qué se eligió una base de datos relacional?

PostgreSQL es ideal para datos con múltiples relaciones y estructuras normalizadas. Su modelo relacional facilita realizar consultas complejas, mantener la integridad de los datos y escalar el sistema conforme aumente el volumen.

###  Problemas encontrados y soluciones

- **Líneas vacías en el CSV:**  
  Se eliminaron usando PowerShell:
  ```powershell
  Get-Content 'data_prueba_tecnica 1.csv' | Where-Object { $_.Trim() -ne "" } | Set-Content 'data_prueba_tecnica_limpio.csv'
  ```

- **Valores nulos en claves primarias:**  
  Se resolvió generando IDs artificiales cuando faltaban.

- **Montos inconsistentes o en notación científica:**  

### 1.2 ¿Por qué usar Python y Parquet?

- **Python:**  
  - Excelente para manipulación de datos (`pandas`, `pyarrow`).
  - Fácil integración con bases de datos (`sqlalchemy`, `psycopg2`).
  - Permite automatizar flujos ETL rápidamente.

- **Parquet:**  
  - Formato columnar, comprimido y eficiente.
  - Ideal para datasets grandes.
  - Compatible con múltiples herramientas analíticas.

### 1.3 Principales transformaciones aplicadas

- Truncamiento de cadenas (`id`, `company_id`, `company_name`, `status`) a 24 caracteres.
- Conversión del campo `amount` a `Decimal(16,2)`, sustituyendo valores fuera de rango por `-1`.
- Limpieza de valores nulos (`nan`, `None`, cadenas vacías).
- Generación de identificadores artificiales cuando era necesario.

---

## Estructura del proyecto

```
PipeLine/
├── data/                      # Archivos .parquet generados
├── data_sample/              # Archivos CSV originales y limpios
├── db/                       # Conexión a PostgreSQL
│   └── connection.py
├── ERD/                      # Diagrama de entidad-relación
├── schema/                   # Scripts SQL de creación de esquema y vista
│   ├── first schema.sql
│   └── schema.sql
├── disperse.py               # Inserta los datos transformados en la base
├── extract.py                # Convierte CSV a Parquet
├── transform.py              # Limpia y transforma los datos
├── menu.py                   # Menú interactivo del pipeline
├── requirements.txt          # Dependencias del proyecto
└── README.md                 # Este archivo
```

---

## Comando útil para carga manual (opcional)

En caso de requerir cargar los datos directamente desde un CSV:

```sql
\copy cargo(id, company_name, company_id, amount, status, created_at, updated_at) FROM 'data_sample/data_prueba_tecnica_limpio.csv' DELIMITER ',' CSV HEADER NULL '';
```



