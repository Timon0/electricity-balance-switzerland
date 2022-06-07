import pandas as pd
import plotly.graph_objects as go
import util.constants as constants

df = pd.read_csv('../data/electricity_yearly_with_population.csv')
df['import_minus'] = df['import']*-1
df['import_export_balance'] = df['import_export_balance']*-1

electricity_export = {
    'name': 'Export',
    'type': 'bar',
    'x': df['year'],
    'y': df['export'],
    'marker': {
        'color': constants.EXPORT_COLOR
    },
}

electricity_import = {
    'name': 'Import',
    'type': 'bar',
    'x': df['year'],
    'y': df['import_minus'],
    'marker': {
        'color': constants.IMPORT_COLOR
    },
}

balance = {
    'name': 'Balance',
    'x': df['year'],
    'y': df['import_export_balance'],
    'mode': 'lines',
    'line_color': constants.BLACK_COLOR,
    'line': {
        'width': 3
    },
    'showlegend': False
}

layout = {
    'plot_bgcolor': constants.WHITE_COLOR,
    'showlegend': True,
    'legend': {
        'orientation': 'h'
    },
    'barmode': 'relative',
    'margin': {
        'r': 150,
        'b': 10,
        'pad': 10
    },
    'xaxis': {
        'showgrid': False,
        'showline': False,
        'color': constants.TICK_TEXT_COLOR
    },
    'yaxis': {
        'showgrid': True,
        'ticksuffix': ' GWh',
        'tickformat': ',.0f',
        'gridcolor': constants.GRID_COLOR,
        'showline': False,
        'color': constants.TICK_TEXT_COLOR
    },
    'separators': ',\''
}

figdict = {
    'data': [electricity_export, electricity_import, balance],
    'layout': layout
}

fig = go.Figure(figdict)

fig.add_annotation(
    dict(
        font=dict(color="black", size=14),
        x=1,
        y=df.import_export_balance.iloc[-1],
        textangle=0,
        xanchor='left',
        showarrow=False,
        text='<b>Balance</b>',
        yshift=2,
        xref='paper'
    )
)
