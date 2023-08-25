#!/usr/bin/env python3
import sys
from collections import OrderedDict

def decrypt_caesar(hex):

    letter_frequences = OrderedDict()
    letter_frequences['E'] = 1
    letter_frequences['T'] = 2
    letter_frequences['A'] = 3
    letter_frequences['I'] = 4
    letter_frequences['N'] = 5
    letter_frequences['O'] = 6
    letter_frequences['S'] = 7
    letter_frequences['H'] = 8
    

    byte_array = bytes.fromhex(hex)

    print(byte_array)

    frequencies = {}
    for b in byte_array:
        b = str(b)
        if frequencies.keys().__contains__(b):
            frequencies[b] += 1
        else:
            frequencies[b] = 1

    print(frequencies)

    #replace the most frequently occuring character with E, then the 2nd with T, etc
    for 
    
        


if __name__ == '__main__':
    decrypt_caesar(sys.argv[1])