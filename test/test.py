#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import pprint

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    def insertLeft(self,newNode):
        if not self.leftChild :
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
    def insertRight(self,newNode):
        if not self.rightChild:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    def getRightChild(self):
        return self.rightChild
    def getLeftChild(self):
        return self.leftChild
    def setRootVal(self,obj):
        self.key = obj
    def getRootVal(self):
        return self.key

r = BinaryTree('a')
pprint.pprint(r.getRootVal())
pprint.pprint(r.getLeftChild())
r.insertLeft('b')
pprint.pprint(r.getLeftChild())
pprint.pprint(r.getLeftChild().getRootVal())
r.insertRight('c')
pprint.pprint(r.getRightChild())
pprint.pprint(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
pprint.pprint(r.getRightChild().getRootVal())




