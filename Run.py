import sys
import os
from textwrap import indent
from PIL import ImageQt
from PyQt5.QtWidgets import QMainWindow, QWidget, QMenuBar, QStatusBar, QApplication, QLabel, QPushButton, QRadioButton
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QScrollArea, QStatusBar
from PyQt5 import QtGui
from PyQt5 import *
from PyQt5 import uic

list_images = []
list_photos = []
current_directory = 'images\\'
colors = []
for i in range(12):
    colors.append((255, 255, 255))

def load_images():
    images = os.listdir(current_directory)
    for image in images:
        if image.endswith(".png") or image.endswith("jpg"):
            list_images.append(os.path.join(current_directory, image))
        photo = QtGui.QImage(image)
        list_photos.append(photo)

class ColorPicker(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ColorPicker.ui', self)
        

        # define widgets
        self.listWidget = self.findChild(QListWidget, 'listWidget')
        self.label = self.findChild(QLabel, 'label')

        self.statusbar = self.findChild(QStatusBar, 'statusbar')
        assert isinstance(self.statusbar, QStatusBar)

        self.labelColor_1 = self.findChild(QLabel, 'labelColor_1')
        self.labelColor_2 = self.findChild(QLabel, 'labelColor_2')
        self.labelColor_3 = self.findChild(QLabel, 'labelColor_3')
        self.labelColor_4 = self.findChild(QLabel, 'labelColor_4')
        self.labelColor_5 = self.findChild(QLabel, 'labelColor_5')
        self.labelColor_6 = self.findChild(QLabel, 'labelColor_6')
        self.labelColor_7 = self.findChild(QLabel, 'labelColor_7')
        self.labelColor_8 = self.findChild(QLabel, 'labelColor_8')
        self.labelColor_9 = self.findChild(QLabel, 'labelColor_9')
        self.labelColor_10 = self.findChild(QLabel, 'labelColor_10')
        self.labelColor_11 = self.findChild(QLabel, 'labelColor_11')
        self.labelColor_12 = self.findChild(QLabel, 'labelColor_12')
        self.labelColor_13 = self.findChild(QLabel, 'labelColor_13')
        self.labelColor_14 = self.findChild(QLabel, 'labelColor_14')
        self.labelColor_15 = self.findChild(QLabel, 'labelColor_15')
        self.labelColor_16 = self.findChild(QLabel, 'labelColor_16')

        self.radioButton = self.findChild(QRadioButton, 'radioButton')
        self.radioButton_2 = self.findChild(QRadioButton, 'radioButton_2')
        self.radioButton_3 = self.findChild(QRadioButton, 'radioButton_3')
        self.radioButton_4 = self.findChild(QRadioButton, 'radioButton_4')
        self.radioButton_5 = self.findChild(QRadioButton, 'radioButton_5')
        self.radioButton_6 = self.findChild(QRadioButton, 'radioButton_6')
        self.radioButton_7 = self.findChild(QRadioButton, 'radioButton_7')
        self.radioButton_8 = self.findChild(QRadioButton, 'radioButton_8')
        self.radioButton_9 = self.findChild(QRadioButton, 'radioButton_9')
        self.radioButton_10 = self.findChild(QRadioButton, 'radioButton_10')
        self.radioButton_11 = self.findChild(QRadioButton, 'radioButton_11')
        self.radioButton_12 = self.findChild(QRadioButton, 'radioButton_12')


        assert isinstance(self.listWidget, QListWidget)
        assert isinstance(self.label, QLabel)
        assert isinstance(self.labelColor_1, QLabel)
        assert isinstance(self.radioButton, QRadioButton)
        assert isinstance(self.radioButton_2, QRadioButton)

        self.statusbar.showMessage("Hellothere")
        

        # load objects
        load_images()
        self.populate_list()
        self.label.setPixmap(QtGui.QPixmap(list_images[0]))

        self.listWidget.currentItemChanged.connect(self.update_image)

        self.list_labelColor = [self.labelColor_1,
                            self.labelColor_2,
                            self.labelColor_3,
                            self.labelColor_4,
                            self.labelColor_5,
                            self.labelColor_6,
                            self.labelColor_7,
                            self.labelColor_8,
                            self.labelColor_9,
                            self.labelColor_10,
                            self.labelColor_11,
                            self.labelColor_12]

        self.list_radioButtons = [self.radioButton,
                                  self.radioButton_2,
                                  self.radioButton_3,
                                  self.radioButton_4,
                                  self.radioButton_5,
                                  self.radioButton_6,
                                  self.radioButton_7,
                                  self.radioButton_8,
                                  self.radioButton_9,
                                  self.radioButton_10,
                                  self.radioButton_11,
                                  self.radioButton_12] 

        self.update_display_colors()   
        self.showMaximized()


    def mousePressEvent(self, QMouseEvent):
        x = QMouseEvent.x() - self.label.x()
        y = QMouseEvent.y() - self.label.y()

        a = self.label.x()
        c = self.label.y()
        b = a + self.label.width()
        d = self.label.height()
        
        if x<a or x>b or y<c or y>d: return

        index = y * self.label.size().width() + x
        image = ImageQt.fromqpixmap(self.label.pixmap())
        image = image.resize((self.label.size().width(), self.label.size().height()))
        image_data = image.getdata()
        r, g, b = image_data[index]

        for index, radio in enumerate(self.list_radioButtons):
            if not radio.isChecked():continue
            colors[index] = r, g, b
        
        self.update_display_colors()


    def update_display_colors(self):
        for index, object in enumerate(self.list_labelColor):
            r, g, b = colors[index]
            object.setStyleSheet('background-color: rgb({}, {}, {});'.format(r, g, b))

    def update_image(self):
        index = self.listWidget.currentRow()
        image = QtGui.QPixmap(list_images[index])

        if image.width() > self.label.width():
            image = image.scaledToWidth(self.label.width())

        elif image.height() > self.label.height():
            image = image.scaledToHeight(self.label.height())

        self.label.setPixmap(image)

    def mouseMoveEvent(self, QMouseEvent) -> None:
        x = QMouseEvent.x() - self.label.x()
        y = QMouseEvent.y() - self.label.y()

        a = self.label.x()
        c = self.label.y()
        b = a + self.label.width()
        d = self.label.height()
        
        if x<a or x>b or y<c or y>d: return

        self.statusbar.showMessage('triggered!')


    def populate_list(self):
        for image in list_images:
            item = QListWidgetItem()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(image),QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item.setIcon(icon)
            self.listWidget.addItem(item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ColorPicker()

    demo.show()
    sys.exit(app.exec_())
