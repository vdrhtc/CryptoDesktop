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

    def __init__(self, clipboard):
        super().__init__()
        self.clipboard = clipboard
        self.buildDecodeView()
    
    def decode_handler(self):
        if self.readFromClipboard.isChecked():
            self.outputBox.setText(Controller.handle_decoding(self.clipboard.text()))
        else:
            self.outputBox.setText(Controller.handle_decoding(self.inputBox.toPlainText()))
        
    def mode_switcher(self):
        if self.readFromClipboard.isChecked():
            self.inputBox.hide()
            self.inputLabel.setText("Reading from clipboard")
        else:
            self.inputBox.show()
            self.inputLabel.setText("Enter cyphered text to decode:")
        
    def makeInputTextBox(self, base):
        self.inputBox = QTextEdit()
        return base.addWidget(self.inputBox,1,0,1,2)


    def makeDecodeControls(self, base):
        self.readFromClipboard = QCheckBox('Read from clipboard')
        self.readFromClipboard.stateChanged.connect(self.mode_switcher)
        decodeButton = QPushButton('Decode')
        decodeButton.clicked.connect(self.decode_handler)
        base.addWidget(decodeButton)
        base.addWidget(self.readFromClipboard)


    def makeOutputTextBox(self, base):
        self.outputBox = QTextEdit()
        self.outputBox.setReadOnly(True)
        base.addWidget(self.outputBox)

    def buildDecodeView(self):
        base = QGridLayout(self)
        self.inputLabel = QLabel("Enter cyphered text to decode:")
        base.addWidget(self.inputLabel, 0, 0, 1, 2)
        self.makeInputTextBox(base)
        self.makeDecodeControls(base)
        base.addWidget(QLabel("Text:"), 3, 0)
        self.makeOutputTextBox(base)