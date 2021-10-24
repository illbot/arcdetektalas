from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys




def main_window():
    app = QApplication(sys.argv)
    global win
    win = QMainWindow()
    win.setGeometry(200,200,600,400)
    win.setWindowTitle("Arcdetektalas")

    label = QtWidgets.QLabel(win)
    label.setText("label")
    label.move(50,50)

    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main_window()