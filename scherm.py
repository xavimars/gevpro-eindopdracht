#!usr/bin/python3.4

import os,sys
from PyQt4 import QtGui, QtCore


    

class scherm(QtGui.QWidget):

    def __init__(self):
        super(scherm, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 500, 300)
        self.setWindowTitle('TwieTwiet')

        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(4)
        self.Button_one = QtGui.QPushButton('New TwieTwiet', self)

        tweet1 = QtGui.QLabel('Test1', self)
        tweet1.resize(500, 50)
        tweet1.move(20, 0)

        tweet2 = QtGui.QLabel('Test2', self)
        tweet2.resize(500,100)
        tweet2.move(20, 70) 
        
        self.Button_one.move(200, 200)
        self.Button_one.resize(100, 50)

        
        self.show()



def main():

    app = QtGui.QApplication(sys.argv)
    sc = scherm()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
