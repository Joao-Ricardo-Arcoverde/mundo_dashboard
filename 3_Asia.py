import streamlit as st
import plotly.express as px
import json
mundo = px.data.gapminder().rename(columns={"country":"país",
                              "continent":"continente",
                              "year":"ano",
                               "lifeExp":"ExpVida",
                               "pop":"pop",
                               "gdpPercap":"PIBpercap",
                               "iso_alpha":"sigla",
                                "iso_num":"num_sigla",
                                 })
asia = mundo[mundo["continente"]=="Asia"]
asia_populosos = asia[asia["ano"]==2007].sort_values("pop", ascending=False)

st.set_page_config(page_title="Asia", page_icon="🇯🇵", layout="wide")

st.subheader("Ásia")
st.markdown("""
            A Ásia é o maior dos continentes, tanto em área como em população.
            
            Ela é dividida entre:
            - Ásia Central
            - Ásia Oriental
            - Ásia Meridional
            - Ásia Ocidental
            - Sudeste Asiático
            
            Seus principais países são: China, Índia, Indonésia, Paquistão e Bangladesh.
            """)
st.divider()

fig7 = px.bar(
        asia_populosos,
        x="país",
        y="pop",
        color="pop",
        color_continuous_scale="purples",
        text_auto=True
    ).update_layout(title="Populações Asiáticas",
                        xaxis_title="Países",
                        yaxis_title="População",
                        legend_title="População",
                    template="plotly_white",hovermode="x").update_traces(hovertemplate=None)

fig8 = px.scatter(asia[asia["ano"]==2007],
                                 x="PIBpercap",
                                 y="ExpVida",
                                 color="país",
                                 size="pop",
                                 size_max=45,
                                 template="plotly_white",
                                 log_x=True,
                                 hover_data={"pop":False}
    ).update_layout(title="Indicadores Socioeconômicos Mundiais Asiáticos",
                  xaxis_title = "PIB per Capita",
                  yaxis_title = "Expectativa de Vida").update_traces(hovertemplate=None)

col1, col2 = st.columns(2)

col1.plotly_chart(fig7)
col2.plotly_chart(fig8)
