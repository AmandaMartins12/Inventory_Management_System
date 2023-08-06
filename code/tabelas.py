import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('estoque.db')
c = conn.cursor()

# Criação da tabela de produtos
c.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY,
        tipo TEXT,
        descricao TEXT,
        medida TEXT,
        estoque_minimo INTEGER,
        observacao TEXT
    )
''')

# Criação da tabela de fornecedores
c.execute('''
    CREATE TABLE IF NOT EXISTS fornecedores (
        id INTEGER PRIMARY KEY,
        fornecedor TEXT,
        cnpj TEXT,
        telefone TEXT,
        email TEXT,
        endereco TEXT
    )
''')

# Criação da tabela de obras
c.execute('''
    CREATE TABLE IF NOT EXISTS obras (
        id INTEGER PRIMARY KEY,
        obra TEXT,
        cnpj TEXT,
        endereco TEXT
    )
''')

# Criação da tabela de entrada de estoque
c.execute('''
    CREATE TABLE IF NOT EXISTS entrada_estoque (
        id INTEGER PRIMARY KEY,
        tipo_id INTEGER,
        produto_id INTEGER,
        ncm TEXT,
        valor_unit REAL,
        valor_total REAL,
        nota_fiscal TEXT,
        fornecedor_id INTEGER,
        cnpj_fornecedor TEXT,
        num_relatorio TEXT,
        data TEXT,
        observacao TEXT,
        anexos TEXT,
        FOREIGN KEY (tipo_id) REFERENCES produtos(id),
        FOREIGN KEY (produto_id) REFERENCES produtos(id),
        FOREIGN KEY (fornecedor_id) REFERENCES fornecedores(id)
    )
''')

# Criação da tabela de saída de estoque
c.execute('''
    CREATE TABLE IF NOT EXISTS saida_estoque (
        id INTEGER PRIMARY KEY,
        data TEXT,
        tipo_id INTEGER,
        produto_id INTEGER,
        ncm TEXT,
        valor_unit REAL,
        valor_total REAL,
        quantidade INTEGER,
        romaneio TEXT,
        destino_id INTEGER,
        observacao TEXT,
        anexos TEXT,
        FOREIGN KEY (tipo_id) REFERENCES produtos(id),
        FOREIGN KEY (produto_id) REFERENCES produtos(id),
        FOREIGN KEY (destino_id) REFERENCES obras(id)
    )
''')

# Commit e fechamento da conexão
conn.commit()
conn.close()
