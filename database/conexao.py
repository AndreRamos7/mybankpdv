import sqlite3

class Conexao:

    def __init__(self):
        self.conn = sqlite3.connect('database/banco.db')
        

    def executar(self, sql, params=()):
        self.cursor.execute(sql, params)

    def consultar(self, sql, params=()):
        self.cursor.execute(sql, params)
        return self.cursor.fetchone()

    def fechar(self):
        pass
        #self.conn.close()
