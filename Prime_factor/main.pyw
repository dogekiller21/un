from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from project import Ui_MainWindow
if __name__ == "__main__":

    # Start
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # Logic

    def is_number(str):
        try:
            float(str)
            return True
        except ValueError:
            return False

    def count():
        k = ui.lineEdit.text()
        if is_number(k) == True:
            k = int(k)
            n = k
            a = []
            i = 2
            while i < n + 1:
                if k % i == 0:
                    a.append(i)
                    k = k / i
                    i = 2
                else:
                    i += 1
            s = '\n'.join(str(e) for e in a)
            ui.label.setText(s)
        else:
            ui.label.setText('Error')
    ui.pushButton.clicked.connect(count)

    # Exit
    sys.exit(app.exec_())
