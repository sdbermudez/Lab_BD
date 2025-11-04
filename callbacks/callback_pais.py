from dash import Input, Output, State, ctx, no_update
from dash.exceptions import PreventUpdate
import pandas as pd

def call_pais_dropdown(app, engine):
    @app.callback(
        Output('pais-drop', 'options'),
        Input('pais-drop', 'search_value'),
        State('pais-drop', 'value'),
        prevent_initial_call=True
    )
    def actualizar_dropdown_paises(search_value, current_value):
        trigger = ctx.triggered_id

        # No hacer nada si no se está buscando
        if not search_value or len(search_value.strip()) < 2:
            raise PreventUpdate

        # Consulta: busca coincidencias parciales por país
        query = """
            SELECT DISTINCT "Country/Region" AS pais
            FROM full_grouped
            WHERE "Country/Region" ILIKE %s
            ORDER BY pais
            LIMIT 30;
        """

        like_param = f"%{search_value.strip()}%"
        df = pd.read_sql(query, engine, params=(like_param,))

        if df.empty:
            return []

        options = [{'label': p, 'value': p} for p in df['pais'].dropna().tolist()]
        return options
