import streamlit as st
import sqlite3
from datetime import datetime

# Conexão com o banco de dados
conn = sqlite3.connect('estoque.db')
c = conn.cursor()

# Função para cadastrar produtos, fornecedores e obras
def cadastrar_item(tabela, valores):
    query = f"INSERT INTO {tabela} VALUES ({', '.join(['?'] * len(valores))})"
    c.execute(query, valores)
    conn.commit()

# Função para registrar entrada de estoque...
def registrar_entrada(id_produto, tipo, descricao, ncm, valor_unitario, valor_total, nota_fiscal, cnpj_fornecedor,
                      num_relatorio, data, observacao):
    c.execute("INSERT INTO entrada_estoque (id_produto, tipo, descricao, ncm, valor_unitario, valor_total, nota_fiscal, cnpj_fornecedor, num_relatorio, data, observacao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
              (id_produto, tipo, descricao, ncm, valor_unitario, valor_total, nota_fiscal, cnpj_fornecedor, num_relatorio, data, observacao))
    conn.commit()

# Função para registrar saída de estoque...
def registrar_saida(id_produto, tipo, descricao, ncm, valor_unitario, valor_total, quantidade, romaneio, destino,
                    observacao):
    c.execute("INSERT INTO saida_estoque (id_produto, tipo, descricao, ncm, valor_unitario, valor_total, quantidade, romaneio, destino, observacao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
              (id_produto, tipo, descricao, ncm, valor_unitario, valor_total, quantidade, romaneio, destino, observacao))
    conn.commit()

# Título da aplicação
st.title("Sistema de Gerenciamento de Estoque")

# Menu de seleção de páginas
escolha = st.sidebar.selectbox("Escolha uma opção:",
                               ["Home","Cadastro de Produto", "Cadastro de Fornecedor", "Cadastro de Obra", "Entrada de Estoque", "Saída de Estoque", "Dashboard"])
# Home
if escolha == "Home":
    st.write("Bem-vindo ao Sistema de Gerenciamento de Estoque. Selecione uma opção no menu lateral:")

# Página de cadastro de produtos
if escolha == "Cadastro de Produto":
    st.header("Cadastro de Produto")

    # Layout de colunas para organizar os campos de cadastro e a tabela
    col1, col2 = st.columns(2)

    # Coluna 1: Campos de cadastro
    with col1:
        tipo = st.text_input("Tipo")
        descricao = st.text_input("Descrição do Produto")
        medida = st.text_input("Medida")
        estoque_minimo = st.number_input("Estoque Mínimo", min_value=0)
        observacao = st.text_input("Observação")
        if st.button("Cadastrar Produto"):
            c.execute("INSERT INTO produtos (tipo, descricao, medida, estoque_minimo, observacao) VALUES (?, ?, ?, ?, ?)", 
                      (tipo, descricao, medida, estoque_minimo, observacao))
            conn.commit()
            st.success("Produto cadastrado com sucesso!")

    # Coluna 2: Tabela de visualização
    with col2:
        if st.button("Visualizar Tabela de Produtos"):
            result = c.execute("SELECT * FROM produtos").fetchall()
            st.table(result)

# Página de cadastro de fornecedores
if escolha == "Cadastro de Fornecedor":
    st.header("Cadastro de Fornecedor")

    # Layout de colunas para organizar os campos de cadastro e a tabela
    col1, col2 = st.columns(2)

    # Coluna 1: Campos de cadastro
    with col1:
        fornecedor = st.text_input("Fornecedor")
        cnpj = st.text_input("CNPJ")
        telefone = st.text_input("Telefone")
        email = st.text_input("E-mail")
        endereco = st.text_input("Endereço")
        if st.button("Cadastrar Fornecedor"):
            c.execute("INSERT INTO fornecedores (fornecedor, cnpj, telefone, email, endereco) VALUES (?, ?, ?, ?, ?)", 
                      (fornecedor, cnpj, telefone, email, endereco))
            conn.commit()
            st.success("Fornecedor cadastrado com sucesso!")
    
    # Coluna 2: Tabela de visualização
    with col2:
        if st.button("Visualizar Tabela de Fornecedores"):
            result = c.execute("SELECT * FROM fornecedores").fetchall()
            st.table(result)

# Página de cadastro de obras
if escolha == "Cadastro de Obra":
    st.header("Cadastro de Obra")

    # Layout de colunas para organizar os campos de cadastro e a tabela
    col1, col2 = st.columns(2)

    # Coluna 1: Campos de cadastro
    with col1:
        id = st.text_input("ID")
        obra = st.text_input("Obra")
        cnpj_obra = st.text_input("CNPJ")
        endereco_obra = st.text_input("Endereço da Obra")
        if st.button("Cadastrar Obra"):
            c.execute("INSERT INTO obras (id, obra, cnpj, endereco) VALUES (?, ?, ?)", 
                      (id, obra, cnpj_obra, endereco_obra))
            conn.commit()
            st.success("Obra cadastrada com sucesso!")

    # Coluna 2: Tabela de visualização
    with col2:
        if st.button("Visualizar Tabela de Obras"):
            result = c.execute("SELECT * FROM obras").fetchall()
            st.table(result)

# Página de entrada de estoque
if escolha == "Entrada de Estoque":
    st.header("Entrada de Estoque")

    # Layout de colunas para organizar os campos de entrada
    col1, col2 = st.columns(2)

    # Coluna 1: Campos de entrada
    with col1:
        id_produto = st.text_input("ID")
        tipo_entrada = st.text_input("Tipo")
        descricao_entrada = st.text_input("Descrição do Produto")
        ncm_entrada = st.text_input("NCM")
        valor_unitario_entrada = st.text_input("Valor Unit.")
        valor_total_entrada = st.text_input("Valor Total")
        nota_fiscal_entrada = st.text_input("Nota Fiscal")
        cnpj_fornecedor_entrada = st.text_input("CNPJ Fornecedor")
        num_relatorio_entrada = st.text_input("Num. Relatório")
        data_entrada = st.text_input("Data")
        observacao_entrada = st.text_input("Observação")
        # ... outros campos de entrada ...
        if st.button("Registrar Entrada"):
            # Chame a função de registro de entrada
            registrar_entrada(id_produto, tipo_entrada, descricao_entrada, ncm_entrada, valor_unitario_entrada,
                              valor_total_entrada, nota_fiscal_entrada, cnpj_fornecedor_entrada, num_relatorio_entrada,
                              data_entrada, observacao_entrada)
            st.success("Entrada registrada com sucesso!")

    # Botão para visualizar a tabela de entrada
    if st.button("Visualizar Tabela de Entrada"):
        result = c.execute("SELECT * FROM entrada_estoque").fetchall()
        st.table(result)

# Página de saída de estoque
if escolha == "Saída de Estoque":
    st.header("Saída de Estoque")

    # Layout de colunas para organizar os campos de saída
    col1, col2 = st.columns(2)

    # Coluna 1: Campos de saída
    with col1:
        id_produto = st.text_input("ID")
        tipo_saida = st.text_input("Tipo de Saída")
        descricao_saida = st.text_input("Descrição do Produto")
        ncm_saida = st.text_input("NCM")
        valor_unitario_saida = st.text_input("Valor Unit.")
        valor_total_saida = st.text_input("Valor Total")
        quantidade_saida = st.text_input("Quantidade")
        romaneio_saida = st.text_input("Romaneio")
        destino_saida = st.text_input("Destino")
        observacao_saida = st.text_input("Observação")
        # ... outros campos de saída ...
        if st.button("Registrar Saída"):
            # Chame a função de registro de saída
            registrar_saida(id_produto, tipo_saida, descricao_saida, ncm_saida, valor_unitario_saida,
                            valor_total_saida, quantidade_saida, romaneio_saida, destino_saida, observacao_saida)
            st.success("Saída registrada com sucesso!")

# Botão para visualizar a tabela de saída
    if st.button("Visualizar Tabela de Saída"):
        result = c.execute("SELECT * FROM saida_estoque").fetchall()
        st.table(result)

# Página de dashboard
if escolha == "Dashboard":
    st.header("Dashboard")
    # Interface para visualização dos dados do estoque e alertas
    
# Fechando a conexão com o banco de dados
conn.close()