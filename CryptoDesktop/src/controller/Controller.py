'''
Created on 17 июля 2014 г.

@author: gleb
'''
from coder.coder import *

class Controller(object):
    '''
    Class that operates this application
    '''
        
    @staticmethod
    def handle_encoding(text, method):
        return encode(text, method)
    
    @staticmethod
    def handle_decoding(text, method):
        return decode(text, method)
        