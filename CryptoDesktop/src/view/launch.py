'''
Created on 12 июля 2014 г.

@author: gleb
'''

from PyQt4 import QtGui
import sys

from view.EncodeView import EncodeView
from view.DecodeView import DecodeView

class Window(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()
        Window.EV = EncodeView()
        Window.DV = DecodeView()

    def initializeWindow(self):
        self.resize(250, 150)
        self.move(300, 300)
        self.setWindowTitle('Crypto')
        self.statusBar().showMessage("Ready")
        tabWidget = QtGui.QTabWidget()
        tabWidget.addTab(self.EV, 'Encode')
        tabWidget.addTab(self.DV, 'Decode')
        self.setCentralWidget(tabWidget)
          
        self.show()

        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    W = Window()
    W.initializeWindow()
    sys.exit(app.exec_())
