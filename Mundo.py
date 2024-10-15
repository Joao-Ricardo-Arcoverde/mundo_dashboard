import streamlit as st
import plotly.express as px
import json
import numpy as np

# Dashboard Mundo

st.set_page_config(page_title="Mundo", page_icon="🌍", layout="wide")


st.sidebar.markdown("Desenvolvido por [João Ricardo](https://github.com/Joao-Ricardo-Arcoverde)")
st.sidebar.markdown("Documentação [Streamlit](https://docs.streamlit.io/library/api-reference)")
st.sidebar.markdown("Documentação [Plotly](https://plotly.com/python/)")


st.title("Dashboard Mundo")

st.subheader("Introdução")

st.markdown("""
        Este é um dashboard interativo que nos
         apresenta informações sobre os **continentes do mundo**, como população, PIB per capita, expectativa de vida, etc. 
         
        Com ele poderemos observar as principais características de cada continente e comparar os dados entre eles.
            
         Use o menu lateral para navegar entre as páginas e
         explorar as principais informações de cada continente!
            """)

st.divider()


linhas_territoriais = json.load(open("world-countries.json",'r'))
mundo = px.data.gapminder().rename(columns={"country":"país",
                              "continent":"continente",
                              "year":"ano",
                               "lifeExp":"ExpVida",
                               "pop":"pop",
                               "gdpPercap":"PIBpercap",
                               "iso_alpha":"sigla",
                                "iso_num":"num_sigla",
                                 })

contintente_escolhido = st.multiselect("Seleção de continente(s)",
                   mundo["continente"].unique(),
                   mundo["continente"].unique())

# DADOS
mundo_escolhido = mundo[(mundo["continente"].isin(contintente_escolhido))]
## PEGANDO O PAÍS MAIS POPULOSO E SUA QUANTIDADE
país_mais_populoso = mundo_escolhido.loc[mundo_escolhido['pop'].idxmax()]["país"]
população_país_mais_populoso = mundo_escolhido[mundo_escolhido["ano"]==2007]["pop"].max()

## PEGANDO O MAIS LONGEVO E SUA QUANTIDADE
país_mais_longevo = mundo_escolhido.loc[mundo_escolhido['ExpVida'].idxmax()]["país"]
anos_mais_longevo = mundo_escolhido[mundo_escolhido["ano"]==2007]["ExpVida"].max()

## PEGANDO O MAIS RICO E SUA QUANTIDADE
país_mais_rico = mundo.loc[mundo_escolhido['PIBpercap'].idxmax()]["país"]
qtd_mais_rico = mundo_escolhido[mundo_escolhido["ano"]==2007]["PIBpercap"].max()

## PEGANDO UMA LISTA DOS 5 MAIS POPULOSOS E FAZENDO UM DF DELES
lista_paises_mais_populosos = mundo_escolhido[mundo_escolhido["ano"]==2007].sort_values(by="pop", ascending=False).reset_index().head(5)["país"].unique()
df_paises_mais_populosos = mundo_escolhido[mundo_escolhido["país"].isin(lista_paises_mais_populosos)]

## PEGANDO UMA LISTA DOS 5 MAIS RICOS E FAZENDO UM DF DELES
lista_paises_mais_ricos = mundo_escolhido[mundo_escolhido["ano"]==2007].sort_values(by="PIBpercap", ascending=False).reset_index().head(5)["país"].unique()
df_paises_mais_ricos = mundo_escolhido[mundo_escolhido["país"].isin(lista_paises_mais_ricos)]

## PEGANDO UMA LISTA DOS 5 MAIS LONGEVOS E FAZENDO UM DF DELES
lista_paises_mais_longevos = mundo_escolhido[mundo_escolhido["ano"]==2007].sort_values(by="ExpVida", ascending=False).reset_index().head(5)["país"].unique()
df_paises_mais_longevos = mundo_escolhido[mundo_escolhido["país"].isin(lista_paises_mais_longevos)]

## CRIANDO UM DF PARA APRESENTAR NO ST.DATAFRAME()
dados_df = mundo_escolhido[mundo_escolhido["ano"]==2007].drop(columns=["sigla","num_sigla","ano"])

fig1 = px.choropleth_mapbox(mundo_escolhido,
                     geojson=linhas_territoriais,
                     locations="sigla",
                     color=mundo_escolhido.select_dtypes(include=[np.number]).apply(np.log10)["pop"],
                     color_continuous_scale="blues",
                     mapbox_style="carto-positron",
                     zoom=1.1,
                     opacity=0.8,
                     width=1150,
                     height=700,
                     center={"lat":20, "lon":0},
        hover_data = {"país":True,"pop":True}).update_layout(title="Mapa-múndi",
                    xaxis_title="Longitude",
                    yaxis_title="Latitude",
                    legend_title="População",
                    coloraxis_showscale=False,
                    mapbox_pitch = 10,
                    mapbox_bearing = 0)

fig2 = px.line(df_paises_mais_populosos,
                                 x="ano",
                                 y="pop",
                                 color="país",
                                 log_y=True,
                                 width=400).update_layout(hovermode="x",
                                                           title="Crescimento populacional",
                                                           xaxis_title="Ano",
                                                           yaxis_title="População").update_traces(hovertemplate=None,line_shape ="spline")

fig3 = px.line(df_paises_mais_ricos,
                                 x="ano",
                                 y="PIBpercap",
                                 color="país",
                                 log_y=True,
                                 width=400).update_layout(hovermode="x",
                                                           title="Desenvolvimento econômico",
                                                           xaxis_title="Ano",
                                                           yaxis_title="PIB per Capita").update_traces(hovertemplate=None,line_shape ="spline")

fig4 = px.line(df_paises_mais_longevos,
                                 x="ano",
                                 y="ExpVida",
                                 color="país",
                                 log_y=True,
                                 width=400).update_layout(hovermode="x",
                                                           title="Evolução da expectativa de vida",
                                                           xaxis_title="Ano",
                                                           yaxis_title="Expectativa de Vida").update_traces(hovertemplate=None,line_shape ="spline")

fig5 = px.scatter(mundo[mundo["ano"]==2007],
                                 x="PIBpercap",
                                 y="ExpVida",
                                 color="país",
                                 size="pop",
                                 size_max=45,
                                 template="plotly_white",
                                 log_x=True,
                                 hover_data={"pop":False}
    ).update_layout(title="Gráfico de Bolhas - Indicadores Socioeconômicos Mundiais",
                  xaxis_title = "PIB per Capita",
                  yaxis_title = "Expectativa de Vida")
container1 = st.container(border=True)

col1, col2, col3 = container1.columns(spec = 3, gap="small" )

col1.metric(label="País Mais Populoso", value=país_mais_populoso)
col1.metric(label="População", value=f"{população_país_mais_populoso:,.0f}")
col2.metric(label="País Mais Longevo", value=país_mais_longevo)
col2.metric(label="Longevidade", value=f"{anos_mais_longevo:,.0f} anos")
col3.metric(label="País Mais Rico", value=país_mais_rico)
col3.metric(label="PIB per Capita", value=f"${qtd_mais_rico:,.0f} por habitante")

st.plotly_chart(fig1)

col4, col5, col6 = st.columns(3)
col4.plotly_chart(fig2)
col5.plotly_chart(fig3)
col6.plotly_chart(fig4)
