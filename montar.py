import pandas as pd
from sqlalchemy import create_engine
from complements.postg import conectar

ruta1 = r"C:\Users\SAMUEL\OneDrive\Documentos\2025\sexto semestre\Bases de datos\Tablero_lab\country_wise_latest.csv"
ruta2 = r"C:\Users\SAMUEL\OneDrive\Documentos\2025\sexto semestre\Bases de datos\Tablero_lab\covid_19_clean_complete.csv"
ruta3 = r"C:\Users\SAMUEL\OneDrive\Documentos\2025\sexto semestre\Bases de datos\Tablero_lab\day_wise.csv"
ruta4 = r"C:\Users\SAMUEL\OneDrive\Documentos\2025\sexto semestre\Bases de datos\Tablero_lab\full_grouped.csv"
ruta5 = r"C:\Users\SAMUEL\OneDrive\Documentos\2025\sexto semestre\Bases de datos\Tablero_lab\usa_county_wise.csv"
ruta6 = r"C:\Users\SAMUEL\OneDrive\Documentos\2025\sexto semestre\Bases de datos\Tablero_lab\worldometer_data.csv"

df1 = pd.read_csv(ruta1, low_memory=False)
df2 = pd.read_csv(ruta2, low_memory=False)
df3 = pd.read_csv(ruta3, low_memory=False)
df4 = pd.read_csv(ruta4, low_memory=False)
df5 = pd.read_csv(ruta5, low_memory=False)
df6 = pd.read_csv(ruta6, low_memory=False)

dfs = [df1,df2,df3,df4,df5,df6]

lent = 0
for l in dfs: 
    print(l.shape)
    print()
    print(l.columns)
    print("--"*40)
    lent+= len(l)
    
print(lent)
    

engine = conectar()

df1.to_sql('country_wise_lates', engine, if_exists='replace',index=False)
df2.to_sql('covid_19_clean_complete', engine, if_exists='replace',index=False)
df3.to_sql('day_wise', engine, if_exists='replace',index=False)
df4.to_sql('full_grouped', engine, if_exists='replace',index=False)
df5.to_sql('usa_county_wise', engine, if_exists='replace',index=False)
df6.to_sql('worldometer_data.csv', engine, if_exists='replace',index=False)