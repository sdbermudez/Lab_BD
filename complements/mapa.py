import plotly.express as px

def crear_mapa(df, variable, mes):
    df_mes = df[df["mes"] == mes]
    df_mes = df_mes[df_mes[variable] > 0]

    fig = px.choropleth(
        df_mes,
        locations="Country/Region",
        locationmode="country names",
        color=variable,
        hover_name="Country/Region",
        color_continuous_scale=["#e0f7fa", "#42d1e0", "#2494a1"],
        title=f"Distribución mundial de {variable.capitalize()} (Mes {mes})",
    )

    fig.update_layout(
        geo=dict(
            showframe=False,
            showcoastlines=True,
            projection_type="natural earth",
            coastlinecolor="#42d1e0"
        ),
        plot_bgcolor="#f8f9fa",
        paper_bgcolor="#f8f9fa",
        coloraxis_colorbar=dict(
            title=dict(
                text=variable.capitalize(),
                font=dict(size=14, color="#2494a1")
            ),
            tickfont=dict(size=12, color="#2494a1"),
            outlinewidth=1,
            outlinecolor="#2494a1"
        ),
        title=dict(
            font=dict(size=22, color="#2494a1", family="Arial Black"),
            x=0.5
        ),
        margin=dict(l=0, r=0, t=50, b=0)
    )

    return fig