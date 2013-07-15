#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-

'''
@description A cpp interpreter main.
@author Lhfcws Wu 
@time 2013-07-15
'''

from cpp_interpreter import CPPInterpreter

def main():
    interpreter = CPPInterpreter()
    interpreter.execute('h')

    while interpreter.nexit:
        interpreter.getline()

    print 'C++ interpreter exited!'

###########

if __name__ == '__main__':
    main()
