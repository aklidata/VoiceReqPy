import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget


def app():
    my_app = QApplication(sys.argv)
    w = QWidget()
    l1 = QtWidgets.QLabel(w)
    l1.setText("First Speech Rec App")
    w.setWindowTitle("Speech Recognition")
    w.show()
    sys.exit(my_app.exec_())

app()