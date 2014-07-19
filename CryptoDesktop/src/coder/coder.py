'''
Created on 18 июля 2014 г.

@author: gleb

'''
from numpy import *

def encode(text):
    if len(text)==0:
        return text
    
    initial_sequence = array([ord(char) for char in text])
    sequence = create_matrix(len(text)).dot(initial_sequence.T)
    return repr(sequence)

def decode(encoded_text):
    column = eval(encoded_text).T
    inversed_matrix = create_matrix(len(column)).I
    final_sequence = inversed_matrix * column
    return ''.join([chr(int(round(x))) for x in array(final_sequence)[:,0]])

    
def create_matrix(n):
    rows = []
    for i in range (0, n):
        rows.append([ 2**(i%5) + (-1)**(n+i)*3*(x%5) for x in range(0, n)])
    res_matrix = matrix(rows)
    
    while(linalg.det(res_matrix)==0):
        res_matrix+=eye(n)
    print(res_matrix)     
    return res_matrix