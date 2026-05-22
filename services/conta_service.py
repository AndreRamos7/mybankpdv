from database.conexao import Conexao

class ContaService:

    @staticmethod
    def obter_saldos(cliente_id):

        con = Conexao()

        dados = con.consultar(
            '''
            SELECT saldoCorente, saldo_poupanca
            FROM contas
            WHERE cliente_id = ?
            ''',
            (cliente_id,)
        )

        

        return dados[0]

    @staticmethod
    def extrato(cliente_id):

        con = Conexao()

        dados = con.consultar(
            '''
            SELECT tipo, valor, descricao, data
            FROM transacoes
            WHERE cliente_id = ?
            ORDER BY data DESC
            ''',
            (cliente_id,)
        )

        

        return dados

    @staticmethod
    def sacar(cliente_id, valor):

        con = Conexao()

        saldo = con.consultar(
            '''
            SELECT saldo_corrente
            FROM contas
            WHERE cliente_id = ?
            ''',
            (cliente_id,)
        )[0][0]

        if saldo >= valor + 37:

            novo = saldo - valor

            con.executar(
                '''
                UPDATE contas
                SET saldo_corrente = ?
                WHERE cliente_id = ?
                ''',
                (novo, cliente_id)
            )

            con.executar(
                '''
                INSERT INTO transacoes(cliente_id, tipo, valor, descricao)
                VALUES (?, ?, ?, ?)
                ''',
                (
                    cliente_id,
                    'SAQUE',
                    valor,
                    'Saque em terminal'
                )
            )

            
            return True

        
        return False
