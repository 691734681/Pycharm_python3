#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

import random

class Account():
    num_account = 0
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        Account.num_account += 1
    def __del__(self):
        Account.num_account -= 1
    def deposit(self,amt):
        self.balance = self.balance + amt
    def withdraw(self,amt):
        self.balance = self.balance - amt
    def inquiry(self):
        return self.balance

class EvilAccount(Account):
    def __init__(self,name,balance,evilfactor):
        #Account.__init__(self,name,balance)
        super().__init__(name,balance)
        #super(EvilAccount,self).__init__(name,balance)
        self.evilfactor = evilfactor
    def inquiry(self):
        if random.randint(0,4) == 1:
            return self.balance * self.evilfactor
        else:
            #return self.balance
            return super().inquiry()

c = EvilAccount('George',1000.00,1.1)
c.deposit(10.0)
available = c.inquiry()
print(available)
