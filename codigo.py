# Título - Sistemas de vendas
# Seção cadastrar vendas
    #campo data
    #campo vendedor - Ana, Bruno, Carla
    #campo produto - notebook, fone, celular
    #campo quantidade 
    #campo vaor
    #botão cadastrar venda
        #quando eu clicar no botão -> adicionar a venda na tabela
# Seção Vendas cadastradas
    #tabela com as vendas
# Seção dashboard
    #card/métrica - > faturamento total
    #gráfico de barra/coluna -> venda por vendedor
    #gráfico de pizza -> venda por produto

#streamlit pandas plotly

import streamlit as st
import pandas as pd
import plotly.express as px

#carregar a base de vendas
tabela_vendas = pd.read_csv("vendas.csv")

st.write("# Sistema de vendas")

#seção de cadastro de vendas
st.sidebar.write("## Cadastrar vendas")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Fone", "Celular"])
quantidade = st.sidebar.number_input("Quantidade")
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadastrar Venda")

#lógica de cadastro
if botao_cadastrar:
    if valor == 0 or quantidade ==0 or vendedor =="":
        st.warning("Venda com erros de preenchimento")
    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    print(nova_venda)
    ultima_linha = len(tabela_vendas) 
    tabela_vendas.loc[ultima_linha] = nova_venda
    tabela_vendas.to_csv("vendas.csv", index=False)
    st.success("Venda cadastrada")

#seção de visualizar de vendas
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)

#seção de Dashboard
st.write("## Dashboard")

#card/métrica - > faturamento total
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento Total", f"R$ {faturamento}")

#gráfico de barra/coluna -> venda por vendedor
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico1)

#gráfico de pizza -> venda por produto
grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole= 0.5)
st.plotly_chart(grafico2)
