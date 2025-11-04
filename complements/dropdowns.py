from dash import html, dcc


meses = [
    {'label': 'enero', 'value': 1},
    {'label': 'febrero', 'value': 2},
    {'label': 'marzo', 'value': 3},
    {'label': 'abril', 'value': 4},
    {'label': 'mayo', 'value': 5},
    {'label': 'junio', 'value': 6},
    {'label': 'julio', 'value': 7}
]
def dropdown_mes(id_mes):
    return dcc.Dropdown(
        id = id_mes,
        options = meses,
        placeholder="Seleccione un mes",
        value=None,
        clearable=True,
        persistence=True, 
        searchable=True, 
        style = {'cursos':'text'}
)
    
def dropdown_pais():
    return dcc.Dropdown(
        id='pais-drop',
        options=[],
        placeholder="Seleccione un pais",
        value=None,
        clearable=True,
        persistence=True, 
        searchable=True, 
        style = {'cursos':'text'}
    )
    
variables = [
    {'label': 'confirmed', 'value': 'confirmed'},
    {'label': 'deaths', 'value': 'deaths'},
    {'label': 'recovered', 'value': 'recovered'},
    {'label': 'active', 'value': 'active'},
    {'label': 'new_cases', 'value': 'new_cases'},
    {'label': 'new_deaths', 'value': 'new_deaths'},
    {'label': 'new_recovered', 'value': 'new_recovered'}
]

def dropdown_variable(id_drop):
    return dcc.Dropdown(
        id=id_drop,
        options=variables,
        placeholder="Seleccione una variable",
        value=None,
        clearable=True,
        persistence=True,
        searchable=True,
        style={'cursor': 'text'}
    )
    
def boton():
    return html.Button(
    "Actualizar gráfico",
    id="btn-actualizar-dispersion",
    n_clicks=0,
    style={
        "backgroundColor": "#2494a1",
        "color": "white",
        "border": "none",
        "padding": "10px 20px",
        "borderRadius": "8px",
        "fontWeight": "bold",
        "cursor": "pointer",
        "boxShadow": "2px 2px 5px rgba(0,0,0,0.2)",
        "transition": "0.3s",
    }
)