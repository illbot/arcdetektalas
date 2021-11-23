from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from mtcnn.mtcnn import MTCNN

from haarCascade import haarCascade
from mtcnn_detect import mtcnn_detect
from rgb_detect import rgb_detect

#import mtcnn
import sys
import cv2
import os

'''
datas = [
    (os.path.join(os.path.dirname(mtcnn.__file__),'data\*'), )
]
'''


class MainContent(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.src_image = QtWidgets.QLabel()
        self.result_image = QtWidgets.QLabel()
        self.face_count = QtWidgets.QLabel()
        self.error = QtWidgets.QLabel()
        self.error.setText("")

        #self.detector = MTCNN()

        self.img_url = None

        self.btn_MTCNN = QtWidgets.QPushButton("MTCNN", self)
        self.btn_HaarCascade = QtWidgets.QPushButton("HaarCascade", self)
        self.btn_RGB = QtWidgets.QPushButton("RGB", self)


        hbox = QtWidgets.QHBoxLayout()

        hbox.addWidget(self.btn_MTCNN)
        hbox.addWidget(self.btn_HaarCascade)
        hbox.addWidget(self.btn_RGB)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addLayout(hbox)

        vbox.addWidget(self.error)
        lb1 = QtWidgets.QLabel("source: ")
        vbox.addWidget(lb1)

        vbox.addWidget(self.src_image)

        lb2 = QtWidgets.QLabel("result: ")
        vbox.addWidget(lb2)
        vbox.addWidget(self.result_image)
        vbox.addWidget(self.face_count)

        self.initButtons()
        self.setLayout(vbox)
        self.show()

    def setSrcImg(self, img):
        self.src_image = img

    def setResultImg(self, img):
        self.result_image = img

    def setImgUrl(self, url):
        self.img_url = url

    @pyqtSlot()
    def MTCNN(self):
        if self.img_url is not None:
            self.error.setText("MTCNN")
            img = cv2.imread(self.img_url)
            [result_pic, faces_count] = mtcnn_detect(img)
            self.setResultPic(result_pic, faces_count)
        else:
            self.error.setText("Nincs betöltve kép")

    @pyqtSlot()
    def HaarCascade(self):
        if self.img_url is not None:
            self.error.setText("HaarCascade")
            img = cv2.imread(self.img_url)
            [result_pic, faces_count] = haarCascade(img)
            self.setResultPic(result_pic, faces_count)
        else:
            self.error.setText("Nincs betöltve kép")

    @pyqtSlot()
    def RGB(self):
        if self.img_url is not None:
            self.error.setText("RGB")
            img = cv2.imread(self.img_url)
            [result_pic, faces_count] = rgb_detect(img)
            self.setResultPic(result_pic, faces_count)
        else:
            self.error.setText("Nincs betöltve kép")

    def initButtons(self):
        self.btn_MTCNN.clicked.connect(self.MTCNN)
        self.btn_HaarCascade.clicked.connect(self.HaarCascade)
        self.btn_RGB.clicked.connect(self.RGB)

    def setResultPic(self, result_pic, faces_count):
        result_rgb = cv2.cvtColor(result_pic, cv2.COLOR_BGR2RGB)
        result_pixmap = self.convert_nparray_to_QPixmap(result_rgb)
        pm1 = result_pixmap.scaled(800, 450, Qt.KeepAspectRatio)
        self.result_image.setPixmap(pm1)
        self.face_count.setText("Detektált arcok száma: " + str(faces_count))

    def convert_nparray_to_QPixmap(self, img):
        w, h, ch = img.shape
        # Convert resulting image to pixmap
        if img.ndim == 1:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

        qimg = QImage(img.data, h, w, 3*h, QImage.Format_RGB888)
        qpixmap = QPixmap(qimg)

        return qpixmap


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

        self.setGeometry(300, 300, 805, 720)
        self.show()

    def import_pic(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '.\\teszt_kepek', "Image files (*.jpg *.gif)")
        self.image_url = fname[0]
        print(self.image_url)
        pixmap = QPixmap(self.image_url)
        pm1 = pixmap.scaled(800, 450, Qt.KeepAspectRatio)
        self.main_widget.src_image.setPixmap(pm1)
        self.main_widget.setImgUrl(self.image_url)



def main_window():
    app = QApplication(sys.argv)
    example = App()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main_window()