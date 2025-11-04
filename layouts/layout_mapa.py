import dash_bootstrap_components as dbc
from dash import html, dcc
from complements.dropdowns import dropdown_mes, dropdown_variable

def layout_map():
    return dcc.Tab(label='Mapa',className='tab-custom', selected_className='tab-selected',children=[
        dbc.Row([
            html.H1("Mapa por meses por pais y variable"),
        ], className='mb-4'), 
        dbc.Row([
            dbc.Col([
                dropdown_mes("mes-drop2")
        ], width=3), 
            dbc.Col([
                dropdown_variable('variable-drop3')
                
            ], width=3)
        ], className='mb-4'), 
        dbc.Row([
            dcc.Graph(id="mapa-mundial")
            
        ], className='mb-4')
    ])