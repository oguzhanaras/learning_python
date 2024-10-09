import os
from PyQt6 import QtWidgets, QtGui
import sys


def window():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("PyQt6 Lesson 2")

    # Mutlak dosya yolu
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "python.png")

    label1 = QtWidgets.QLabel(pencere)
    label2 = QtWidgets.QLabel(pencere)

    # Resmi yükle ve kontrol et
    pixmap = QtGui.QPixmap(image_path)
    if pixmap.isNull():
        print("Resim yüklenemedi, dosya yolunu kontrol et:", image_path)
    else:
        label2.setPixmap(pixmap)

    label1.setText("burasi bir yazidir")
    label1.move(200, 30)

    label2.move(200, 70)

    pencere.setGeometry(100, 100, 500, 500)
    pencere.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    window()
