#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

from pythonds.trees.binaryTree import BinaryTree

myTree = BinaryTree('A')
# print(myTree.getRootVal())
myTree.insertLeft('B')
myTree.insertRight('C')
# print(myTree.getLeftChild().getRootVal())
# print(myTree.getRightChild().getRootVal())
myTree.getLeftChild().insertLeft('D')
myTree.getLeftChild().insertRight('E')
# print(myTree.getLeftChild().getLeftChild().getRootVal())
# print(myTree.getLeftChild().getRightChild().getRootVal())
myTree.getRightChild().insertLeft('F')
myTree.getRightChild().insertRight('G')
# print(myTree.getRightChild().getLeftChild().getRootVal())
# print(myTree.getRightChild().getRightChild().getRootVal())
myTree.getLeftChild().getRightChild().insertLeft('H')
myTree.getLeftChild().getRightChild().insertRight('I')
# print(myTree.getLeftChild().getRightChild().getLeftChild().getRootVal())
# print(myTree.getLeftChild().getRightChild().getRightChild().getRootVal())
myTree.getRightChild().getRightChild().insertLeft('J')
myTree.getRightChild().getRightChild().insertRight('K')
# print(myTree.getRightChild().getRightChild().getLeftChild().getRootVal())
# print(myTree.getRightChild().getRightChild().getRightChild().getRootVal())

# 前序遍历
def preOrder(tree):
    if tree:
        print(tree.getRootVal(),end = ' * ')
        preOrder(tree.getLeftChild())
        preOrder(tree.getRightChild())

preOrder(myTree)
print()

# 中序遍历
def inOrder(tree):
    if tree:
        inOrder(tree.getLeftChild())
        print(tree.getRootVal(),end = ' * ')
        inOrder(tree.getRightChild())

inOrder(myTree)
print()

# 后序遍历
def postOrder(tree):
    if tree:
        postOrder(tree.getLeftChild())
        postOrder(tree.getRightChild())
        print(tree.getRootVal(),end = ' * ')

postOrder(myTree)
print()
