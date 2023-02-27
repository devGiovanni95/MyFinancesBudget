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


    ])
])


# =========  Callbacks  =========== #
