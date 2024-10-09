import sys
from PyQt5 import QtWidgets


def window():
    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Lesson 3")

    button = QtWidgets.QPushButton(pencere)
    button.setText("burası buton")
    etiket = QtWidgets.QLabel(pencere)
    etiket.setText("merhaba dunya")

    etiket.move(200, 30)
    button.move(190, 80)

    pencere.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    window()
