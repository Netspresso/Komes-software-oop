import os, sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QCursor, QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Komes Software")
        self.setGeometry(200, 200, 800, 600)
        self.setStyleSheet("background: #fff;")

        self.widgets = {
            "price": [],
            "logo": [],
            'leftHeader': [],
            'mediumHeader': [],
            'rightHeader': [],
            'perpetual_license': [],
            'yearly_license': [],
        }
        self.buttons = {
            "buttonNFX": [],
            "buttonMF": [],
            "buttonCAE": [],
            "buttonSDC": [],
            "buttonMW": [],
        }

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

        # Button widget
        self.buttonNFX = self.create_button("Midas NFX")
        # self.buttonNFX.setGeometry(QtCore.QRect(20, 80, 0, 0))
        self.buttonMF = self.create_button("Midas MeshFree")
        self.buttonCAE = self.create_button("CAE LIMIT")
        self.buttonSDC = self.create_button("SDC Verifier")
        self.buttonMW = self.create_button("DEP MeshWorks")

        # buttons callback
        # self.buttonNFX.clicked.connect(start_choosing_NFX)
        # self.buttonMF.clicked.connect(start_choosing_MF)
        # self.buttonCAE.clicked.connect(start_choosing_CAE)
        # self.buttonSDC.clicked.connect(start_choosing_SDC)
        # self.buttonMW.clicked.connect(start_choosing_MW)

        # Storing buttons into dictionary
        self.buttons["buttonCAE"].append(self.buttonCAE)
        self.buttons["buttonNFX"].append(self.buttonNFX)
        self.buttons["buttonMF"].append(self.buttonMF)
        self.buttons["buttonSDC"].append(self.buttonSDC)
        self.buttons["buttonMW"].append(self.buttonMW)

        self.button_is_checked = True

        self.y = 160
        for button in self.buttons:
            self.buttons[button][-1].setGeometry(QtCore.QRect(
                20, self.y, 0, 0))
            self.buttons[button][-1].adjustSize()
            self.buttons[button][-1].setCheckable(True)
            self.buttons[button][-1].released.connect(
                self.the_button_was_released)
            self.buttons[button][-1].setChecked(self.button_is_checked)

            self.y += 60

        # #Storing headers into dictionary
        self.widgets["leftHeader"].append(self.leftHeader)
        self.widgets["rightHeader"].append(self.rightHeader)

    def the_button_was_released(self):
        self.button_is_checked = self.buttons["buttonNFX"][-1].isChecked()

        print(self.button_is_checked)

    def create_button(self, label):
        """ Function that handle creating buttons with styling """
        button = QPushButton(self)
        button.setText(label)
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button.adjustSize()
        button.setStyleSheet("*{border: 4px solid '#BC006C';" +
                             "border-radius: 15px;" + "font-size: 25px;" +
                             "color: 'black';" + "padding: 5px 10px;" +
                             "margin: 5px 10px;}" +
                             "*:hover{background: '#BC006C';" +
                             "color: white;}")

        return button


def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


window()