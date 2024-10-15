import streamlit as st
import plotly.express as px
import json

from Mundo import *

americas = mundo[mundo["continente"]=="Americas"]
americas_populosos = americas[americas["ano"]==2007].sort_values("pop", ascending=False)

st.set_page_config(page_title="Americas", page_icon="🇧🇷", layout="wide")

st.subheader("Américas")
st.markdown("""
            As Américas são os continentes do hemisfério ocidental do planeta Terra.

            Elas são divididas em:
            - América do Norte
            - América Central
            - América do Sul

            Seus principais países são: Estados Unidos, Brasil, México, Argentina e Canadá.
            """)

st.divider()

fig5 = px.bar(
        americas_populosos,
        x="país",
        y="pop",
        color="pop",
        color_continuous_scale="greens",
        text_auto=True
    ).update_layout(title="Populações Americanas",
                        xaxis_title="Países",
                        yaxis_title="População",
                        legend_title="População",
                    template="plotly_white",
                    hovermode="x").update_traces(hovertemplate=None)

fig6 = px.scatter(americas[americas["ano"]==2007],
                                 x="PIBpercap",
                                 y="ExpVida",
                                 color="país",
                                 size="pop",
                                 size_max=45,
                                 template="plotly_white",
                                 log_x=True,
                                 hover_data={"pop":False}
    ).update_layout(title="Indicadores Socioeconômicos Americanos",
                  xaxis_title = "PIB per Capita",
                  yaxis_title = "Expectativa de Vida").update_traces(hovertemplate=None)  

col1, col2 = st.columns(2)

col1.plotly_chart(fig5)
col2.plotly_chart(fig6)
