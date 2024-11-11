from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout

from LePhuocThinh_K234161856.ThanhThang.MainWindowHoaExt import MainWindowHoaExt

app=QApplication([])
myWindow= MainWindowHoaExt()
myWindow.setupUi(QMainWindow())
myWindow.processChangeGIF()
myWindow.show()
app.exec()