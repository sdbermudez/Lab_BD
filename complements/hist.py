import plotly.express as px

def crear_linea(df, variable):
    fig = px.line(
        df,
        x="mes",
        y=variable,
        markers=True,  # puntos en la línea
        title=f"Evolución mensual de {variable.capitalize()}",
        labels={"mes": "Mes", variable: variable.capitalize()},
    )

    fig.update_traces(
        line=dict(color="#2494a1", width=4),  # color corporativo
        marker=dict(size=8, color="#42d1e0", line=dict(width=1.5, color="#2494a1"))
    )

    fig.update_layout(
        plot_bgcolor="#f8f9fa",
        paper_bgcolor="#f8f9fa",
        xaxis=dict(
            tickmode="array",
            tickvals=list(range(1, 13)),
            title_font=dict(size=16, color="#2494a1"),
            tickfont=dict(size=12, color="#2494a1")
        ),
        yaxis=dict(
            title="Casos",
            title_font=dict(size=16, color="#2494a1"),
            tickfont=dict(size=12, color="#2494a1")
        ),
        title=dict(
            font=dict(size=22, color="#2494a1", family="Arial Black"),
            x=0.5
        ),
        hovermode="x unified",
    )

    return fig