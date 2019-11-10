import sip
from PyQt5.QtCore import QByteArray, QDataStream, QIODevice, QPoint, QMimeData, Qt
from PyQt5.QtGui import QDrag

sip.setapi('QString', 2)

from PyQt5.QtWidgets import QFrame, QMainWindow, QApplication, QLabel

myMimeType = 'application/MyWindow'


class MyLabel(QLabel):
    def __init__(self, parent):
        super(MyLabel, self).__init__(parent)

        self.setStyleSheet("""
            background-color: black;
            color: white;
            font: bold;
            padding: 6px;
            border-width: 2px;
            border-style: solid;
            border-radius: 16px;
            border-color: white;
        """)

    def mousePressEvent(self, event):
        itemData = QByteArray()
        dataStream = QDataStream(itemData, QIODevice.WriteOnly)
        dataStream.writeString(self.text())
        dataStream << QPoint(event.pos() - self.rect().topLeft())

        mimeData = QMimeData()
        mimeData.setData(myMimeType, itemData)
        mimeData.setText(self.text())

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(event.pos() - self.rect().topLeft())

        self.hide()

        if drag.exec_(Qt.MoveAction | Qt.CopyAction, Qt.CopyAction) == Qt.MoveAction:
            self.close()

        else:
            self.show()


class MyFrame(QFrame):
    def __init__(self, parent=None):
        super(MyFrame, self).__init__(parent)

        self.setStyleSheet("""
            background-color: lightgray;
            border-width: 2px;
            border-style: solid;
            border-color: black;
            margin: 2px;
        """)

        y = 6
        for labelNumber in range(6):
            label = MyLabel(self)
            label.setText("Label #{0}".format(labelNumber))
            label.move(6, y)
            label.show()

            y += label.height() + 2

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat(myMimeType):
            if event.source() in self.children():
                event.setDropAction(Qt.MoveAction)
                event.accept()

            else:
                event.acceptProposedAction()

        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasFormat(myMimeType):
            mime = event.mimeData()
            itemData = mime.data(myMimeType)
            dataStream = QDataStream(itemData, QIODevice.ReadOnly)

            text = QByteArray()
            offset = QPoint()
            dataStream >> text >> offset

            newLabel = MyLabel(self)
            newLabel.setText(event.mimeData().text())
            newLabel.move(event.pos() - offset)
            newLabel.show()

            if event.source() in self.children():
                event.setDropAction(Qt.MoveAction)
                event.accept()

            else:
                event.acceptProposedAction()

        else:
            event.ignore()


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.myFrame = MyFrame(self)

        self.setCentralWidget(self.myFrame)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.setApplicationName('MyWindow')

    main = MyWindow()
    main.resize(333, 333)
    main.move(app.desktop().screen().rect().center() - main.rect().center())
    main.show()

    sys.exit(app.exec_())
