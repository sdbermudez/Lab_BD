from dash import Input, Output
from complements.postg import conectar
from complements.evolucion import crear_evolucion, crear_evolucion_multiple
from complements.postg import evolucion, evolucion_multiple

def callback_evo(app, engine):
    @app.callback(
        Output("grafico-evolucion", "figure"),
        Input("variable-drop4", "value")
    )
    def actualizar_evolucion(variable):
        if variable is None: 
            return None
        df = evolucion(engine)
        if df is None or df.empty:
            return {}
        return crear_evolucion(df, variable)

def callback_evo_multiple(app, engine):
    @app.callback(
        Output("grafico-evolucion-multiple", "figure"),
        Input("variable-drop5", "value"),
        Input("variable-drop6", "value"),
        Input("variable-drop7", "value")
    )
    def actualizar_evolucion_multiple(var1, var2, var3):
        variables = [var1, var2, var3]
        if all(v is None for v in variables):
            return {}
        df = evolucion_multiple(engine, variables)
        if df is None or df.empty:
            return {}
        return crear_evolucion_multiple(df, [v for v in variables if v is not None])
