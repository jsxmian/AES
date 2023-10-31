from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel

from s_aes import encrypt
from s_aes import decrypt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Application")
        self.setGeometry(100,100,400,300)
        # ----------------------------------基本测试----------------------------------------------
        self.label0 = QLabel(self)
        self.label0.setText("S-AES")
        self.label0.setGeometry(100, 20, 60, 30)
        self.label1 = QLabel(self)
        self.label1.setText("输入:")
        self.label1.setGeometry(0, 50, 40, 30)
        # 第一个输入框
        self.input1 = QLineEdit(self)
        self.input1.setGeometry(50, 50, 200, 30)
        self.input1.setToolTip("请输入16位二进制数")
        self.input1.setText("1101011100101000")

        # 第二个输入框
        self.label2 = QLabel(self)
        self.label2.setText("密钥:")
        self.label2.setGeometry(0, 100, 40, 30)
        self.input2 = QLineEdit(self)
        self.input2.setGeometry(50, 100, 200, 30)
        self.input2.setToolTip("请输入16位二进制数")
        self.input2.setText("0100101011110101")

        # 第二个输入框
        self.label3 = QLabel(self)
        self.label3.setText("输出:")
        self.label3.setGeometry(0, 150, 40, 30)
        self.input3 = QLineEdit(self)
        self.input3.setGeometry(50, 150, 200, 30)

        # 第二个输入框
        self.label4 = QLabel(self)
        self.label4.setText("解密:")
        self.label4.setGeometry(0, 200, 40, 30)
        self.input5 = QLineEdit(self)
        self.input5.setGeometry(50, 200, 200, 30)

        # 确认按钮
        self.button = QPushButton("确认", self)
        self.button.setGeometry(260, 50, 50, 30)
        self.button.clicked.connect(self.encrypt)

        # 确认按钮
        self.button1 = QPushButton("确认", self)
        self.button1.setGeometry(260, 200, 50, 30)
        self.button1.clicked.connect(self.decrypt)


    def decrypt(self):
        encrypt = int(self.input3.text(), 2)
        key = int(self.input2.text(), 2)
        print(encrypt)
        print(key)
        encrypt = decrypt(encrypt, key)
        print(encrypt)
        self.input5.setText(str(bin(encrypt))[2:])
    # 基本
    def encrypt(self):
        plaintext = int(self.input1.text(), 2)
        key = int(self.input2.text(), 2)
        print(plaintext)
        print(key)
        ciphertext = encrypt(plaintext, key)
        print(ciphertext)
        self.input3.setText(str(bin(ciphertext))[2:])



app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
