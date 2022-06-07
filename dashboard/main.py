import streamlit as st

import charts.production_history as production_history_chart
import charts.production_seasonal as production_seasonal_chart
import charts.production_winter_vs_summer as production_winter_vs_summer_chart
import charts.import_vs_export as import_vs_export
import charts.import_vs_export_seasonal as import_vs_export_seasonal


st.set_page_config(page_title='Electricity Balance in Switzerland')
st.title('Electricity Balance in Switzerland')

st.text('')
st.text('')

st.subheader('Production History')


st.plotly_chart(
    production_history_chart.fig,
    config={'displayModeBar': False}
)


st.subheader('Seasonal Production History')


st.plotly_chart(
    production_seasonal_chart.fig,
    config={'displayModeBar': False}
)

st.subheader('Winter vs Summer production')


st.plotly_chart(
    production_winter_vs_summer_chart.fig,
    config={'displayModeBar': False}
)

st.subheader('Import vs Export History')


st.plotly_chart(
    import_vs_export.fig,
    config={'displayModeBar': False}
)

st.subheader('Import vs Export Seasonal Balance')


st.plotly_chart(
    import_vs_export_seasonal.fig,
    config={'displayModeBar': False}
)