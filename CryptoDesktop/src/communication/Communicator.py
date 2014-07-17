'''
Created on 17 июля 2014 г.

@author: gleb
'''

class Communicator():
    '''
    Static class which holds the data to exchange (single thread, no locks)
    ''' 
    
    # Exchange for encoding
    textToEncode = None
    encodedText = None
    
    #Exchange for decoding
    textToDecode = None
    text = None