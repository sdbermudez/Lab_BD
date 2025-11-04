import dash_bootstrap_components as dbc
from dash import Dash, html, dcc
import plotly as plt
import os

from complements.postg import conectar
from layouts.layout_master import dashboard_layout


from callbacks.callback_pais import call_pais_dropdown
from callbacks.callback_hist import callbacks_histograma
from callbacks.callback_bars import callback_barras
from callbacks.callback_map import callback_mapa
from callbacks.callback_disper import callback_dispersion
from callbacks.callback_evolucion import callback_evo, callback_evo_multiple

engine=conectar()

app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY],suppress_callback_exceptions=True, prevent_initial_callbacks='initial_duplicate' )
app.title = "Dashboard Laboratorio"

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>Dashboard Laboratorio</title>
        <link rel="icon" type="image/png" href="/assets/icono.png">
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

app.layout= dashboard_layout()

call_pais_dropdown(app, engine)
callbacks_histograma(app, engine)
callback_barras(app, engine)
callback_mapa(app,engine)
callback_dispersion(app, engine)
callback_evo(app, engine)
callback_evo_multiple(app,engine)

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port=8050, debug=True)
