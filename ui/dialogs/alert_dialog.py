from PyQt6.QtWidgets import *

class AlertDialog(QDialog):

    def __init__(self, titulo, mensagem):
        super().__init__()

        self.setWindowTitle(titulo)

        self.setMinimumSize(500, 250)

        self.setStyleSheet('''
            QDialog {
                background: #0f172a;
            }

            QLabel {
                color: white;
                font-size: 26px;
            }

            QPushButton {
                background: #16a34a;
                color: white;
                font-size: 22px;
                min-height: 70px;
                border-radius: 15px;
            }
        ''')

        layout = QVBoxLayout()

        label = QLabel(mensagem)

        btn = QPushButton('OK')

        btn.clicked.connect(self.accept)

        layout.addWidget(label)
        layout.addWidget(btn)

        self.setLayout(layout)