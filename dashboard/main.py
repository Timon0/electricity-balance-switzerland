import streamlit as st

import charts.production_history as production_history_chart
import charts.production_seasonal as production_seasonal_chart
import charts.production_winter_vs_summer as production_winter_vs_summer_chart
import charts.import_vs_export as import_vs_export
import charts.import_vs_export_seasonal as import_vs_export_seasonal

st.set_page_config(page_title='Electricity Balance in Switzerland')

st.title('Electricity Balance in Switzerland')
st.markdown('''
    Analysis of the electricity balance in switzerland by **Timon Kurmann**.  
    This analysis is based on the publicly available data from the [Swiss Federal Office of Energy (SFOE)](https://www.bfe.admin.ch/bfe/de/home/versorgung/statistik-und-geodaten/energiestatistiken/elektrizitaetsstatistik.html).
''')

st.subheader('History')
st.markdown('''
    The production is composed of three distinct categories - hydro power, nuclear power and thermal & renewable energy. 
    Hydro power making up the biggest part of the production. Therefore Switzerland is relying heavily on it. Since 
    1960, when Switzerland started to record their electricity production and electricity consumption, in most years the 
    production was greater than the consumption. But in some years (e.g. 2005) Switzerland consumed more than they 
    produced. How is this possible?
''')

st.plotly_chart(
    production_history_chart.fig,
    use_container_width=True,
    config={'displayModeBar': False}
)

st.subheader('Seasonal Distribution')
st.markdown('''
    Taking a closer look at the distribution of the electricity consumption and the electricity production during winter
    and summer periods, interesting patterns show up: In winter the consumption is a lot greater than in summer and 
    vice versa the production.
''')

st.plotly_chart(
    production_seasonal_chart.fig,
    use_container_width=True,
    config={'displayModeBar': False}
)

st.subheader('Winter vs Summer Production Distribution')
st.markdown('''
    In summer 2019 Switzerland produced approximately 30% more than in winter 2018/2019. The greatest difference 
    being the production of hydro power. In summer there is more rainfall and the glaciers melt, thus
    the hydroelectric power plants can produce more electricity. To some extend the nuclear power plants can compensate
    this difference but not all of it.  
    The year 2018/2019 was chosen as an example, because it was the last year before the pandemic with non deviating
    values. 
''')

st.plotly_chart(
    production_winter_vs_summer_chart.fig,
    use_container_width=True,
    config={'displayModeBar': False}
)

st.subheader('Import vs Export')
st.markdown('''
    The extra electricity in summer can be exported and the lacking electricity in winter must be imported from
    Germany, France, Italy or Austria. This results in a positive balance most of the time, meaning that Switzerland
    exports more than they import. There are again a few exceptions, as we have already seen in the first chart 
    (e.g. 2005).
''')

st.plotly_chart(
    import_vs_export.fig,
    use_container_width=True,
    config={'displayModeBar': False}
)

st.subheader('Import vs Export Seasonal Balance')
st.markdown('''
    Looking at the import and export balance during the winter and summer half years, one can see that in nearly every
    year the winter balance was negative and the summer balance was positive (with one exception: Winter 2019/2020 the 
    start of the COVID pandemic). In other words, Switzerland does not produce enough electricity in winter and is
    consequently forced to import the remaining electricity that people have enough power available.
''')

st.plotly_chart(
    import_vs_export_seasonal.fig,
    use_container_width=True,
    config={'displayModeBar': False}
)


st.markdown('''
    In summary, the analysis shows that the electricity production in Switzerland depends heavily on hydro power. 
    Hydro power has one major disadvantage: It can not produce as much electricity in winter as it does in summer. 
    This forces Switzerland to import a lot electricity in winter, **making them severely dependent on foreign countries 
    during winter periods**.
''')
