#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree

"""
根据数学表达式建立解析树的原则：
1.如果读入的字符是‘（’，添加新的节点做为当前节点的做子节点，当前节点下降（即当前节点变成刚才创建的左子节点）
2.如果读入的字符是操作符即加减乘除，将当前节点的值设置为读入的操作符，并添加一个新的节点做为当前节点的右子节点，当前节点下降（即变成刚才创建的右子节点）
3.如果读入的字符是数字，将当前节点的值设置为该数字，当前节点变成它的父节点
4.如果读入的字符是‘）’，当前节点变为其父节点
"""

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree
pt = buildParseTree("( ( 10 + 5 ) * 3 )")
pt.postorder() #defined and explained in the next section





