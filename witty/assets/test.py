from PySide import QtGui, QtCore

class Images(QtGui.QScrollArea):
    def __init__(self, images):
        super().__init__()


        self.content = QtGui.QWidget()
        self.layout = QtGui.QGridLayout(self.content)
        self.layout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.setFixedHeight(800)
        images  =['test.png','test.png','test.png','test.png']
        row = 0
        for image in images:
            thumb = QtGui.QLabel()
            thumb.setPixmap(QtGui.QPixmap(image))
            self.layout.addWidget(thumb, row, 0)
            row += 1

        self.setWidget(self.content)
        self.setMinimumWidth(self.content.sizeHint().width())
        # self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        # layout.addWidget(scroll_area)

app = QtGui.QApplication([])

window = QtGui.QWidget()
layout = QtGui.QVBoxLayout(window)
scroll_area = Images(['test.png','test.png','test.png','test.png'])
layout.addWidget(scroll_area)
window.show()

app.exec_()