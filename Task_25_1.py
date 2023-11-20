### Task_25_1
'''
Простой вариант:
Разработайте счётчик нажатий на кнопку,
который меняет свою надпись на число нажатий на неё (1, 2, 3, и т.д.)
'''

# Окно с кнопкой при нажатии которой
# бесконечно меняется надпись на кнопке 'Press Me!' на 'Other'
# и печатается 'Clicked!'
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
class MainWindow(QMainWindow): # подкласс для настройки главного окна
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My App')  # определяем окно с надписью
        self.button = QPushButton('Press Me!') # определяем кнопку с надписью
        self.button.setCheckable(True)  # определяем что кнопка button будет запоминать своё состояние (нажата/отжата)
     #     кто     #что с ним#
     #             # сделали:# connect(имя метода который ...
     # self.button #.clicked # будет управлять действиями после нажатия (clicked) кнопки button
        self.button.clicked.connect(self.the_button_was_clicked)
        self.setCentralWidget(self.button)
        self.status = '0'

    def the_button_was_clicked(self):
        self.status = str(int(self.status) + 1)
        self.button.setText(self.status)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()