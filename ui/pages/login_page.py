from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from services.auth_service import AuthService

class LoginPage(QWidget):

    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window

        layout = QHBoxLayout()

        banner = QLabel()
        pixmap = QPixmap('ui/assets/logoitau.jpg')

        banner.setPixmap(
            pixmap
        )

        painel = QWidget()

        painel.setStyleSheet(
            'background: #0f172a;'
        )

        painel_layout = QVBoxLayout()

        titulo = QLabel('BANCO VISION')

        titulo.setStyleSheet('''
            color: white;
            font-size: 40px;
            font-weight: bold;
        ''')

        subtitulo = QLabel(
            'Terminal Bancário Inteligente'
        )

        subtitulo.setStyleSheet('''
            color: #cbd5e1;
            font-size: 20px;
        ''')

        self.cpf = QLineEdit()
        self.cpf.setPlaceholderText('CPF')

        self.senha = QLineEdit()
        self.senha.setPlaceholderText('Senha')
        self.senha.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        for campo in [self.cpf, self.senha]:

            campo.setMinimumHeight(70)

            campo.setStyleSheet('''
                background: white;
                border-radius: 15px;
                font-size: 22px;
                padding: 15px;
            ''')

        btn = QPushButton('ACESSAR')

        btn.setMinimumHeight(80)

        btn.setStyleSheet('''
            QPushButton {
                background: #16a34a;
                color: white;
                font-size: 28px;
                font-weight: bold;
                border-radius: 18px;
            }

            QPushButton:hover {
                background: #15803d;
            }
        ''')

        btn.clicked.connect(self.login)

        painel_layout.addStretch()
        painel_layout.addWidget(titulo)
        painel_layout.addWidget(subtitulo)
        painel_layout.addSpacing(30)
        painel_layout.addWidget(self.cpf)
        painel_layout.addWidget(self.senha)
        painel_layout.addWidget(btn)
        painel_layout.addStretch()

        painel.setLayout(painel_layout)

        layout.addWidget(banner, 2)
        layout.addWidget(painel, 1)

        self.setLayout(layout)

    def login(self):

        usuario = AuthService.login(
            self.cpf.text(),
            self.senha.text()
        )

        if usuario:
            self.main_window.abrir_dashboard(usuario)

        else:
            QMessageBox.warning(
                self,
                'Erro',
                'Login inválido'
            )
