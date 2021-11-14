from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MainContent(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.src_image = QtWidgets.QLabel()
        self.result_image = QtWidgets.QLabel()

        self.btn_MTCNN = QtWidgets.QPushButton("MTCNN", self)
        self.btn_HaarCascade = QtWidgets.QPushButton("HaarCascade", self)
        self.btn_RGB = QtWidgets.QPushButton("RGB", self)


        hbox = QtWidgets.QHBoxLayout()

        hbox.addWidget(self.btn_MTCNN)
        hbox.addWidget(self.btn_HaarCascade)
        hbox.addWidget(self.btn_RGB)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addLayout(hbox)

        lb1 = QtWidgets.QLabel("source: ")
        vbox.addWidget(lb1)

        vbox.addWidget(self.src_image)

        lb2 = QtWidgets.QLabel("result: ")
        vbox.addWidget(lb2)
        vbox.addWidget(self.result_image)

        self.initButtons()
        self.setLayout(vbox)
        self.show()

    def setSrcImg(self, img):
        self.src_image = img

    def setResultImg(self, img):
        self.result_image = img

    @pyqtSlot()
    def MTCNN(self):
        print("MTCNN")

    @pyqtSlot()
    def HaarCascade(self):
        print("Haar")

    @pyqtSlot()
    def RGB(self):
        print("RGB")

    def initButtons(self):
        self.btn_MTCNN.clicked.connect(self.MTCNN)
        self.btn_HaarCascade.clicked.connect(self.HaarCascade)
        self.btn_RGB.clicked.connect(self.RGB)


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.image_url = None
        self.main_widget = MainContent()

        self._init_UI()

    def _init_UI(self):
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        menu = QtWidgets.QMenuBar()
        openFileAction = QtWidgets.QAction('Import', self)
        openFileAction.triggered.connect(self.import_pic)
        menu.addAction(openFileAction)
        self.setMenuBar(menu)

        self.setGeometry(300, 300, 1280, 720)
        self.show()

    def import_pic(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '.\\teszt_kepek', "Image files (*.jpg *.gif)")
        self.image_url = fname[0]
        print(self.image_url)
        pixmap = QPixmap(self.image_url)
        pm1 = pixmap.scaled(800, 450, Qt.KeepAspectRatio)
        self.main_widget.src_image.setPixmap(pm1)



def main_window():
    app = QApplication(sys.argv)
    example = App()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main_window()