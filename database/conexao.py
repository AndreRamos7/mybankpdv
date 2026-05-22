import sqlite3

class Conexao:

    def __init__(self):
        self.conn = sqlite3.connect('database/banco.db')
        self.cursor = self.conn.cursor()

    def executar(self, sql, params=()):
        self.cursor.execute(sql, params)
        self.conn.commit()

    def consultar(self, sql, params=()):
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()

    def fechar(self):
        self.conn.close()
