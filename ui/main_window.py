from PyQt6.QtWidgets import *
from ui.pages.login_page import LoginPage
from ui.pages.dashboard_page import DashboardPage

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Banco Vision')
        self.showMaximized()

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.login_page = LoginPage(self)

        self.stack.addWidget(self.login_page)

    def abrir_dashboard(self, usuario):
        self.dashboard = DashboardPage(self, usuario)

        self.stack.addWidget(self.dashboard)
        self.stack.setCurrentWidget(self.dashboard)

    def voltar_login(self):
        self.stack.setCurrentWidget(self.login_page)
