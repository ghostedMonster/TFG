import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox


def dialog():
    mbox = QMessageBox()

    mbox.setText("Parece que has pulsado")
    mbox.setDetailedText("No deberías haberlo hecho")
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    mbox.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(640, 480)
    w.setWindowTitle('Otra prueba d PyQt5')

    label = QLabel(w)
    label.setText("Pulsa aqui")
    label.move(300, 200)
    label.show()

    btn = QPushButton(w)
    btn.setText('Pulsa, anda')
    btn.move(300, 240)
    btn.show()
    btn.clicked.connect(dialog)

    w.show()
    sys.exit(app.exec_())
