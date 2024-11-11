from LePhuocThinh_K234161856.KhauHao.MainWindowKhauHao import Ui_MainWindow


class MainWindowKhauHaoExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def setupSignalAndSlot(self):
        self.pushButtonThucHien.clicked.connect(self.xuly)
        self.pushButtonThoat.clicked.connect(self.thoat)
        self.pushButtonThucHien_3.clicked.connect(self.lammoi)

    def xuly(self):
        C0= float(self.lineEditC0.text())
        Ct = float(self.lineEditCt.text())
        t = float(self.lineEditT.text())
        r = float(self.lineEditR.text())

        i = 1
        S = 0
        while i <= t:
            C = Ct / ((1 + r) ** i)
            S = S + C
            i = i + 1

        NPV = S - C0

        self.lineEditNPV.setText(f"{NPV}")

        if NPV > 0:
            self.lineEdit_6.setText("Dự án sinh lời, nên đầu tư.")
        elif NPV < 0:
            self.lineEdit_6.setText("Dự án không sinh lời, không nên đầu tư.")
        else:
            self.lineEdit_6.setText("Dự án hòa vốn.")

    def thoat(self):
        self.MainWindow.close()

    def lammoi(self):
        self.lineEditC0.setText("")
        self.lineEditR.setText("")
        self.lineEditCt.setText("")
        self.lineEditT.setText("")
        self.lineEdit_6.setText("")
        self.lineEditNPV.setText("")
        self.lineEditC0.setFocus()
    def show(self):
        self.MainWindow.show()


