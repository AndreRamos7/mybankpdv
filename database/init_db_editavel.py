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
''', ('Bill Gates', '33366699988', '1234', 'bill@pix'))

con.executar('''
INSERT INTO contas(cliente_id, saldo_corrente, saldo_poupanca)
VALUES (?, ?, ?)
''', (2, 1000, 15000))


con.executar('''
INSERT INTO clientes(nome, cpf, senha, pix)
VALUES (?, ?, ?, ?)
''', ('Jim Hopper', '12345678901', '1234', 'jim@pix'))

con.executar('''
INSERT INTO contas(cliente_id, saldo_corrente, saldo_poupanca)
VALUES (?, ?, ?)
''', (3, 500, 50000))

print('Banco atualizado!')
