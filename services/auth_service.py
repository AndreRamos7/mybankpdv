from database.conexao import Conexao

class AuthService:

    @staticmethod
    def login(cpf, senha):

        con = Conexao()

        dados = con.consultar(
            '''
            SELECT * FROM clientes
            WHERE cpf = ? AND senha = ?
            ''',
            (cpf, senha)
        )

        if dados:
            return dados[0]

        return None
