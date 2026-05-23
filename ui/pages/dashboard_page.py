from PyQt6.QtWidgets import *
from services.conta_service import ContaService
from services.pix_service import PixService
from ui.components.menu_button import MenuButton
from ui.dialogs.input_dialog import InputDialog
from ui.dialogs.alert_dialog import AlertDialog

class DashboardPage(QWidget):

    def __init__(self, main_window, usuario):
        super().__init__()

        self.main_window = main_window
        self.usuario = usuario
        self.cliente_id = usuario[0]

        self.setStyleSheet(
            'background: #111827;'
        )

        layout = QVBoxLayout()

        titulo = QLabel(
            f'Bem-vindo, {usuario[1]}'
        )

        titulo.setStyleSheet('''
            color: white;
            font-size: 34px;
            font-weight: bold;
            padding: 20px;
        ''')

        saldos = ContaService.obter_saldos(
            self.cliente_id
        )

        self.lbl_corrente = QLabel(
            f'Saldo Corrente: R$ {saldos[0]:.2f}'
        )

        self.lbl_poupanca = QLabel(
            f'Saldo Poupança: R$ {saldos[1]:.2f}'
        )

        for lbl in [
            self.lbl_corrente,
            self.lbl_poupanca
        ]:

            lbl.setStyleSheet('''
                color: white;
                font-size: 28px;
            ''')

        grid = QGridLayout()

        btn_extrato = MenuButton(
            'EXTRATO',
            '#2563eb'
        )

        btn_pix = MenuButton(
            'PIX',
            '#9333ea'
        )

        btn_saque = MenuButton(
            'SAQUE',
            '#dc2626'
        )

        btn_logout = MenuButton(
            'ENCERRAR',
            '#475569'
        )

        btn_extrato.clicked.connect(
            self.mostrar_extrato
        )

        btn_pix.clicked.connect(
            self.realizar_pix
        )

        btn_saque.clicked.connect(
            self.realizar_saque
        )

        btn_logout.clicked.connect(
            self.main_window.voltar_login
        )

        grid.addWidget(btn_extrato, 0, 0)
        grid.addWidget(btn_pix, 0, 1)
        grid.addWidget(btn_saque, 1, 0)
        grid.addWidget(btn_logout, 1, 1)

        self.area = QTextEdit()

        self.area.setReadOnly(True)

        self.area.setStyleSheet('''
            background: white;
            border-radius: 15px;
            font-size: 18px;
            padding: 15px;
        ''')

        layout.addWidget(titulo)
        layout.addWidget(self.lbl_corrente)
        layout.addWidget(self.lbl_poupanca)
        layout.addLayout(grid)
        layout.addWidget(self.area)

        self.setLayout(layout)

    def atualizar(self):

        saldos = ContaService.obter_saldos(
            self.cliente_id
        )

        self.lbl_corrente.setText(
            f'Saldo Corrente: R$ {saldos[0]:.2f}'
        )

        self.lbl_poupanca.setText(
            f'Saldo Poupança: R$ {saldos[1]:.2f}'
        )

    def mostrar_extrato(self):

        dados = ContaService.extrato(
            self.cliente_id
        )

        texto = '===== EXTRATO =====\n\n'

        for item in dados:

            texto += f'''
Data: {item[3]}
Tipo: {item[0]}
Valor: R$ {item[1]:.2f}
Detalhes: {item[2]}
--------------------------------
'''

        self.area.setText(texto)

    def realizar_saque(self):

      dialog = InputDialog(
            'SAQUE',
            'Digite o valor'
        )

      if dialog.exec():

            valor = float(dialog.get_value())

            sucesso = ContaService.sacar(
                self.cliente_id,
                valor
            )

            if sucesso:

                QMessageBox.information(
                    self,
                    'Sucesso',
                    'Saque realizado'
                )

                self.atualizar()
                self.mostrar_extrato()

            else:

                alert = AlertDialog(
                    'Erro',
                    'Saldo insuficiente'
                )

                alert.exec()

    def realizar_pix(self):

        dialog_chave = InputDialog(
            'TRANSFERÊNCIA PIX',
            'Digite a chave PIX'
        )

        if dialog_chave.exec():

            chave = dialog_chave.get_value()

            dialog_valor = InputDialog(
                'TRANSFERÊNCIA PIX',
                'Digite o valor'
            )

            if dialog_valor.exec():
                try:
                    valor = float(
                        dialog_valor.get_value()
                    )

                    sucesso = PixService.transferir(
                        self.cliente_id,
                        chave,
                        valor
                    )

                    if sucesso == True:

                        alert = AlertDialog(
                            'Sucesso',
                            'PIX realizado'
                        )

                        alert.exec()

                        self.atualizar()
                        self.mostrar_extrato()
                    elif sucesso == 'MESMA_CONTA':
                        alert = AlertDialog(
                            'Operação inválida',
                            'Você não pode transferir para sua própria conta.'
                        )

                        alert.exec()

                    else:

                        alert = AlertDialog(
                            'Erro',
                            'Falha no PIX'
                        )

                        alert.exec()

                except:

                    QMessageBox.warning(
                        self,
                        'Erro',
                        'Digite um valor válido'
                    )