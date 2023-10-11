import sys
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QDialog

class user_login(QDialog):
    def __init__(self):
        super(user_login,self).__init__()
        loadUi("login.ui", self)
        self.submit_button.clicked.connect(self.user_function)
        
    def user_function(self):
        process = self.process_id.text()
        arrival = self.Arrival_time.text()
        burst = self.Burst_time.text()
        print("Process Id: ", process, " Arrival Time: ", arrival, " Burst Time: ", burst)
        
app = QApplication(sys.argv)
mainwindow = user_login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.show()
app.exec_()
