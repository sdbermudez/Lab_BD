import dash_bootstrap_components as dbc
from dash import html, dcc


def dashboard_layout():
    
    
    return dbc.Container([
        html.Div([
            #html.Img(src='/assets/logo_horizontal.jpg', style={'width': '60%', 'height': 'auto'}),
        ],className="text-center mt-4 mb-4"),
        
        dcc.Tabs(
            id= 'tabs',
            value='Descubre',
            children=[

            ], 
            colors={
                'border': '#61ce70',
                'primary': "#257737",
                'background': "#257737"
            },
            persistence=True, parent_className="tabs-container", persistence_type='memory')
    ], fluid=True)