from dash import Input, Output
from dash.exceptions import PreventUpdate
from complements.postg import histograma
from complements.hist import crear_linea  # donde está la función anterior

def callbacks_histograma(app, engine):
    @app.callback(
        Output("grafico-histograma", "figure"),
        Input("pais-drop", "value"),
        Input("variable-drop2", "value")
    )
    def actualizar_histograma(pais, variable):
        if not pais or not variable:
            raise PreventUpdate
        df = histograma(variable, pais, engine)
        if df.empty:
            raise PreventUpdate
        fig = crear_linea(df, variable)
        return fig
