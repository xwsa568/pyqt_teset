import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application') #창의 제목
        self.move(300, 300) #창의 위치 선정
        self.resize(400, 200) #창의 사이즈 조절

        btn = QPushButton('Quit', self)
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv) #어플리케이션 객체 생성
    ex = MyApp()
    sys.exit(app.exec_())