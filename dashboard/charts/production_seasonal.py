import pandas as pd
import plotly.graph_objects as go

import util.constants as constants

month_map = {
    1: 'Jan.',
    2: 'Feb.',
    3: 'Mar.',
    4: 'Apr.',
    5: 'May.',
    6: 'Jun.',
    7: 'Jul.',
    8: 'Aug.',
    9: 'Sept.',
    10: 'Oct.',
    11: 'Nov.',
    12: 'Dec.'
}

df = pd.read_csv('../data/electricity_monthly.csv')
df = df.loc[(df['year_month'] >= '2016-04') & (df['year_month'] < '2019-10')]
df['month'] = df['month'].apply(lambda x: month_map.get(x))

production_therm_and_renewable = {
    'name': 'Thermal and Renewables',
    'type': 'bar',
    'x': [df['year_season'], df['month']],
    'y': df['production_therm_and_renewable'],
    'marker': {
        'color': constants.THERM_AND_RENEWABLES_COLOR,
        'line': {
            'color': constants.THERM_AND_RENEWABLES_COLOR
        }
    }
}

production_nuclear = {
    'name': 'Nuclear',
    'type': 'bar',
    'x': [df['year_season'], df['month']],
    'y': df['production_nuclear'],
    'marker': {
        'color': constants.NUCLEAR_COLOR,
        'line': {
            'color': constants.NUCLEAR_COLOR
        }
    }
}

production_hydro = {
    'name': 'Hydro',
    'type': 'bar',
    'x': [df['year_season'], df['month']],
    'y': df['production_hydro'] - df['production_hydro_losses'],
    'marker': {
        'color': constants.HYDRO_COLOR,
        'line': {
            'color': constants.HYDRO_COLOR
        }
    }
}

consumption = {
    'name': 'Consumption',
    'x': [df['year_season'], df['month']],
    'y': df['consumption_country'],
    'mode': 'lines',
    'line_color': constants.BLACK_COLOR,
    'line': {
        'width': 3
    },
    'showlegend': False
}

layout = {
    'barmode': 'stack',
    'plot_bgcolor': '#ffffff',
    'showlegend': True,
    'legend': {
        'orientation': 'h',
        'y': -0.4,

    },
    'margin': {
        'r': 150
    },
    'xaxis': {
        'showgrid': False,
        'showline': False,
        'color': constants.TICK_TEXT_COLOR,
        'dividercolor': constants.GRID_COLOR

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
    'data': [consumption, production_therm_and_renewable, production_nuclear, production_hydro],
    'layout': layout
}

fig = go.Figure(**figdict)
fig.add_annotation(
    dict(
        font=dict(color="black", size=14),
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
