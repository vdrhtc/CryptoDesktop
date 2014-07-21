'''
Created on 21 июля 2014 г.

@author: elvira
'''

from PyQt4.QtGui import *
from distutils.command.build import build

class OptionsView(QWidget):
    '''
    Options for the application
    '''

    def __init__(self):
        super().__init__()
        self.build_options_view()
        
    def get_matrix_building_rule(self):
        if self.methodBox.toPlainText() == '':
            return '2**(y%5) + (-1)**(y+x)*3*(x%5)'
        return self.methodBox.toPlainText()
    
    def method_area_visibility_toggler(self):
        self.methodBox.setVisible(self.methodBox.isHidden())
        
    def makeMethodBoxArea(self, base):
        methodBoxToggler = QPushButton("Matrix filling rule")
        self.methodBox = QTextEdit()
        methodBoxToggler.clicked.connect(self.method_area_visibility_toggler)
        base.addWidget(methodBoxToggler)
        base.addWidget(self.methodBox)
        self.methodBox.hide()
    
    def build_options_view(self):
        base = QGridLayout(self)
        self.makeMethodBoxArea(base)