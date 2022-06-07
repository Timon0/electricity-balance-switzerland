import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import util.constants as constants

df = pd.read_csv('../data/electricity_monthly.csv')

df_summer = df.loc[(df['year'] == 2019) & (df['month'] >= 6) & (df['month'] <= 8)]
df_summer_avg = df_summer[['production_hydro', 'production_nuclear', 'production_therm_and_renewable']].mean()
df_summer_total_avg = round(df_summer[['production_total_netto']].mean()[0])

df_winter = df.loc[(df['year_month'] == '2018-12') | (df['year_month'] == '2019-01') | (df['year_month'] == '2019-02')]
df_winter_avg = df_winter[['production_hydro', 'production_nuclear', 'production_therm_and_renewable']].mean()
df_winter_total_avg = round(df_winter[['production_total_netto']].mean()[0])

labels = ['Hydro', 'Nuclear', 'Thermal and Renewables']
colors = [constants.HYDRO_COLOR, constants.NUCLEAR_COLOR, constants.THERM_AND_RENEWABLES_COLOR]

fig = make_subplots(1, 2, specs=[[{'type': 'domain'}, {'type': 'domain'}]],
                    subplot_titles=['Winter 2018/2019', 'Summer 2019'])
fig.add_trace(go.Pie(labels=labels, values=df_winter_avg, scalegroup='one', marker_colors=colors,
                     name='Winter 2018/2019', direction='clockwise', sort=True), 1, 1)
fig.add_trace(go.Pie(labels=labels, values=df_summer_avg, scalegroup='one', marker_colors=colors,
                     name='Summer 2019', direction='clockwise', sort=True), 1, 2)

fig.update_traces(hole=.4, hoverinfo='label+percent')
fig.update(layout_showlegend=True, layout_legend_orientation='h')
fig.add_annotation(
    dict(
        font=dict(color='black', size=18),
        x=0.225,
        y=0.5,
        textangle=0,
        align='center',
        xanchor='center',
        yanchor='middle',
        showarrow=False,
        text=f'<b>{df_winter_total_avg}<br>GWh<b>',
    )
)
fig.add_annotation(
    dict(
        font=dict(color='black', size=18),
        x=0.775,
        y=0.5,
        textangle=0,
        align='center',
        xanchor='center',
        yanchor='middle',
        showarrow=False,
        text=f'<b>{df_summer_total_avg}<br>GWh<b>',
    )
)
