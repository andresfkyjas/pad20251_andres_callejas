import sqlite3
import pandas as pd
import os
ruta = "{}/src/ibgd/arquitectura_ml/ingestion.db".format(os.getcwd())
conn = sqlite3.connect(ruta)
tabla = "jobs"
df = pd.read_sql_query(f"select * from {tabla}",conn)
print(df.head())