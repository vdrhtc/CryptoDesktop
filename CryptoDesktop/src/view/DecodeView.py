'''
Created on 17 июля 2014 г.

@author: gleb
'''

from PyQt4.QtGui import *

class DecodeView(QWidget):
    '''
    Class that builds decode view
    '''

    def __init__(self):
        super().__init__()
        self.buildDecodeView()
    
    def buildDecodeView(self):
        base = QVBoxLayout(self)
        base.addWidget(QLabel("Enter cyphered text to decode:"))
        base.addWidget(QTextEdit())
        base.addWidget(QPushButton('Decode'))
        base.addWidget(QLabel("Text:"))
        outputBox = QTextEdit()
        outputBox.setReadOnly(True)
        base.addWidget(outputBox)