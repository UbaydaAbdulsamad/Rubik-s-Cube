import sys
import os
from textwrap import indent
from PIL import ImageQt
from PyQt5.QtWidgets import QMainWindow, QWidget, QMenuBar, QStatusBar, QApplication, QLabel, QPushButton, QRadioButton
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QScrollArea, QStatusBar, QVBoxLayout
from PyQt5 import QtGui
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import *
from PyQt5 import uic

list_Qimage = []
list_Qpixmap = []
colors = []
current_directory = 'images\\'

for i in range(12):
    colors.append((255, 255, 255))

def load_images():
    images = os.listdir(current_directory)
    for image in images:
        image = os.path.join(current_directory, image)
        list_Qimage.append(QImage(image))
        list_Qpixmap.append(QPixmap(image))
        print(image, ' has been loaded.')
    
class ColorPicker(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ColorPicker.ui', self)
        
        #region define widgets
        self.verticalLayout = self.findChild(QVBoxLayout, 'verticalLayout')
        assert isinstance(self.verticalLayout, QVBoxLayout)

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
        #endregion
        
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
         
        self.max_width = app.primaryScreen().size().width() - 400
        self.max_height = app.primaryScreen().size().height() - 50
        self.current_image = None

        # linking
        self.listWidget.itemClicked.connect(self.item_clicked_event)

        #load_images()
        self.populate_list()  
        self.showMaximized()

    def item_clicked_event(self, item):

        image = item.data(5)

        if image.width() > self.max_width:
            image = image.scaledToWidth(self.max_width)

        if image.height() > self.max_height:
            image = image.scaledToHeight(self.max_height)

        self.current_image = image
        self.label.setPixmap(QPixmap(image))

    def populate_list(self):
        images = os.listdir(current_directory)
        for image in images:
            path = os.path.join(current_directory, image)

            icon = QtGui.QIcon()
            icon.addPixmap(QPixmap(path),QtGui.QIcon.Normal, QtGui.QIcon.Off)

            item = QListWidgetItem()
            item.setData(0, QPixmap(path))
            item.setData(5, QImage(path))
            item.setIcon(icon)

            self.listWidget.addItem(item)

    def mousePressEvent(self, QMouseEvent):

        x = QMouseEvent.x() - self.label.x()
        y = QMouseEvent.y() - self.label.y()     

        color = self.current_image.pixelColor(x, y)
        r, g, b, _ = color.getRgb()

        for index, radio in enumerate(self.list_radioButtons):
            if not radio.isChecked():continue
            colors[index] = r, g, b
        self.update_display_colors()

    def update_display_colors(self):
        for index, object in enumerate(self.list_labelColor):
            r, g, b = colors[index]
            object.setStyleSheet('background-color: rgb({}, {}, {});'.format(r, g, b))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ColorPicker()

    demo.show()
    sys.exit(app.exec_())
