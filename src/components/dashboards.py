from dash import html, dcc
from dash.dependencies import Input, Output, State
from datetime import date, datetime, timedelta
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import calendar
#from globals import *
from app import app

card_icon ={
    "color":"white",
    "textAlign":"center",
    "fontSize":30,
    "margin":"auto",
}


# =========  Layout  =========== #
layout = dbc.Col([
       dbc.Row([

#=============================Cards de detalhes gerais======================================
# Linha 1
            #Card Saldo Total
            dbc.Col([
                dbc.CardGroup([
                    dbc.Card([
                        html.Legend('Saldo'),
                        html.H5('R$ 5.400,00', id= 'p-saldo-dashboards',style={})
                    ], style={'padding-left':'20px','padding-top':'10px'}),
                    dbc.Card(
                                        #Pegando icone da biblioteca e importando o estilo declarado no começo
                    html.Div(className='fa fa-university', style=card_icon),
                    color='warning',
                    style={'maxWidth':75, 'height': 100, 'margin-left':'-10px'}
                    )
                ])
            ],width=4),


            #Card Receita
            dbc.Col([
                dbc.CardGroup([
                    dbc.Card([
                        html.Legend('Receita'),
                        html.H5('R$ 10.000,00', id= 'p-receita-dashboards',style={})
                    ], style={'padding-left':'20px','padding-top':'10px'}),
                    dbc.Card(
                                        #Pegando icone da biblioteca e importando o estilo declarado no começo
                    html.Div(className='fa fa-smile-o', style=card_icon),
                    color='success',
                    style={'maxWidth':75, 'height': 100, 'margin-left':'-10px'}
                    )
                ])
            ],width=4),


            #Card Despesa
            dbc.Col([
                dbc.CardGroup([
                    dbc.Card([
                        html.Legend('Despesa'),
                        html.H5('R$ 4.600,00', id= 'p-despesa-dashboards',style={})
                    ], style={'padding-left':'20px','padding-top':'10px'}),
                    dbc.Card(
                                        #Pegando icone da biblioteca e importando o estilo declarado no começo
                    html.Div(className='fa fa-meh-o', style=card_icon),
                    color='danger',
                    style={'maxWidth':75, 'height': 100, 'margin-left':'-10px'}
                    )
                ])
            ],width=4)
    ], style={'margin':'10px'}),


#=======================================Filtros=======================================================
#linha 2 coluna 1
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.Legend("Filtrar Lançamentos",className="card-title"),
                html.Label("Categorias das Receitas"),
                html.Div(
                    dcc.Dropdown(
                        id="dropdown-receita",
                        clearable=False,
                        style={"width":"100%"},
                        persistence=True,
                        persistence_type="session",
                        multi=True
                    )
                ),

                html.Label("Categorias das Despesas", style={"margin-top":"10px"}),
                    dcc.Dropdown(
                        id="dropdown-despesa",
                        clearable=False,
                        style={"width":"100%"},
                        persistence=True,
                        persistence_type="session",
                        multi=True
                    ),


                html.Legend("Periodo de Análise", style={"margin-top": "10px"}),
                    #Range pega um periodo
                    dcc.DatePickerRange(
                        month_format='Do MMM, YY',
                        end_date_placeholder_text='Data...',
                        start_date=datetime(2023, 2, 27).date(),
                        end_date=datetime.today() + timedelta(days=31),
                        updatemode='singledate',
                        id='date-picker-config',
                        style={'z-index':'100'}),
            ],style={'height':'100%', 'padding':'20px'})
        ], width=4),#tamanho do card de filtros

#linha 2 coluna 2
        dbc.Col(
            dbc.Card(dcc.Graph(id='graph1'),style= {'height':'100%', 'padding': '10px'}),width=8
        )
    ],style={'margin':'10px'}),#Fim da linha 2

#linha 3

        dbc.Row([
            dbc.Col(dbc.Card(dcc.Graph(id='graph2'), style={'padding':'10px'}), width=6),
            dbc.Col(dbc.Card(dcc.Graph(id='graph3'), style={'padding':'10px'}), width=3),
            dbc.Col(dbc.Card(dcc.Graph(id='graph4'), style={'padding':'10px'}), width=3),
        ])



])


# =========  Callbacks  =========== #
