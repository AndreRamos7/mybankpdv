from conexao import Conexao

con = Conexao()

con.executar('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cpf TEXT,
    senha TEXT,
    pix TEXT
)
''')

con.executar('''
CREATE TABLE IF NOT EXISTS contas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    saldo_corrente REAL,
    saldo_poupanca REAL
)
''')

con.executar('''
CREATE TABLE IF NOT EXISTS transacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    tipo TEXT,
    valor REAL,
    descricao TEXT,
    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

con.executar('''
INSERT INTO clientes(nome, cpf, senha, pix)
VALUES (?, ?, ?, ?)
''', ('João Silva', '11122233344', '1234', 'joao@pix'))

con.executar('''
INSERT INTO contas(cliente_id, saldo_corrente, saldo_poupanca)
VALUES (?, ?, ?)
''', (1, 10000, 5000))

print('Banco inicializado!')
