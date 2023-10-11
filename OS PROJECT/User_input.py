import sys
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox

class user_login(QDialog):
    def __init__(self):
        super(user_login, self).__init__()
        loadUi("login.ui", self)
        self.submit_button.clicked.connect(self.user_function)

    def user_function(self):
        process = self.process_id.text().split()
        arrival = self.Arrival_time.text().split()
        burst = self.Burst_time.text().split()

        if len(process) != len(arrival) or len(process) != len(burst) or len(arrival) != len(burst):
            QtWidgets.QMessageBox.critical(self, "Error", "Number of Process ID, Arrival Time, and Burst Time must be the same in list format.")
            return

        for p, a, b in zip(process, arrival, burst):
            print("Process Id:", p, "Arrival Time:", a, "Burst Time:", b)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = user_login()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.show()
    sys.exit(app.exec_())
