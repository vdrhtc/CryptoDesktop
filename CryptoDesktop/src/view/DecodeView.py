'''
Created on 17 июля 2014 г.

@author: gleb
'''

from PyQt4.QtGui import *
from controller.Controller import Controller
class DecodeView(QWidget):
    '''
    Class that builds decode view
    '''

    def __init__(self):
        super().__init__()
        self.buildDecodeView()
    
    def decode_handler(self):
        self.outputBox.setText(Controller.handle_decoding(self.inputBox.toPlainText()))
        
    def makeInputTextBox(self, base):
        self.inputBox = QTextEdit()
        return base.addWidget(self.inputBox)


    def makeDecodeButton(self, base):
        decodeButton = QPushButton('Decode')
        decodeButton.clicked.connect(self.decode_handler)
        return base.addWidget(decodeButton)


    def makeOutputTextBox(self, base):
        self.outputBox = QTextEdit()
        self.outputBox.setReadOnly(True)
        base.addWidget(self.outputBox)

    def buildDecodeView(self):
        base = QVBoxLayout(self)
        base.addWidget(QLabel("Enter cyphered text to decode:"))
        self.makeInputTextBox(base)
        self.makeDecodeButton(base)
        base.addWidget(QLabel("Text:"))
        self.makeOutputTextBox(base)