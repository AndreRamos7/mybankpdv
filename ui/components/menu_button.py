from PyQt6.QtWidgets import QPushButton

class MenuButton(QPushButton):

    def __init__(self, texto, cor):
        super().__init__(texto)

        self.setMinimumHeight(120)

        self.setStyleSheet(f'''
            QPushButton {{
                background-color: {cor};
                color: white;
                font-size: 26px;
                font-weight: bold;
                border-radius: 20px;
                padding: 20px;
            }}

            QPushButton:hover {{
                border: 4px solid white;
            }}
        ''')
