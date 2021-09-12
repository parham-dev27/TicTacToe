#parhamTheDeveloper
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(402, 402)
        MainWindow.setMinimumSize(QtCore.QSize(402, 402))
        MainWindow.setMaximumSize(QtCore.QSize(402, 402))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self._1 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.click_b_P(1))
        self._1.setGeometry(QtCore.QRect(0, 0, 134, 134))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(90)
        self._1.setFont(font)
        self._1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self._1.setStyleSheet("background-color: rgb(169, 169, 169);")
        self._1.setObjectName("_1")
        self._2 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.click_b_P(2))
        self._2.setGeometry(QtCore.QRect(134, 0, 134, 134))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(90)
        self._2.setFont(font)
        self._2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self._2.setStyleSheet("background-color: rgb(192, 192, 192);")
        self._2.setObjectName("_2")
        self._3 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.click_b_P(3))
        self._3.setGeometry(QtCore.QRect(268, 0, 134, 134))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(90)
        self._3.setFont(font)
        self._3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self._3.setStyleSheet("background-color: rgb(169, 169, 169);")
        self._3.setObjectName("_3")
        self._5 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.click_b_P(5))
        self._5.setGeometry(QtCore.QRect(134, 134, 134, 134))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(90)
        self._5.setFont(font)
        self._5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self._5.setStyleSheet("background-color: rgb(169, 169, 169);")
        self._5.setObjectName("_5")
        self._7 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.click_b_P(7))
        self._7.setGeometry(QtCore.QRect(0, 268, 134, 134))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(90)
        self._7.setFont(font)
        self._7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self._7.setStyleSheet("background-color: rgb(169, 169, 169);")
        self._7.setObjectName("_7")
        self._9 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.click_b_P(9))
        self._9.setGeometry(QtCore.QRect(268, 268, 134, 134))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(90)
        self._9.setFont(font)
        self._9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self._9.setStyleSheet("background-color: rgb(169, 169, 169);")
        self._9.setObjectName("_9")
        self._6 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.click_b_P(6))
        self._6.setGeometry(QtCore.QRect(268, 134, 134, 134))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(90)
        self._6.setFont(font)
        self._6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self._6.setStyleSheet("background-color: rgb(192, 192, 192);")
        self._6.setObjectName("_6")
        self._8 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.click_b_P(8))
        self._8.setGeometry(QtCore.QRect(134, 268, 134, 134))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(90)
        self._8.setFont(font)
        self._8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self._8.setStyleSheet("background-color: rgb(192, 192, 192);")
        self._8.setObjectName("_8")
        self._4 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.click_b_P(4))
        self._4.setGeometry(QtCore.QRect(0, 134, 134, 134))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(90)
        self._4.setFont(font)
        self._4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self._4.setStyleSheet("background-color: rgb(192, 192, 192);")
        self._4.setObjectName("_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.Openli = [1, 2, 3,
                        4, 5, 6,
                        7, 8, 9]
        self.listBoard = {1: "",
        2:"",
        3:"",
        4:"",
        5:"",
        6:"",
        7:"",
        8:"",
        9:""}
    def click_b_P(self, num):
        num = int(num)
        if num == 1:
                self._1.setStyleSheet("color: rgb(148, 17, 0);\nbackground-color: rgb(169, 169, 169);")
                self._1.setText("X")
                self._1.setEnabled(False)
                self.Openli.remove(1)
                self.listBoard[1] = "X"
                try:
                        self.winCheck()
                        self.computer_Move()
                except:
                        pass
        elif num == 2:
                self._2.setStyleSheet("color: rgb(148, 17, 0);\nbackground-color: rgb(192, 192, 192);")
                self._2.setText("X")
                self._2.setEnabled(False)
                self.Openli.remove(2)
                self.listBoard[2] = "X"
                try:
                        self.winCheck()
                        self.computer_Move()
                except:
                        pass
        elif num == 3:
                self._3.setStyleSheet("color: rgb(148, 17, 0);\nbackground-color: rgb(169, 169, 169);")
                self._3.setText("X")
                self._3.setEnabled(False)
                self.Openli.remove(3)
                self.listBoard[3] = "X"
                try:
                        self.winCheck()
                        self.computer_Move()
                except:
                        pass
        elif num == 4:
                self._4.setStyleSheet("color: rgb(148, 17, 0);\nbackground-color: rgb(192, 192, 192);")
                self._4.setText("X")
                self._4.setEnabled(False)
                self.Openli.remove(4)
                self.listBoard[4] = "X"
                try:
                        self.winCheck()
                        self.computer_Move()
                except:
                        pass
        elif num == 5:
                self._5.setStyleSheet("color: rgb(148, 17, 0);\nbackground-color: rgb(169, 169, 169);")
                self._5.setText("X")
                self._5.setEnabled(False)
                self.Openli.remove(5)
                self.listBoard[5] = "X"
                try:
                        self.winCheck()
                        self.computer_Move()
                except:
                        pass
        elif num == 6:
                self._6.setStyleSheet("color: rgb(148, 17, 0);\nbackground-color: rgb(192, 192, 192);")
                self._6.setText("X")
                self._6.setEnabled(False)
                self.Openli.remove(6)
                self.listBoard[6] = "X"
                try:
                        self.winCheck()
                        self.computer_Move()
                except:
                        pass
        elif num == 7:
                self._7.setStyleSheet("color: rgb(148, 17, 0);\nbackground-color: rgb(169, 169, 169);")
                self._7.setText("X")
                self._7.setEnabled(False)
                self.Openli.remove(7)
                self.listBoard[7] = "X"
                try:
                        self.winCheck()
                        self.computer_Move()
                except:
                        pass
        elif num == 8:
                self._8.setStyleSheet("color: rgb(148, 17, 0);\nbackground-color: rgb(192, 192, 192);")
                self._8.setText("X")
                self._8.setEnabled(False)
                self.Openli.remove(8)
                self.listBoard[8] = "X"
                try:
                        self.winCheck()
                        self.computer_Move()
                except:
                        pass
        elif num == 9:
                self._9.setStyleSheet("color: rgb(148, 17, 0);\nbackground-color: rgb(169, 169, 169);")
                self._9.setText("X")
                self._9.setEnabled(False)
                self.Openli.remove(9)
                self.listBoard[9] = "X"
                try:
                        self.winCheck()
                        self.computer_Move()
                except:
                        pass

    def computer_Move(self):
        from random import choice
        rand = choice(self.Openli)
        if rand == 1:
                self._1.setStyleSheet("color: rgb(0, 116, 11);\nbackground-color: rgb(169, 169, 169);")
                self._1.setText("O")
                self._1.setEnabled(False)
                self.Openli.remove(1)
                self.listBoard[1] = "O"
                self.winCheck()
        elif rand == 2:
                self._2.setStyleSheet("color: rgb(0, 116, 11);\nbackground-color: rgb(192, 192, 192);")
                self._2.setText("O")
                self._2.setEnabled(False)
                self.Openli.remove(2)
                self.listBoard[2] = "O"
                self.winCheck()
        elif rand == 3:
                self._3.setStyleSheet("color: rgb(0, 116, 11);\nbackground-color: rgb(169, 169, 169);")
                self._3.setText("O")
                self._3.setEnabled(False)
                self.Openli.remove(3)
                self.listBoard[3] = "O"
                self.winCheck()

        elif rand == 4:
                self._4.setStyleSheet("color: rgb(0, 116, 11);\nbackground-color: rgb(192, 192, 192);")
                self._4.setText("O")
                self._4.setEnabled(False)
                self.Openli.remove(4)
                self.listBoard[4] = "O"
                self.winCheck()

        elif rand == 5:
                self._5.setStyleSheet("color: rgb(0, 116, 11);\nbackground-color: rgb(169, 169, 169);")
                self._5.setText("O")
                self._5.setEnabled(False)
                self.Openli.remove(5)
                self.listBoard[5] = "O"
                self.winCheck()

        elif rand == 6:
                self._6.setStyleSheet("color: rgb(0, 116, 11);\nbackground-color: rgb(192, 192, 192);")
                self._6.setText("O")
                self._6.setEnabled(False)
                self.Openli.remove(6)
                self.listBoard[6] = "O"
                self.winCheck()

        elif rand == 7:
                self._7.setStyleSheet("color: rgb(0, 116, 11);\nbackground-color: rgb(169, 169, 169);")
                self._7.setText("O")
                self._7.setEnabled(False)
                self.Openli.remove(7)
                self.listBoard[7] = "O"
                self.winCheck()

        elif rand == 8:
                self._8.setStyleSheet("color: rgb(0, 116, 11);\nbackground-color: rgb(192, 192, 192);")
                self._8.setText("O")
                self._8.setEnabled(False)
                self.Openli.remove(8)
                self.listBoard[8] = "O"
                self.winCheck()

        elif rand == 9:
                self._9.setStyleSheet("color: rgb(0, 116, 11);\nbackground-color: rgb(169, 169, 169);")
                self._9.setText("O")
                self._9.setEnabled(False)
                self.Openli.remove(9)
                self.listBoard[9] = "O"
                self.winCheck()


    def winCheck(self):
        if self.listBoard[1] == "X" and self.listBoard[2] == "X" and self.listBoard[3] == "X":
                self.win()
                raise ValueError
        elif self.listBoard[4] == "X" and self.listBoard[5] == "X" and self.listBoard[6] == "X":
                self.win()
                raise ValueError
        elif self.listBoard[7] == "X" and self.listBoard[8] == "X" and self.listBoard[9] == "X":
              self.win()
              raise ValueError
        elif self.listBoard[1] == "X" and self.listBoard[4] == "X" and self.listBoard[7] == "X":
                self.win()
                raise ValueError
        elif self.listBoard[2] == "X" and self.listBoard[5] == "X" and self.listBoard[8] == "X":
                self.win()
                raise ValueError
        elif self.listBoard[3] == "X" and self.listBoard[6] == "X" and self.listBoard[9] == "X":
                self.win()
                raise ValueError
        elif self.listBoard[1] == "X" and self.listBoard[5] == "X" and self.listBoard[9] == "X":
                self.win()
                raise ValueError
        elif self.listBoard[3] == "X" and self.listBoard[5] == "X" and self.listBoard[7] == "X":
                self.win()
                raise ValueError
        if self.listBoard[1] == "O" and self.listBoard[2] == "O" and self.listBoard[3] == "O":
                self.lose()
                raise ValueError
        elif self.listBoard[4] == "O" and self.listBoard[5] == "O" and self.listBoard[6] == "O":
                self.lose()
                raise ValueError
        elif self.listBoard[7] == "O" and self.listBoard[8] == "O" and self.listBoard[9] == "O":
              self.lose()
              raise ValueError
        elif self.listBoard[1] == "O" and self.listBoard[4] == "O" and self.listBoard[7] == "O":
                self.lose()
                raise ValueError
        elif self.listBoard[2] == "O" and self.listBoard[5] == "O" and self.listBoard[8] == "O":
                self.lose()
                raise ValueError
        elif self.listBoard[3] == "O" and self.listBoard[6] == "O" and self.listBoard[9] == "O":
                self.lose()
                raise ValueError
        elif self.listBoard[1] == "O" and self.listBoard[5] == "O" and self.listBoard[9] == "O":
                self.lose()
                raise ValueError
        elif self.listBoard[3] == "O" and self.listBoard[5] == "O" and self.listBoard[7] == "O":
                self.lose()
                raise ValueError
        if bool(self.listBoard[1]) and bool(self.listBoard[2]) and bool(self.listBoard[3]) and bool(self.listBoard[4]) and bool(self.listBoard[5]) and bool(self.listBoard[6]) and bool(self.listBoard[7]) and bool(self.listBoard[8]) and bool(self.listBoard[9]):
                self.tie()


    def tie(self):
        self._9.setStyleSheet("background-color: rgb(169, 169, 169);")
        self._8.setStyleSheet("background-color: rgb(192, 192, 192);")
        self._7.setStyleSheet("background-color: rgb(169, 169, 169);")
        self._6.setStyleSheet("background-color: rgb(192, 192, 192);")
        self._5.setStyleSheet("background-color: rgb(169, 169, 169);")
        self._4.setStyleSheet("background-color: rgb(192, 192, 192);")
        self._3.setStyleSheet("background-color: rgb(169, 169, 169);")
        self._2.setStyleSheet("background-color: rgb(192, 192, 192);")
        self._1.setStyleSheet("background-color: rgb(169, 169, 169);")
        self._1.setText("")
        self._2.setText("")
        self._3.setText("")
        self._4.setText("T")
        self._5.setText("I")
        self._6.setText("E")
        self._7.setText("")
        self._8.setText("")
        self._9.setText("")
        self._1.setEnabled(False)
        self._2.setEnabled(False)
        self._3.setEnabled(False)
        self._4.setEnabled(False)
        self._5.setEnabled(False)
        self._6.setEnabled(False)
        self._7.setEnabled(False)
        self._8.setEnabled(False)
        self._9.setEnabled(False)

    def lose(self):
        self._9.setStyleSheet("color: rgb(148, 17, 0);\nbackground-color: rgb(169, 169, 169);")
        self._8.setStyleSheet("color: rgb(148, 17, 0);\nbackground-color: rgb(192, 192, 192);")
        self._7.setStyleSheet("color: rgb(148, 17, 0);\nbackground-color: rgb(169, 169, 169);")
        self._6.setStyleSheet("color: rgb(148, 17, 0);\nbackground-color: rgb(192, 192, 192);")
        self._5.setStyleSheet("color: rgb(148, 17, 0);\nbackground-color: rgb(169, 169, 169);")
        self._4.setStyleSheet("color: rgb(148, 17, 0);\nbackground-color: rgb(192, 192, 192);")
        self._3.setStyleSheet("color: rgb(148, 17, 0);\nbackground-color: rgb(169, 169, 169);")
        self._2.setStyleSheet("color: rgb(148, 17, 0);\nbackground-color: rgb(192, 192, 192);")
        self._1.setStyleSheet("color: rgb(148, 17, 0);\nbackground-color: rgb(169, 169, 169);")
        self._1.setText("Y")
        self._2.setText("O")
        self._3.setText("U")
        self._4.setText("L")
        self._5.setText("O")
        self._6.setText("")
        self._7.setText("")
        self._8.setText("S")
        self._9.setText("T")
        self._1.setEnabled(False)
        self._2.setEnabled(False)
        self._3.setEnabled(False)
        self._4.setEnabled(False)
        self._5.setEnabled(False)
        self._6.setEnabled(False)
        self._7.setEnabled(False)
        self._8.setEnabled(False)
        self._9.setEnabled(False)

    def win(self):
        self._9.setStyleSheet("color: rgb(0, 116, 11);\nbackground-color: rgb(169, 169, 169);")
        self._8.setStyleSheet("color: rgb(0, 116, 11);\nbackground-color: rgb(192, 192, 192);")
        self._7.setStyleSheet("color: rgb(0, 116, 11);\nbackground-color: rgb(169, 169, 169);")
        self._6.setStyleSheet("color: rgb(0, 116, 11);\nbackground-color: rgb(192, 192, 192);")
        self._5.setStyleSheet("color: rgb(0, 116, 11);\nbackground-color: rgb(169, 169, 169);")
        self._4.setStyleSheet("color: rgb(0, 116, 11);\nbackground-color: rgb(192, 192, 192);")
        self._3.setStyleSheet("color: rgb(0, 116, 11);\nbackground-color: rgb(169, 169, 169);")
        self._2.setStyleSheet("color: rgb(0, 116, 11);\nbackground-color: rgb(192, 192, 192);")
        self._1.setStyleSheet("color: rgb(0, 116, 11);\nbackground-color: rgb(169, 169, 169);")
        self._1.setText("Y")
        self._2.setText("O")
        self._3.setText("U")
        self._4.setText("")
        self._5.setText("")
        self._6.setText("")
        self._7.setText("W")
        self._8.setText("O")
        self._9.setText("N")
        self._1.setEnabled(False)
        self._2.setEnabled(False)
        self._3.setEnabled(False)
        self._4.setEnabled(False)
        self._5.setEnabled(False)
        self._6.setEnabled(False)
        self._7.setEnabled(False)
        self._8.setEnabled(False)
        self._9.setEnabled(False)

          
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TicTacToe"))
        self._1.setText(_translate("MainWindow", ""))
        self._2.setText(_translate("MainWindow", ""))
        self._3.setText(_translate("MainWindow", ""))
        self._5.setText(_translate("MainWindow", ""))
        self._7.setText(_translate("MainWindow", ""))
        self._9.setText(_translate("MainWindow", ""))
        self._6.setText(_translate("MainWindow", ""))
        self._8.setText(_translate("MainWindow", ""))
        self._4.setText(_translate("MainWindow", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
