import streamlit as st
import plotly.express as px
import json 
from Mundo import *

oceania = mundo[mundo["continente"]=="Oceania"]
oceania_populosos = oceania[oceania["ano"]==2007].sort_values("pop", ascending=False)

st.set_page_config(page_title="Oceania", page_icon="🇦🇺", layout="wide")

st.subheader("Oceania")
st.markdown("""
            A Oceania é um continente insular, composto por regiões da Ásia e da América.
            
            Ela é dividida entre:
            - Australásia
            - Melanésia
            - Micronésia
            - Polinésia
            
            Seus principais países são: Austrália e Nova Zelândia.
            """)
st.divider()

fig11 = px.bar(
        oceania_populosos,
        x="país",
        y="pop",
        color="pop",
        color_continuous_scale="reds",
        text_auto=True
    ).update_layout(title="Populações Oceania",
                        xaxis_title="Países",
                        yaxis_title="População",
                        legend_title="População",
                    template="plotly_white",hovermode="x").update_traces(hovertemplate=None)

fig12 = px.scatter(oceania[oceania["ano"]==2007],
                                 x="PIBpercap",
                                 y="ExpVida",
                                 color="país",
                                 size="pop",
                                 size_max=45,
                                 template="plotly_white",
                                 log_x=True,
                                 hover_data={"pop":False}
    ).update_layout(title="Indicadores Socioeconômicos Oceania",
                  xaxis_title = "PIB per Capita",
                  yaxis_title = "Expectativa de Vida").update_traces(hovertemplate=None)

col1, col2 = st.columns(2)

col1.plotly_chart(fig11)
col2.plotly_chart(fig12)
