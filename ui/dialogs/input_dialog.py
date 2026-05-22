from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

class InputDialog(QDialog):

    def __init__(self, titulo, placeholder=''):
        super().__init__()

        self.setWindowTitle(titulo)

        self.setMinimumSize(500, 300)

        self.setStyleSheet('''
            QDialog {
                background: #111827;
            }

            QLabel {
                color: white;
                font-size: 28px;
                font-weight: bold;
            }

            QLineEdit {
                background: white;
                border-radius: 15px;
                padding: 18px;
                font-size: 26px;
                min-height: 50px;
            }

            QPushButton {
                background: #2563eb;
                color: white;
                font-size: 24px;
                font-weight: bold;
                border-radius: 15px;
                min-height: 70px;
            }

            QPushButton:hover {
                background: #1d4ed8;
            }
        ''')

        layout = QVBoxLayout()

        self.label = QLabel(titulo)

        self.input = QLineEdit()
        self.input.setPlaceholderText(placeholder)

        self.btn_confirmar = QPushButton('CONFIRMAR')

        self.btn_confirmar.clicked.connect(self.accept)

        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addSpacing(20)
        layout.addWidget(self.btn_confirmar)

        self.setLayout(layout)

    def get_value(self):
        return self.input.text()