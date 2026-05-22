from database.conexao import Conexao
from PyQt6.QtWidgets import *

class PixService(QPushButton):

    @staticmethod
    def transferir(cliente_id, chave_pix, valor):

        con = Conexao()

        destino = con.consultar(
            '''
            SELECT id, pix
            FROM clientes
            WHERE pix = ?
            ''',
            (chave_pix,)
        )
        if destino[0][0] == cliente_id:
            
            return 'MESMA_CONTA'

        if not destino:
            
            return False

        destino_id = destino[0][0]

        saldo = con.consultar(
            '''
            SELECT saldo_corrente
            FROM contas
            WHERE cliente_id = ?
            ''',
            (cliente_id,)
        )[0][0]

        if saldo < valor:
            
            return False

        x = con.consultar(
            '''
            SELECT saldo_corrente
            FROM contas
            WHERE cliente_id = ?
            ''',
            (destino_id,)
        )[0][0]

        con.executar(
            '''
            UPDATE contas
            SET saldo_corrente = ?
            WHERE cliente_id = ?
            ''',
            (saldo - valor, 1)
        )

        con.executar(
            '''
            UPDATE contas
            SET saldo_corrente = ?
            WHERE cliente_id = ?
            ''',
            (x + valor, destino_id)
        )

        con.executar(
            '''
            INSERT INTO transacoes(cliente_id, tipo, valor, descricao)
            VALUES (?, ?, ?, ?)
            ''',
            (
                cliente_id,
                'PIX ENVIADO',
                valor,
                f'Enviado para {chave_pix}'
            )
        )

        con.executar(
            '''
            INSERT INTO transacoes(cliente_id, tipo, valor, descricao)
            VALUES (?, ?, ?, ?)
            ''',
            (
                destino_id,
                'PIX RECEBIDO',
                valor,
                f'Recebido de transferência PIX'
            )
        )

        

        return True
