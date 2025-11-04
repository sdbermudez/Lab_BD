import dash_bootstrap_components as dbc
from dash import html, dcc
from layouts.layout_histograma import layout_histogrma
from layouts.layout_barras import layout_barras
from layouts.layout_mapa import layout_map
from layouts.layout_dispersion import layout_disp
from layouts.layout_evolucion import layout_evo

def dashboard_layout():
    
    
    return dbc.Container([
         html.Div([
            html.Img(src='/assets/logo.png', style={'width': '50%', 'height': 'auto'}),
        ],className="text-center mt-4 mb-4"),
        
        dcc.Tabs(
            id= 'tabs',
            value='Descubre',
            children=[
                layout_histogrma(),
                layout_barras(),
                layout_map(), 
                layout_disp(),
                layout_evo()
            ], 
            colors={
                'border': '#42d1e0',
                'primary': "#2494a1",
                'background': "#2494a1"
            },
            persistence=True, parent_className="tabs-container", persistence_type='memory')
    ], fluid=True)