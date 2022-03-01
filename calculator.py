#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Simple Calculator
#

class Calculator(object):
    def __init__(self, caching=True):
        """ init """
        pass

    def add(self, xxx, yyy):
        """ addition """
        return xxx + yyy

    def sub(self, xxx, yyy):
        """ substraction """
        return xxx - yyy

    def mult(self, xxx, yyy):
        """ multiply """
        return xxx * yyy

    def div(self, xxx, yyy):
        """ divide """
        return xxx / yyy

    def mod(self, xxx, yyy):
        """ divide """
        return xxx % yyy

    def operator(self, opr, xxx, yyy):
        if opr == 'add':
            return self.add(xxx, yyy)
        elif opr == 'sub':
            return self.sub(xxx, yyy)
        elif opr == 'mult':
            return self.mult(xxx, yyy)
        elif opr == 'div':
            return self.div(xxx, yyy)
        elif opr == 'mod':
            return self.mod(xxx, yyy)
