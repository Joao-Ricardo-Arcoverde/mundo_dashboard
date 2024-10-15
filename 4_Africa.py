import streamlit as st
import plotly.express as px
import json
from Mundo import *

africa = mundo[mundo["continente"]=="Africa"]
africa_populosos = africa[africa["ano"]==2007].sort_values("pop", ascending=False)

st.set_page_config(page_title="Africa", page_icon="🇿🇦", layout="wide")

st.subheader("África")
st.markdown("""
            A África é o terceiro continente mais extenso, depois da Ásia e da América.
            
            Ela é dividida entre:
            - África Setentrional
            - África Ocidental
            - África Central
            - África Oriental
            - África Austral
            
            Seus principais países são: África do Sul, Nigéria, Etiópia, Egito e República Democrática do Congo.
            """)

st.divider()

fig9 = px.bar(
        africa_populosos,
        x="país",
        y="pop",
        color="pop",
        color_continuous_scale="oranges",
        text_auto=True
    ).update_layout(title="Populações Africanas",
                        xaxis_title="Países",
                        yaxis_title="População",
                        legend_title="População",
                    template="plotly_white",hovermode="x").update_traces(hovertemplate=None)

fig10 = px.scatter(africa[africa["ano"]==2007],
                                 x="PIBpercap",
                                 y="ExpVida",
                                 color="país",
                                 size="pop",
                                 size_max=45,
                                 template="plotly_white",
                                 log_x=True,
                                 hover_data={"pop":False}
    ).update_layout(title="Indicadores Socioeconômicos Africanos",
                  xaxis_title = "PIB per Capita",
                  yaxis_title = "Expectativa de Vida").update_traces(hovertemplate=None)

col1, col2 = st.columns(2)
col1.plotly_chart(fig9)
col2.plotly_chart(fig10)
