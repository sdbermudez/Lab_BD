import dash_bootstrap_components as dbc
from dash import html, dcc
from complements.dropdowns import dropdown_mes, dropdown_variable

def layout_barras():
    return dcc.Tab(label='Diagrama de Barras',className='tab-custom', selected_className='tab-selected',children=[
        dbc.Row([
            html.H1("Diagrama de barras por variable por pais"),
            
        ]), 
        dbc.Row([
            dbc.Col([
                dropdown_mes("mes-drop")
            ], width=3), 
            dbc.Col([
                dropdown_variable('variable-drop')
            ], width=3)
        ]),
        dbc.Row([
            dcc.Graph(id='grafico-barras')
        ])
    ])