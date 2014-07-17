'''
Created on 12 июля 2014 г.

@author: gleb
'''

from PyQt4.QtGui import *

class EncodeView(QWidget):
    '''
    Class that builds an Encode view
    '''

    def __init__(self):
        super().__init__()
        self.buildEncodeView()
    
    def buildEncodeView(self):
        base = QVBoxLayout(self)
        base.addWidget(QLabel("Enter text to encode:"))
        base.addWidget(QTextEdit())
        base.addWidget(QPushButton('Encode'))
        base.addWidget(QLabel("Cyphered text:"))
        outputBox = QTextEdit()
        outputBox.setReadOnly(True)
        base.addWidget(outputBox)

        
