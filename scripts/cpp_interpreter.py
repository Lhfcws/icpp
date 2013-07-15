#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-

'''
@description A cpp interpreter.
@author Lhfcws Wu 
@time 2013-07-15
'''

import commands
import os

path = '/home/lhfcws/coding/projects/cpp_interpreter/scripts/'

class CPPInterpreter(object):
    def __init__(self):
        self.nexit = True                   # Exit flag
        self.has_main = False               # auto generate main flag
        self.pre_codes = '#include "headers.h"\n'   # Common headers
        self.codes = [self.pre_codes]               # normal codes
        self.src = path + '../temp_src/src.cpp'            # temp source code path
        self.bin = path + '../temp_src/exe'                # temp binary file path
        self.help_src = path + '../help.txt'               # Help text
        self.compile_cmd = 'g++ ' + self.src + ' -o ' + self.bin    # Compile command in shell

        # Commands Dictionary
        self.cmd_dict = {
                # run
                'r' : 'run',
                'run': 'run',
                # clear
                'clear': 'clear',
                'c': 'clear',
                # delete
                'delete' : 'delete',
                'd': 'delete',
                # show
                'show' : 'show',
                's': 'show',
                # help
                'help': 'help',
                'h': 'help',
                # exit
                'exit': 'exit',
                'e': 'exit',
                # main
                'main': 'main',
        }
    
    # Get line
    def getline(self):
        codeline = raw_input('> ')
        self.processline(codeline)

    # Parse line
    def processline(self, codeline):
        codeline = codeline.strip()
        if codeline[0] == '#':
            self.execute(codeline[1:])
        else:
            self.codes.append(codeline + '\n')

    # Write the codes into temp src
    def write_to_src(self):
        fp = open(self.src, 'w')
        fp.writelines(self.codes)
        fp.close()
    
    # Execute interpreter commands
    def execute(self, cmd):
        try:
            handler = self.cmd_dict[cmd]
            self.__getattribute__('_CPPInterpreter__' + handler)()

        except KeyError:
            self.__help()
    
    # Post process before compiling & running
    def post_process(self):
        if self.has_main:
            self.processline('return 0;')
            self.processline('}')

    # Commands
    def __run(self):
        self.post_process()

        self.write_to_src()
        compile_success = '### Compile Success!'

        return_msg = commands.getoutput(self.compile_cmd)
        if return_msg == '':
            return_msg = compile_success

        print '=============================================='
        print return_msg

        if return_msg == compile_success:
            print ''
            print commands.getoutput(self.bin)

        print '=============================================='

    def __clear(self):
        self.codes = [self.pre_codes]

    def __delete(self):
        self.codes.pop(-1)
        if len(self.codes) == 0:
            self.__clear()

    def __show(self):
        for line in self.codes:
            print line
    
    def __help(self):
        fp = open(self.help_src, 'r')

        for line in fp.readlines():
            print line

        fp.close()
        
    def __exit(self):
        self.nexit = False

    def __main(self):
        self.processline('int main(int args, char** argv) {')
        self.has_main = True
