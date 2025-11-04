import plotly.express as px

def crear_dispersion(df):
    fig = px.scatter(
        df,
        x="recovered_per_100_cases",
        y="deaths_per_100_cases",
        size="Confirmed",
        color="who_region",
        hover_name="Country_Region",
        title="Relación entre recuperación y letalidad por país",
        color_discrete_sequence=["#2494a1", "#42d1e0", "#6ad0e0", "#a2e8f0"]
    )

    fig.update_traces(
        marker=dict(line=dict(width=1.5, color="#ffffff")),
        opacity=0.8
    )

    fig.update_layout(
        plot_bgcolor="#f8f9fa",
        paper_bgcolor="#f8f9fa",
        xaxis=dict(
            title="Recuperados / 100 Casos",
            title_font=dict(size=16, color="#2494a1"),
            tickfont=dict(size=12, color="#2494a1"),
            gridcolor="#e5e5e5"
        ),
        yaxis=dict(
            title="Muertes / 100 Casos",
            title_font=dict(size=16, color="#2494a1"),
            tickfont=dict(size=12, color="#2494a1"),
            gridcolor="#e5e5e5"
        ),
        title=dict(
            font=dict(size=22, color="#2494a1", family="Arial Black"),
            x=0.5
        ),
        legend_title=dict(text="Región OMS", font=dict(color="#2494a1")),
        margin=dict(l=60, r=40, t=60, b=60)
    )
    return fig
