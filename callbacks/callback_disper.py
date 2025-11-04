from dash import Input, Output
from complements.postg import dispersion
from complements.dispersion import crear_dispersion
from dash import dcc

def callback_dispersion(app, engine):

    @app.callback(
        Output("grafico-dispersion", "figure"),
        Input("btn-actualizar-dispersion", "n_clicks"),
        prevent_initial_call=True
    )
    def actualizar_dispersion(n_clicks):
        df = dispersion(engine)
        if df.empty:
            return dcc.Graph(figure={}, style={'display': 'none'})

        fig = crear_dispersion(df)
        return fig
