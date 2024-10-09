import sys
from PyQt5 import QtWidgets


def window():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("PyQt5 Lesson 1")
    pencere.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    window()
