from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from app import *
from components import sidebar, dashboards, extratos

from globals import *

# =========  Layout  =========== #
content = html.Div(id="page-content")

app.layout = dbc.Container(children=[

    #Configurando para salvar projeto na memoria de cada usuario
    #utilizando as variaveis locai e nao as globais
    dcc.Store(id='store-receitas',data=df_receitas.to_dict()),
    dcc.Store(id='store-despesas',data=df_despesas.to_dict()),
    dcc.Store(id='store-cat-despesas',data=df_cat_despesa.to_dict()),
    dcc.Store(id='store-cat-receitas',data=df_cat_receita.to_dict()),

    # Criando uma linha e duas colunas
    dbc.Row([
        dbc.Col([
            dcc.Location(id='url'),
            sidebar.layout
        ], md=2),
        dbc.Col([
            content
        ], md=10)
    ])

], fluid=True, )


# Callbacks
@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def render_page(pathname):
    if pathname == '/' or pathname == '/dashboards':
        return dashboards.layout

    if pathname == '/extratos':
        return extratos.layout


# Debug para cada alteracao feita ele atualiza nosso projeto
if __name__ == '__main__':
    app.run_server(port=8051, debug=True)
