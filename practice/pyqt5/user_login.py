import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QLineEdit
import sqlite3


class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.baglanti_olustur()
        self.init_ui()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("database.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS uyeler (kullanici_adi TEXT, parola TEXT)")
        self.baglanti.commit()

    def init_ui(self):
        self.kullanici_adi = QLineEdit()
        self.parola = QLineEdit()
        self.parola.setEchoMode(QLineEdit.EchoMode.Password)
        self.giris = QtWidgets.QPushButton("Giriş Yap")
        self.yazi_alani = QtWidgets.QLabel("")

        self.giris.clicked.connect(self.login)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setWindowTitle("Kullanıcı Girişi")
        self.show()

    def login(self):
        adi = self.kullanici_adi.text()
        par = self.parola.text()

        self.cursor.execute("SELECT * FROM uyeler WHERE kullanici_adi = ? and parola = ?", (adi, par))
        data = self.cursor.fetchall()

        if not data:
            self.yazi_alani.setText("Böyle bir hesap yok.")
        else:
            self.yazi_alani.setText(f"Giriş başarılı. Hoş geldiniz {adi}")

    def closeEvent(self, event):
        self.baglanti.close()


app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec())
