from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout

from LePhuocThinh_K234161856.KhauHao.MainWindowKhauHaoExt import MainWindowKhauHaoExt

app=QApplication([])
myWindow= MainWindowKhauHaoExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()