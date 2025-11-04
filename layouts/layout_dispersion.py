import dash_bootstrap_components as dbc
from dash import html, dcc
from complements.dropdowns import boton

def layout_disp():
    return dcc.Tab(label='Diagrama de dispersión',className='tab-custom', selected_className='tab-selected',children=[
        dbc.Row([
            html.H1("Diagrama de dispersión"),  
        ], className='mb-4'), 
        dbc.Row([
            dbc.Col([
                boton()
            ], width=3)
        ], className='mb-4'),
        dbc.Row([
            dcc.Graph(id='grafico-dispersion')
        ], className='mb-4')
    ])