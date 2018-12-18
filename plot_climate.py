import plotly.graph_objs as go
from plotly.offline import plot

import pandas as pd


titleset = "Climat pendant des visites d'Achille à Skyros"

df = pd.read_csv('N:\Scripts\data_E.csv', sep=';')
df2 = pd.read_csv('N:\Scripts\data_W.csv', sep=';')


# graph

trace1 = go.Scatter(
    x=df['ISO time'],
    y=df['humidity avg'],
    name='UR-est',
    line=dict(
        color=('rgb(0, 0, 0)'),
        width=1,
        dash='dot'
        ),
    yaxis='y2'
    )

trace2 = go.Scatter(
    x=df['ISO time'],
    y=df['temperature avg'],
    name='Temp-est',
    line=dict(
        color=('rgb(0, 0, 0)'),
        width=1,
        ),
    yaxis='y1'
    )

trace3 = go.Scatter(
    x=df2['ISO time'],
    y=df2['humidity avg'],
    name='UR-ouest',
    line=dict(
        color=('rgb(169,169,169)'),
        width=1,
        dash='dot'
        ),
    yaxis='y2'
    )

trace4 = go.Scatter(
    x=df2['ISO time'],
    y=df2['temperature avg'],
    name='Temp-ouest',
    line=dict(
        color=('rgb(169,169,169)'),
        width=1,
        ),
    yaxis='y1'
    )


data = [trace1, trace2, trace3, trace4]
layout = go.Layout(
    title=titleset,
    legend=dict(
        x=1.1,
        orientation='v',
    ),
    xaxis=dict(
        title='Temps'
    ),
    yaxis=dict(
        title='Temperature (°C)',
        range=[0, 100],
    ),
    yaxis2=dict(
        title='Humidité relative (%)',
        range=[0, 100],
        overlaying='y',
        side='right',
    )
)

fig = go.Figure(data=data, layout=layout)

plot(fig)
