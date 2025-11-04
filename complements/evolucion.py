import plotly.graph_objects as go

def crear_evolucion(df, variable):
    # Normalizar nombres a minúsculas por consistencia
    variable = variable.lower()
    colores = {
        "confirmed": "#2494a1",
        "deaths": "#e04f5f",
        "recovered": "#61ce70",
        "active": "#2494a1",
        "new_cases": "#2494a1",
        "new_deaths": "#2494a1",
        "new_recoved": "#2494a1", 
    }

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df["mes"],
        y=df[variable],
        mode="lines+markers",
        line=dict(width=3, color=colores.get(variable, "#2494a1")),
        marker=dict(size=8, color=colores.get(variable, "#42d1e0")),
        hovertemplate=f"<b>Mes:</b> %{{x}}<br><b>{variable.capitalize()}:</b> %{{y:,.0f}}<extra></extra>",
        name=variable.capitalize()
    ))

    fig.update_layout(
        title=f"Evolución mensual de {variable.capitalize()}",
        xaxis_title="Mes",
        yaxis_title="Número de casos",
        xaxis=dict(tickmode="linear", tick0=1, dtick=1),
        hovermode="x unified",
        plot_bgcolor="#f8f9fa",
        paper_bgcolor="#f8f9fa",
        font=dict(family="Arial", size=14, color="#2494a1"),
        title_font=dict(size=22, color="#2494a1", family="Arial Black"),
        margin=dict(l=60, r=40, t=70, b=60)
    )

    return fig


def crear_evolucion_multiple(df, variables):
    colores = {
        "confirmed": "#2494a1",
        "deaths": "#e04f5f",
        "recovered": "#61ce70",
        "active": "#f0a500",
        "new_cases": "#0077b6",
        "new_deaths": "#ff4d6d",
        "new_recovered": "#00b894"
    }

    fig = go.Figure()

    for var in variables:
        if var not in df.columns:
            continue
        var_lower = var.lower()
        fig.add_trace(go.Scatter(
            x=df["mes"],
            y=df[var],
            mode="lines+markers",
            line=dict(width=3, color=colores.get(var_lower, "#2494a1")),
            marker=dict(size=8, color=colores.get(var_lower, "#2494a1")),
            hovertemplate=f"<b>Mes:</b> %{{x}}<br><b>{var}:</b> %{{y:,.0f}}<extra></extra>",
            name=var
        ))

    fig.update_layout(
        title="Comparación mensual de variables seleccionadas",
        xaxis_title="Mes",
        yaxis_title="Número de casos",
        xaxis=dict(tickmode="linear", tick0=1, dtick=1),
        hovermode="x unified",
        plot_bgcolor="#f8f9fa",
        paper_bgcolor="#f8f9fa",
        font=dict(family="Arial", size=14, color="#2494a1"),
        title_font=dict(size=22, color="#2494a1", family="Arial Black"),
        legend_title="Variables",
        margin=dict(l=60, r=40, t=70, b=60)
    )

    return fig
