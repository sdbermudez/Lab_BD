import plotly.express as px
import pandas as pd

def crear_barras(df, variable):
    # Agrupar los países fuera del top 5
    df_ordenado = df.sort_values(by=variable, ascending=False).reset_index(drop=True)
    if len(df_ordenado) > 5:
        otros_valor = df_ordenado.loc[5:, variable].sum()
        df_top = df_ordenado.loc[:4, ["Country/Region", variable]]
        df_top.loc[len(df_top)] = ["Others", otros_valor]
    else:
        df_top = df_ordenado.copy()

    # Orden ascendente para visualización
    df_top = df_top.sort_values(by=variable, ascending=True)

    # Crear gráfico de barras vertical
    fig = px.bar(
        df_top,
        x="Country/Region",
        y=variable,
        text_auto='.2s',
        title=f"Top 5 países por {variable.capitalize()} (resto agrupado en Others)",
        color_discrete_sequence=["#2494a1"]
    )

    # Estilo de barras
    fig.update_traces(
        marker_line_color="#42d1e0",
        marker_line_width=1.5,
        textfont=dict(color="#ffffff", size=12)
    )

    # Layout
    fig.update_layout(
        plot_bgcolor="#f8f9fa",
        paper_bgcolor="#f8f9fa",
        xaxis=dict(
            title="País",
            title_font=dict(size=16, color="#2494a1"),
            tickfont=dict(size=12, color="#2494a1")
        ),
        yaxis=dict(
            title=variable.capitalize(),
            title_font=dict(size=16, color="#2494a1"),
            tickfont=dict(size=12, color="#2494a1"),
            gridcolor="#e5e5e5"
        ),
        title=dict(
            font=dict(size=22, color="#2494a1", family="Arial Black"),
            x=0.5
        ),
        hovermode="x unified",
        margin=dict(l=60, r=40, t=60, b=60)
    )

    return fig
