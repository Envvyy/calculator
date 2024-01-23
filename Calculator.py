from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class YourMainWindow(QMainWindow):
    def __init__(self):
        super(YourMainWindow, self).__init__()
        uic.loadUi('C:\\Users\\Marat\\Desktop\\PythonProjects\\Калькулятор\\untitled.ui', self)
        

if __name__ == "__main__":
    app = QApplication([])
    main_window = YourMainWindow()
    main_window.show()
    app.exec_()
try:
    uic.loadUi('your_ui_file.ui', self)
except Exception as e:
    print(f"Error loading UI file: {e}")