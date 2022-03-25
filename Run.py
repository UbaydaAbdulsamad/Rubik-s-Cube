import sys
import os
import math
from PyQt5.QtWidgets import QMainWindow, QStatusBar, QApplication, QLabel, QRadioButton, QListWidget, QListWidgetItem, QStatusBar, QVBoxLayout
from PyQt5 import QtGui, uic
from PyQt5.QtGui import QImage, QPixmap

colors = []
current_directory = 'images\\'

for i in range(12):
    colors.append((255, 255, 255))

def rgb_to_hsi (r, g, b):
    ''' converts RGB color space to HSI
        inputs:
            r, g, b: int(0 -> 255)
        outputs:
            h: int(0 -> 360)
            s: int(0 -> 1)
            i: int(0 -> 1)
    '''   
    
    r /= 255
    g /= 255
    b /= 255
    
    #finding Hue
    h = math.acos(0.5*((r-g)+(r-b))/(math.sqrt((r-g)**2+(r-b)*(g-b))+0.00000001))
    h = math.degrees(h)
    if b>g: h = 360-h

    # calculating Saturaiton
    s = 1-3/(r+g+b+0.00000001)*(min(r, g, b))
    
    # calculating intensity
    i = (r+g+b)/3
    
    h, i, s, = round(h, 2), round(i, 2), round(s, 2)        
    return (h, s, i)

class ColorPicker(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ColorPicker.ui', self)
        
        #region define widgets
        self.verticalLayout = self.findChild(QVBoxLayout, 'verticalLayout')
        isinstance(self.verticalLayout, QVBoxLayout)

        self.listWidget = self.findChild(QListWidget, 'listWidget')
        self.label = self.findChild(QLabel, 'label')

        self.statusbar = self.findChild(QStatusBar, 'statusbar')
        isinstance(self.statusbar, QStatusBar)

        self.radioButton_RGB = self.findChild(QRadioButton, 'radioButton_RGB')
        assert isinstance(self.radioButton_RGB, QRadioButton)

        self.radioButton_HSI = self.findChild(QRadioButton, 'radioButton_HSL')
        assert isinstance(self.radioButton_HSI, QRadioButton)

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
    
        self.label_red_hue = self.findChild(QLabel, 'label_red_hue')
        self.label_green_saturation = self.findChild(QLabel, 'label_green_saturation')
        self.label_blue_intensity = self.findChild(QLabel, 'label_blue_intensity')
        self.label_red_value = self.findChild(QLabel, 'label_red_value')
        self.label_green_value = self.findChild(QLabel, 'label_green_value')
        self.label_blue_value = self.findChild(QLabel, 'label_blue_value')
        assert isinstance(self.label_red_hue, QLabel)
        assert isinstance(self.label_red_value, QLabel)

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
        self.current_color = QtGui.QColor('white')
        self.statusbar.showMessage('Ubayda Abdulsamad, ID:1906A604, Homework(1)')

        # linking widgets to events
        self.listWidget.itemClicked.connect(self.item_clicked_event)
        self.radioButton_RGB.pressed.connect(self.toggled_rgb)
        self.radioButton_HSI.pressed.connect(self.toggled_hsi)
        for radioButton in self.list_radioButtons:
            radioButton.toggled.connect(self.radio_pressed)

        self.populate_list()  
        self.showMaximized()

    def toggled_rgb(self):
        self.label_red_hue.setText('Red:')
        self.label_green_saturation.setText('Green:')
        self.label_blue_intensity.setText('Blue:')
        
        if self.current_color == None: return
        
        r, g, b, _ = self.current_color.getRgb()
        self.label_red_value.setText(str(r))
        self.label_green_value.setText(str(g))
        self.label_blue_value.setText(str(b))        

    def toggled_hsi(self):
        self.label_red_hue.setText('Hue:')
        self.label_green_saturation.setText('Saturation:')
        self.label_blue_intensity.setText('Intensity:')
        
        if self.current_color == None: return

        r, g, b, _ = self.current_color.getRgb()
        h, s, i = rgb_to_hsi(r, g, b)
            
        self.label_red_value.setText(str(h))
        self.label_green_value.setText(str(s))
        self.label_blue_value.setText(str(i))
               
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
        
        pic = self.listWidget.item(0).data(0)  
        self.label.setPixmap(pic)
        self.current_image = self.listWidget.item(0).data(5)

    def mousePressEvent(self, QMouseEvent):

        x = QMouseEvent.x() - self.label.x()
        y = QMouseEvent.y() - self.label.y()     
        
        if QMouseEvent.x() < self.label.x() or QMouseEvent.x() > self.label.x()+self.label.width(): return
        if QMouseEvent.y() < self.label.y() or QMouseEvent.y() > self.label.y()+self.label.height(): return

        color = self.current_image.pixelColor(x, y)
        
        self.update_color_list(color)
        self.update_labels(color)
        
    def radio_pressed(self):
        for index, radio in enumerate(self.list_radioButtons):
            if not radio.isChecked():continue
            r, g, b = colors[index]
            color = QtGui.QColor(r, g, b)
            self.update_color_list(color)
            self.update_labels(color)
            return
        
    def update_color_list(self, color):
        r, g, b, _ = color.getRgb()
        for index, radio in enumerate(self.list_radioButtons):
            if not radio.isChecked():continue
            colors[index] = r, g, b
            self.current_color = color
            self.display_colors()
            return

    def display_colors(self):
        for index, object in enumerate(self.list_labelColor):
            r, g, b = colors[index]
            object.setStyleSheet('background-color: rgb({}, {}, {});'.format(r, g, b))

    def update_labels(self, color):
        
        r, g, b, _ = color.getRgb()
        
        if self.radioButton_RGB.isChecked():
            self.label_red_value.setText(str(r))
            self.label_green_value.setText(str(g))
            self.label_blue_value.setText(str(b))
        
        elif self.radioButton_HSI.isChecked():
            h, s, i = rgb_to_hsi(r, g, b)
            self.label_red_value.setText(str(h))
            self.label_green_value.setText(str(s))
            self.label_blue_value.setText(str(i))
        
           
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ColorPicker()

    demo.show()
    sys.exit(app.exec_())
