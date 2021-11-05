import os, sys, ast
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QComboBox, QGridLayout, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QCursor, QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Komes Software")
        self.setGeometry(200, 200, 800, 600)

        # self.setFixedWidth(1000)
        self.setStyleSheet("background: #fff;")

        # self.layout1 = QVBoxLayout(self)  # Lewa kolumna
        # self.layout2 = QVBoxLayout(self)  # Prawa kolumna

        self.initUI()

    def initUI(self):
        ''' Function that handle displaying initial screen '''

        # Display Logo
        self.image = QPixmap("logo.jpg")
        self.logo = QLabel(self)
        self.logo.setPixmap(self.image)
        self.logo.setGeometry(QtCore.QRect(320, 0, 160, 41))
        self.logo.setStyleSheet("margin-top: 20px;")
        self.logo.adjustSize()
        # self.layout1.addWidget(self.logo)

        # Headers
        self.leftHeader = QLabel(self)
        self.leftHeader.setText("Wybierz program")
        self.rightHeader = QLabel(self)
        self.rightHeader.setText("Wybrane")
        self.headers = [self.leftHeader, self.rightHeader]
        for header in self.headers:
            header.setStyleSheet("font-size: 30px;" + "color: #02119B;" +
                                 "margin: auto;")
        self.leftHeader.setGeometry(QtCore.QRect(20, 40, 0, 0))
        self.rightHeader.setGeometry(QtCore.QRect(500, 40, 0, 0))
        self.leftHeader.adjustSize()
        self.rightHeader.adjustSize()

        self.software_list = QComboBox(self)
        self.software_list.addItems([
            "Wybierz",  #0
            "Midas NFX",  #1
            "Midas MeshFree",  #2
            "CAE LIMIT",  #3
            "SDC Verifier",  #4
            "DEP MeshWorks",  #5
        ])
        self.software_list.move(60, 140)
        self.software_list.setStyleSheet("font-size: 22px;")
        self.software_list.adjustSize()

        self.module_header = QLabel(self)
        self.module_header.setText("Wybierz Moduł")
        self.module_header.setStyleSheet("font-size: 30px;" +
                                         "color: #02119B;" + "margin: auto;")
        self.module_header.setGeometry(QtCore.QRect(20, 160, 0, 0))
        self.module_header.adjustSize()

        self.module_list = QComboBox(self)
        self.module_list.addItems([
            "Wybierz",
        ])
        self.module_list.move(60, 260)
        self.module_list.setStyleSheet("font-size: 22px;")
        self.module_list.adjustSize()

        self.software_list.currentIndexChanged.connect(self.index_changed)
        self.software_list.currentIndexChanged.connect(self.choose_soft)
        # self.widget = QWidget(self)
        # self.widget.setLayout(self.layout1)

    def index_changed(self, i):  # i is an int
        print(i)

    def choose_soft(self, i):
        # Stored pricelists
        if i == 1:
            self.choosen = 'NFX'
        elif i == 2:
            self.choosen = 'MF'
        elif i == 3:
            self.choosen = 'CAE'
        elif i == 4:
            self.choosen = 'SDC'
        elif i == 5:
            self.choosen = 'MW'
        else:
            return

        # pricelist relative path
        self.script_dir = os.path.dirname(
            __file__)  #<-- absolute dir the script is in
        self.rel_path_V = "prices\\versions\\{}.txt".format(self.choosen)
        self.abs_file_path_V = os.path.join(self.script_dir, self.rel_path_V)
        self.rel_path_M = "prices\\modules\\{}.txt".format(self.choosen)
        self.abs_file_path_M = os.path.join(self.script_dir, self.rel_path_M)

        with open(self.abs_file_path_V, 'r') as v_prices:
            self.contents = v_prices.read()
            self.V_pricing = ast.literal_eval(self.contents)

        with open(self.abs_file_path_M, 'r') as m_prices:
            self.contents = m_prices.read()
            self.M_pricing = ast.literal_eval(self.contents)

        # print([key for key, value in self.V_pricing.items()])

        self.module_list.addItems(
            [key for key, value in self.V_pricing.items()])
        self.module_list.adjustSize()

        # self.module_list.move(60, 140)
        # self.module_list.setStyleSheet("font-size: 22px;")
        # self.module_list.adjustSize()

        # self.module_list.currentIndexChanged.connect(self.index_changed)

        # #Storing headers into dictionary
        # self.widgets["leftHeader"].append(self.leftHeader)
        # self.widgets["rightHeader"].append(self.rightHeader)


def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


window()