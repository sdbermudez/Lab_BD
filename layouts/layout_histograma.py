import dash_bootstrap_components as dbc
from dash import html, dcc
from complements.dropdowns import dropdown_pais, dropdown_variable

def layout_histogrma():
    return dcc.Tab(label='Histograma',className='tab-custom', selected_className='tab-selected',children=[
        dbc.Row([
            html.H1("Histograma por meses por pais y variable"),
        ]), 
        dbc.Row([
            dbc.Col([
                dropdown_pais()
        ], width=3), 
            dbc.Col([
                dropdown_variable('variable-drop2')
                
            ], width=3)
        ]), 
        dbc.Row([
            dcc.Graph(id="grafico-histograma")
        ])
    ])