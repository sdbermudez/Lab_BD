from dash import Input, Output
import dash
import pandas as pd
from complements.postg import barras
from complements.bars import crear_barras


def callback_barras(app, engine):
    @app.callback(
        Output("grafico-barras", "figure"),
        Input("variable-drop", "value"),
        Input("mes-drop", "value")
    )
    def actualizar_barras(variable, mes):
        if variable is None or mes is None:
            return dash.no_update

        df = barras(variable, mes, engine)
        if df is None or df.empty:
            return dash.no_update

        fig = crear_barras(df, variable)
        return fig
