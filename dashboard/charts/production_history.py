import pandas as pd
import plotly.graph_objects as go

import util.constants as constants

df = pd.read_csv('../data/electricity_yearly_with_population.csv')

therm_and_renewables = {
    'name': 'Thermal and Renewables',
    'x': df['year'],
    'y': df['production_therm_and_renewable'],
    'hoverinfo': 'x+y',
    'mode': 'lines',
    'stackgroup': 'production',
    'line_color': constants.THERM_AND_RENEWABLES_COLOR,
    'fillcolor': constants.THERM_AND_RENEWABLES_COLOR
}
nuclear = {
    'name': 'Nuclear',
    'x': df['year'],
    'y': df['production_nuclear'],
    'hoverinfo': 'x+y',
    'mode': 'lines',
    'stackgroup': 'production',
    'line_color': constants.NUCLEAR_COLOR,
    'fillcolor': constants.NUCLEAR_COLOR
}
hydro = {
    'name': 'Hydro',
    'x': df['year'],
    'y': df['production_hydro'] - df['production_hydro_losses'],
    'hoverinfo': 'x+y',
    'mode': 'lines',
    'stackgroup': 'production',
    'line_color': constants.HYDRO_COLOR,
    'fillcolor': constants.HYDRO_COLOR
}
min_production_or_consumption = {
    'name': 'Total Production',
    'x': df['year'],
    'y': df[['production_total_netto', 'consumption_country']].min(axis=1),
    'mode': 'lines',
    'line': {
        'width': 0
    },
    'showlegend': False,
    'hoverinfo': 'skip'
}

consumption_hidden = {
    'name': 'Consumption hidden',
    'x': df['year'],
    'y': df['consumption_country'],
    'mode': 'lines',
    'line': {
        'width': 0
    },
    'showlegend': False,
    'hoverinfo': 'skip',
    'fill': 'tonexty',
    'fillcolor': constants.TICK_TEXT_COLOR
}

consumption = {
    'name': 'Consumption',
    'x': df['year'],
    'y': df['consumption_country'],
    'mode': 'lines',
    'line_color': constants.BLACK_COLOR,
    'line': {
        'width': 3
    },
    'showlegend': False,
}

layout = {
    'plot_bgcolor': constants.WHITE_COLOR,
    'showlegend': True,
    'legend': {
        'orientation': 'h'
    },
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
        'color':  constants.TICK_TEXT_COLOR
    },
    'separators': ',\''
}

figdict = {
    'data': [consumption_hidden, therm_and_renewables, nuclear, hydro, consumption],
    'layout': layout
}

fig = go.Figure(figdict)
more_consumed_than_produced_y = (df.loc[df.year == 2005, 'production_total_netto'].values[0] + df.loc[df.year == 2005, 'consumption_country'].values[0])/2
fig.add_annotation(
    dict(
        font=dict(color=constants.BLACK_COLOR, size=12),
        x=2005,
        y=more_consumed_than_produced_y,
        xanchor='center',
        showarrow=True,
        text='more consumed<br> than produced',
        ay=-70
    )
)
fig.add_annotation(
    dict(
        font=dict(color=constants.BLACK_COLOR, size=14),
        x=1,
        y=df.consumption_country.iloc[-1],
        textangle=0,
        xanchor='left',
        showarrow=False,
        text='<b>Total consumption</b>',
        yshift=2,
        xref='paper'
    )
)

