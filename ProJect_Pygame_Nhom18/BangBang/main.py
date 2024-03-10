import sys
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtCore import pyqtSlot
import subprocess
#import thư viện pygame để chạy nhạc nền
import pygame 

class App(QWidget):
#khởi tạo cửa sổ ứng dụng với tiêu đề, kích thước và vị trí cụ thể
    def __init__(self):
        super().__init__()
        self.title = 'PROJECT PYGAME NHÓM 18'
        self.left = 700
        self.top = 300
        self.width = 728
        self.height = 410
        self.initUI()
   
  

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Phát nhạc khi mở game
        pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound('ProJect_Pygame_Nhom18/BangBang/sounds/musicbg.wav')

        sound.set_volume(0.5)
        sound.play()

        # Tạo label hiển thị hình ảnh
        label = QLabel(self)
        pixmap = QPixmap('ProJect_Pygame_Nhom18/BangBang/images/background.png')
        label.setPixmap(pixmap)
        label.setGeometry(0, 0, self.width, self.height)

        # Tạo 2 button, mỗi button là 1 game
    
        btn1 = QPushButton('Tank PvP', self)
        btn1.move(90, 370) #đặt nút btn1 ở vị trí có tọa độ x: 230 và y: 350 trên cửa sổ giao diện
        btn1.clicked.connect(self.on_click_mode1)

        btn2 = QPushButton('Crazy Tank', self)
        btn2.move(300, 370) #đặt nút btn2 ở vị trí có tọa độ x: 380 và y: 350 trên cửa sổ giao diện
        btn2.clicked.connect(self.on_click_mode2)

        # Tạo button thoát
        btn_exit = QPushButton('Thoát', self)
        btn_exit.move(510, 370) #đặt nút exit ở vị trí có tọa độ x: 230 và y: 350 trên cửa sổ giao diện
        btn_exit.clicked.connect(self.on_click_exit)

        self.show()

    #click vào button Tank PvP để chạy TankPvP.py
    @pyqtSlot()
    def on_click_mode1(self):
        subprocess.run(['python', 'ProJect_Pygame_Nhom18/BangBang/tank-game-master/TankPvP.py'])
 
    #click vào button Crazy Tank để chạy game CrazyTank.py
    @pyqtSlot()
    def on_click_mode2(self):
        subprocess.run(['python', 'ProJect_Pygame_Nhom18/BangBang/CrazyTank.py'])

    @pyqtSlot()
    def on_click_exit(self):
        # Thoát chương trình
        QApplication.quit()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
