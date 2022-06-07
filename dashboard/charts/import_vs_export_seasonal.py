import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import util.constants as constants

df = pd.read_csv('../data/electricity_monthly.csv')
df = df[df['year'] >= 2010]
df['import_export_balance'] = df['import_export_balance']*-1
df['import_minus'] = df['import']*-1
df = df.groupby('year_season').sum()
df = df.reset_index(level=0)

df_summer = df[df['year_season'].str.startswith('Summer')]
df_winter = df[df['year_season'].str.startswith('Winter')]

summer_xaxis_vals = df_summer.iloc[::3, :].year_season
summer_xaxis_labels = summer_xaxis_vals.apply(lambda x: x[-4:])
winter_xaxis_vals = df_winter.iloc[::3, :].year_season
winter_xaxis_labels = winter_xaxis_vals.apply(lambda x: x[-9:-4] + x[-2:])

summer_bar_colors = df_summer['import_export_balance'].apply(lambda y: constants.EXPORT_COLOR if y >= 0 else constants.IMPORT_COLOR)
winter_bar_colors = df_winter['import_export_balance'].apply(lambda y: constants.EXPORT_COLOR if y >= 0 else constants.IMPORT_COLOR)

fig = make_subplots(1, 2, subplot_titles=['Winter Half Year', 'Summer Half Year'], shared_yaxes=True)
fig.add_trace(go.Bar(x=df_winter['year_season'], y=df_winter['import_export_balance'], name="Balance", marker=dict(color=winter_bar_colors), showlegend=False), 1, 1)
fig.add_trace(go.Bar(x=df_summer['year_season'], y=df_summer['import_export_balance'], name="Balance", marker=dict(color=summer_bar_colors), showlegend=False), 1, 2)

fig.update_layout(
    plot_bgcolor=constants.WHITE_COLOR,
    showlegend=True,
    legend_orientation='h',
    margin_b=10,
    margin_pad=10,
    separators=',\'',
    xaxis=dict(
        tickmode='array',
        tickvals=winter_xaxis_vals,
        ticktext=winter_xaxis_labels
    ),
    xaxis2=dict(
        tickmode='array',
        tickvals=summer_xaxis_vals,
        ticktext=summer_xaxis_labels
    )
)
fig.update_xaxes(
    showgrid=False,
    showline=False,
    color=constants.TICK_TEXT_COLOR
)
fig.update_yaxes(
    showgrid=True,
    ticksuffix=' GWh',
    tickformat=',.0f',
    gridcolor=constants.GRID_COLOR,
    showline=False,
    color=constants.TICK_TEXT_COLOR,
    range=[-10_000, 10_000]
)
