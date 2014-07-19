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
   
    def __init__(self, clipboard):
        super().__init__()
        self.clipboard = clipboard
        self.buildEncodeView()
        
    def encode_handler(self):
        if not self.toClipboard.isChecked():
            self.outputBox.setText(Controller.handle_encoding(self.inputBox.toPlainText()))
        else:
            self.clipboard.setText(Controller.handle_encoding(self.inputBox.toPlainText()))
        
        
        
    def method_area_visibility_toggler(self):
        self.methodBox.setVisible(self.methodBox.isHidden())
    
    def mode_switcher(self):
        if self.toClipboard.isChecked():
            self.outputBox.hide()
            self.outputLabel.setText("Writing to clipboard")
        else:
            self.outputBox.show()
            self.outputLabel.setText("Cyphered text:")

    def makeEncodeControls(self, base):
        encodeButton = QPushButton('Encode')
        self.toClipboard = QCheckBox('Encode to clipboard')
        self.toClipboard.stateChanged.connect(self.mode_switcher)
        encodeButton.clicked.connect(self.encode_handler)
        
        base.addWidget(encodeButton)
        base.addWidget(self.toClipboard)


    def makeInputTextBox(self, base):
        self.inputBox = QTextEdit()
        base.addWidget(self.inputBox,1,0,1,2)


    def makeOutputTextBox(self, base):
        outputBox = QTextEdit()
        outputBox.setReadOnly(True)
        self.outputBox = outputBox
        base.addWidget(outputBox)


    def makeMethodBoxArea(self, base):
        methodBoxToggler = QPushButton("Matrix filling rule")
        self.methodBox = QTextEdit()
        methodBoxToggler.clicked.connect(self.method_area_visibility_toggler)
        base.addWidget(methodBoxToggler)
        base.addWidget(self.methodBox)
        self.methodBox.hide()

    def buildEncodeView(self):
        base = QGridLayout(self)
        base.setSpacing(10)
        self.inputLabel = QLabel("Enter text to encode:")
        base.addWidget(self.inputLabel, 0,0,1,2)
        self.makeInputTextBox(base)
        self.makeEncodeControls(base)
        self.outputLabel = QLabel("Cyphered text:")
        base.addWidget(self.outputLabel, 3,0)
        self.makeOutputTextBox(base)
        self.makeMethodBoxArea(base)