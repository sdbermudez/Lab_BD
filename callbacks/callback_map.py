from dash import Input, Output
from complements.postg import barras  # o una función similar que traiga los datos
from complements.mapa import crear_mapa

def callback_mapa(app, engine):
    @app.callback(
        Output("mapa-mundial", "figure"),
        Input("variable-drop3", "value"),
        Input("mes-drop2", "value")
    )
    def actualizar_mapa(variable, mes):
        if variable is None or mes is None:
            return {}
        df = barras(variable, mes, engine)  # Reutiliza tu función que agrupa por país
        if df is None or df.empty:
            return {}
        return crear_mapa(df, variable, mes)
