import os, sys, ast
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QComboBox, QGridLayout, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QListWidgetItem, QListWidget
from PyQt5.QtGui import QCursor, QPixmap


class MainWindow(QMainWindow):
    """Class that displays Main Window of the App"""
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Komes Software")
        self.setGeometry(200, 200, 800, 600)
        self.setStyleSheet("background: #fff;")

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
        self.modules_names = []
        self.modules_prices = []

        self.software_list.move(60, 140)
        self.software_list.setStyleSheet("font-size: 22px;")
        self.software_list.adjustSize()

        self.version_header = QLabel(self)
        self.version_header.setText("Wybierz Wersję")
        self.version_header.setStyleSheet("font-size: 30px;" +
                                          "color: #02119B;" + "margin: auto;")
        self.version_header.setGeometry(QtCore.QRect(20, 160, 0, 0))
        self.version_header.adjustSize()

        self.version_list = QComboBox(self)
        self.version_list.addItems([
            "Wybierz",
        ])
        self.version_list.move(60, 260)
        self.version_list.setStyleSheet("font-size: 22px;")
        self.version_list.adjustSize()

        self.modules_list = QListWidget(self)
        self.items_list = []

        self.choosen_list = QListWidget(self)

        self.choosen_list.setStyleSheet("font-size: 16px;" + "color: #000;" +
                                        "margin: auto;")
        self.modules_list.setStyleSheet("font-size: 16px;" + "color: #000;" +
                                        "margin: auto;")
        self.modules_list.adjustSize()
        self.modules_list.setSelectionMode(
            QtWidgets.QAbstractItemView.ExtendedSelection)
        self.choosen_list.setSelectionMode(
            QtWidgets.QAbstractItemView.ExtendedSelection)
        self.choosen_list.adjustSize()

        self.modules_list.move(20, 300)
        self.choosen_list.move(270, 300)

        self.add_button = QPushButton(self)
        self.add_button.setText('>')
        self.add_button.setStyleSheet("*{font-size: 22px;" + "width: 24px;" +
                                      "padding: 4px;" + "margin: 5px;" +
                                      "border: 0.5px solid black;}" +
                                      "*:hover{background: '#BC006C';}")
        self.add_button.adjustSize()
        self.add_button.move(250, 370)

        # self.software_list.currentIndexChanged.connect(self.index_changed)
        self.software_list.currentIndexChanged.connect(self.choose_soft)

    # def index_changed(self, i):  # i is an int
    #     print(i)

    def choose_soft(self, i):
        # Stored pricelists
        if i == 1:
            self.choosen_soft = 'NFX'
        elif i == 2:
            self.choosen_soft = 'MF'
        elif i == 3:
            self.choosen_soft = 'CAE'
        elif i == 4:
            self.choosen_soft = 'SDC'
        elif i == 5:
            self.choosen_soft = 'MW'
        else:
            return

        self.show_versions(self.choosen_soft)

    def show_versions(self, choosen_software):
        """Function that handle giving the version choice depending on choosen software"""

        # pricelist relative path
        self.script_dir = os.path.dirname(
            __file__)  #<-- absolute dir the script is in
        self.rel_path_V = "prices\\versions\\{}.txt".format(choosen_software)
        self.abs_file_path_V = os.path.join(self.script_dir, self.rel_path_V)

        with open(self.abs_file_path_V, 'r') as v_prices:
            self.contents = v_prices.read()
            self.V_pricing = ast.literal_eval(self.contents)

        # Adding items (List of accesible versions) to QCombo box, depending on choosen software
        self.version_list.addItems(
            [key for key, value in self.V_pricing.items()])
        self.version_list.adjustSize()

        self.version_list.currentIndexChanged.connect(self.choose_version)

    def choose_version(self, i):
        """function that handle choosing one particular version of a software"""

        self.rel_path_M = "prices\\modules\\{}.txt".format(self.choosen_soft)
        self.abs_file_path_M = os.path.join(self.script_dir, self.rel_path_M)

        with open(self.abs_file_path_M, 'r') as m_prices:
            self.contents = m_prices.read()
            self.M_pricing = ast.literal_eval(self.contents)

        if i != 0:
            for key, value in self.M_pricing[i - 1].items():
                self.modules_names.append(key)
                self.modules_prices.append(value)

        for item in self.modules_names:
            listWidgetItem = QListWidgetItem(item)
            self.items_list.append(listWidgetItem)

        for item in self.items_list:
            self.modules_list.addItem(item)

    #     self.show_modules()

    # def show_modules(self):
    #     """Function that handle displaying module list"""

    #     self.add_button.clicked.connect(self.text_changed)

    def text_changed(self):
        for item in self.items_list:
            if item.isSelected():
                print("{} zostal wybany".format(item.text()))
                self.choosen_list.addItem(item)

        self.choosen_modules = []

        # self.version_list.currentIndexChanged.connect(self.choose_modules)

    def choose_modules(self, i):
        """Fuction that handle giving the module choice depending on choosen version"""

        self.choosen_modules.append(self.modules_names[i + 1])
        print(self.choosen_modules)


def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


window()