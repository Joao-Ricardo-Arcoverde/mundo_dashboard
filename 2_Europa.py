import streamlit as st
import plotly.express as px
import json
from Mundo import *

europa = mundo[mundo["continente"]=="Europe"]
europa_populosos = europa[europa["ano"]==2007].sort_values("pop", ascending=False)

st.set_page_config(page_title="Europa", page_icon="🇩🇪", layout="wide")

st.subheader("Europa")
st.markdown("""
            A Europa é um dos continentes que compõem o supercontinente Euroasiático.

            Ela é dividade entre:
            - Europa Ocidentals
            - Europa Oriental
            
            Seus principais países são: Alemanha, França, Itália, Espanha e Reino Unido.
            """)

st.divider()

fig13 = px.bar(
        europa_populosos,
        x="país",
        y="pop",
        color="pop",
        color_continuous_scale="blues",
        text_auto=True
    ).update_layout(title="Populações Europeias",
                        xaxis_title="Países",
                        yaxis_title="População",
                        legend_title="População",
                    template="plotly_white",hovermode="x").update_traces(hovertemplate=None)

fig14 = px.scatter(europa[europa["ano"]==2007],
                                 x="PIBpercap",
                                 y="ExpVida",
                                 color="país",
                                 size="pop",
                                 size_max=45,
                                 template="plotly_white",
                                 log_x=True,
                                 hover_data={"pop":False}
    ).update_layout(title="Indicadores Socioeconômicos Europeus",
                  xaxis_title = "PIB per Capita",
                  yaxis_title = "Expectativa de Vida").update_traces(hovertemplate=None)

col1, col2 = st.columns(2)

col1.plotly_chart(fig13)
col2.plotly_chart(fig14)
