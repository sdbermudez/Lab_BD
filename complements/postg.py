import pandas as pd 
from sqlalchemy import create_engine
from dotenv import load_dotenv
from pathlib import Path
import os


def conectar():
    # Crear engine de SQLAlchemy
    engine = create_engine(
        "postgresql://lab_bd_user:oxBX2o0kh9skW9GvxKVgWpKHuU8XDTmq@dpg-d456l3qdbo4c73e8t150-a.oregon-postgres.render.com/lab_bd",
        connect_args={'client_encoding': 'utf8'}
    )
    return engine


def histograma(variable, pais, engine):
    query=f"""
    with ext_mes as(
    select date_part('month',TO_DATE(f."Date", 'YYYY-MM-DD')) as mes,*
    from full_grouped f
    ),
    agrupar as(
    select e.mes, e."Country/Region", sum(e."Confirmed") as confirmed, sum(e."Deaths") as deaths,
    sum(e."Recovered") as recovered, sum(e."Active") as active, sum(e."New cases") as new_cases,
    sum(e."New deaths") as new_deaths, sum(e."New recovered") as new_recovered
    from ext_mes e
    group by e.mes, e."Country/Region"
    )
    select a.mes, a."Country/Region", a."{variable}" as "{variable}"  
    from agrupar a
    where a."Country/Region"=%s
    order by a.mes asc
    """
    df = pd.read_sql(query, engine, params=(pais,))
    if df.empty: 
        return None
    return df

def barras(variable, mes, engine):
    query=f"""
    with ext_mes as(
    select date_part('month',TO_DATE(f."Date", 'YYYY-MM-DD')) as mes,*
    from full_grouped f
    ),
    agrupar as(
    select e.mes, e."Country/Region", sum(e."Confirmed") as confirmed, sum(e."Deaths") as deaths,
    sum(e."Recovered") as recovered, sum(e."Active") as active, sum(e."New cases") as new_cases,
    sum(e."New deaths") as new_deaths, sum(e."New recovered") as new_recovered
    from ext_mes e
    group by e.mes, e."Country/Region"
    )
    select a.mes, a."Country/Region", a."{variable}" as "{variable}"  
    from agrupar a
    where a."mes"=%s
    order by a."Country/Region" asc
    """
    df = pd.read_sql(query, engine, params=(mes,))
    if df.empty:
        return None
    return df
    
    
def dispersion(engine):
    query = """
    SELECT 
        c."Country/Region",
        c."Confirmed",
        c."Deaths / 100 Cases" AS deaths_per_100_cases,
        c."Recovered / 100 Cases" AS recovered_per_100_cases,
        c."WHO Region" AS who_region
    FROM country_wise_latest c
    WHERE c."Deaths / 100 Cases" IS NOT NULL 
      AND c."Recovered / 100 Cases" IS NOT NULL
    ORDER BY c."Confirmed" DESC
    """
    
    df = pd.read_sql(query, engine)
    if df.empty:
        return None
    return df

def evolucion(engine):
    query = """
    SELECT date_part('month', to_date(d."Date",'YYYY-MM-DD')) as mes, sum(d."Confirmed") as confirmed, sum(d."Deaths") as deaths, 
    sum(d."Recovered") as recovered, sum(d."Active") as active, sum(d."New cases") as new_cases,
    sum(d."New deaths") as new_deaths, sum(d."New recovered") as new_recovered
    FROM day_wise d
    group by mes
    ORDER BY mes ASC
    """
    df = pd.read_sql(query, engine)
    if df.empty:
        return None
    return df

def evolucion_multiple(engine, variables):
    if not variables or all(v is None for v in variables):
        return None

    columnas_db = {
        "confirmed": "Confirmed",
        "deaths": "Deaths",
        "recovered": "Recovered",
        "active": "Active",
        "new_cases": "New cases",
        "new_deaths": "New deaths",
        "new_recovered": "New recovered"
    }

    variables_limpias = []
    for v in variables:
        if v is None:
            continue
        v_lower = v.strip().lower()
        if v_lower in columnas_db:
            variables_limpias.append(columnas_db[v_lower])

    if not variables_limpias:
        return None

    select_cols = [f'SUM(d."{v}") AS "{v}"' for v in variables_limpias]
    select_str = ", ".join(select_cols)

    query = f"""
    SELECT 
        date_part('month', to_date(d."Date",'YYYY-MM-DD')) AS mes,
        {select_str}
    FROM day_wise d
    GROUP BY mes
    ORDER BY mes ASC
    """

    df = pd.read_sql(query, engine)
    if df.empty:
        return None

    
    rename_map = {v: k for k, v in columnas_db.items()}
    df.rename(columns=rename_map, inplace=True)

    return df
