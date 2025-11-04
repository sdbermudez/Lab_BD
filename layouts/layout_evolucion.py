import dash_bootstrap_components as dbc
from dash import html, dcc
from complements.dropdowns import dropdown_variable

def layout_evo():
    return dcc.Tab(label='Evolución',className='tab-custom', selected_className='tab-selected',children=[
        dbc.Row([
            html.H1("Diagrama de dispersión"),  
        ], className='mb-4'), 
        dbc.Row([
            dbc.Col([
                dropdown_variable('variable-drop4')
            ], width=3)
        ], className='mb-4'),
        dbc.Row([
            dcc.Graph(id='grafico-evolucion')
        ], className='mb-4'),
        dbc.Row([
            dbc.Col([
                dropdown_variable('variable-drop5')
            ], width=3),
            dbc.Col([
                dropdown_variable('variable-drop6')
            ], width=3),
            dbc.Col([
                dropdown_variable('variable-drop7')
            ], width=3)
        ], className='mb-4'),
        dbc.Row([
            dcc.Graph(id="grafico-evolucion-multiple")
            
        ], className='mb-4')
        
    ])