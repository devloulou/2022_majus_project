from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import QPainter, QColor, QBrush, QPixmap
from PySide6.QtCore import Qt, QRect

class BackDropImageWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.__backdrop_image = ""
        self.painter = QPainter()

        self.pixmap = QPixmap(self.backdrop_image)
        # rgba színt
        self.fill_brush = QBrush(QColor(0, 0, 0, 210))

    @property
    def backdrop_image(self):
        return self.__backdrop_image

    @backdrop_image.setter
    def backdrop_image(self, image):
        self.__backdrop_image = image
        self.pixmap.load(self.__backdrop_image)

    def paintEvent(self, event):
        self.painter.begin(self)
        self.draw()
        self.painter.end()

    def draw(self):
        rect = self.rect()
        scaled_image = self.pixmap

        scaled_image = self.pixmap.scaledToWidth(rect.width(), Qt.SmoothTransformation)

        if scaled_image.height() < rect.height():
            scaled_image = self.pixmap.scaledToHeight(rect.height(), Qt.SmoothTransformation)

        image_rect = QRect(rect.x(), rect.y(), scaled_image.width(), scaled_image.height())
        image_rect.moveCenter(rect.center())

        self.painter.drawPixmap(image_rect, scaled_image)

        self.painter.setBrush(self.fill_brush)
        #self.painter.setPen(Qt.NoPen)
        self.painter.drawRect(rect)
        
    
if __name__ == '__main__':

    class TestClass:
        def __init__(self):
            # private adattag
            self.__val = 10

        # getter metódus
        @property
        def val(self):
            return self.__val

        @val.setter
        def val(self, value):
            self.__val = value        


    test = TestClass()
    test.val = 15
    print(test.val)
    #test._TestClass__val = 20
    #print(test._TestClass__val
    
    import sys

    app = QApplication(sys.argv)
    win = BackDropImageWidget()
    win.backdrop_image = r"C:\Users\kovac\movie_meta_images\f91517d0-c89c-4bb4-b360-b154f238b98b_backdrop.jpg"
    win.show()
    app.exec()