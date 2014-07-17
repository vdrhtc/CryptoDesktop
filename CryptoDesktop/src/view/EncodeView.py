'''
Created on 12 июля 2014 г.

@author: gleb
'''

from PyQt4.QtGui import *
from controller.Controller import Controller

class EncodeView(QWidget):
    '''
    Class that builds an Encode view
    '''
    inputBox = None
    outputBox = None
   
    def __init__(self):
        super().__init__()
        self.buildEncodeView()
    
    def encode_handler(self):
        self.outputBox.setText(Controller.handle_encoding(self.inputBox.toPlainText()))

    def makeEncodeButton(self, base):
        encodeButton = QPushButton('Encode')
        encodeButton.clicked.connect(self.encode_handler)
        base.addWidget(encodeButton)


    def makeInputTextBox(self, base):
        self.inputBox = QTextEdit()
        base.addWidget(self.inputBox)


    def makeOutputTextBox(self, base):
        outputBox = QTextEdit()
        outputBox.setReadOnly(True)
        self.outputBox = outputBox
        base.addWidget(outputBox)

    def buildEncodeView(self):
        base = QVBoxLayout(self)
        base.addWidget(QLabel("Enter text to encode:"))
        self.makeInputTextBox(base)
        self.makeEncodeButton(base)
        base.addWidget(QLabel("Cyphered text:"))
        self.makeOutputTextBox(base)

        
