from PyQt6.QtGui import QMovie

from LePhuocThinh_K234161856.ThanhThang.MainWindowHoa import Ui_MainWindow


class MainWindowHoaExt(Ui_MainWindow):
    gia_hoa = 19

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()

    def setupSignalAndSlot(self):
        self.pushButtonMua.clicked.connect(self.xuly_mua)

    def xuly_mua(self):
        SlDala = int(self.lineEditSlDL.text())
        SlSapa = int(self.lineEditSlSapa.text())

        so_tien_Dl = SlDala*100*0.85
        so_tien_Sapa = SlSapa*100
        self.lineEditSapa.setText(f"{SlSapa}")
        self.lineEditTienSapa.setText(f"{so_tien_Sapa}")
        self.lineEditDL.setText(f"{SlDala}")
        self.lineEditTienDL.setText(f"{so_tien_Dl}")



        total = so_tien_Dl + so_tien_Sapa
        self.lineEditTongDoanhSo.setText(f"{total}")

    def processChangeGIF(self):
        movie = QMovie("Matirial/gif/flower.gif")
        self.imagegif.setMovie(movie)
        movie.start()

    def show(self):
            self.MainWindow.show()
