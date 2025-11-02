import dash_bootstrap_components as dbc
from dash import Dash, html, dcc
import plotly as plt
import os

from complements.postg import conectar
from layouts.layout_master import dashboard_layout

engine=conectar()

app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY],suppress_callback_exceptions=True, prevent_initial_callbacks='initial_duplicate' )
app.title = "Dashboard Laboratorio"

app.layout= dashboard_layout()

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port=8050, debug=True)
