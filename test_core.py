import pytest

from cathay.sample.customer import Customer
from cathay.sample.core import CustomerDataProcess
from decimal import Decimal, ROUND_DOWN

INIT_MONEY=100.0

class TestCoreSuites:
##########################################################################################
#
# 假設這位客戶, 名字是 Test User, 帳號為100-1100, 一開始帳戶會先存100元, 要測試下面項目: 
# 1. 之後存款1000元, 確認帳戶總金額為1100元
# 2. 接續提款500元, 確認帳戶總金額為600元
# 3. 之後提款700元, 會出現 RuntimeError
#
##########################################################################################
    def __init__(self, name, account):        
        self.name = name
        self.account = account
        self.balance = Decimal(INIT_MONEY)
        
    def deposit(self, amount):        
        if self.balance >= 0 and amount >= 0:
            self.balance=self.balance+Decimal(amount)
        else:
            raise ValueError('balance and amount must be positive')
            
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= Decimal(amount)
        else:
            raise RuntimeError('balance not enough')      

user = TestCoreSuites('Test User', '100-1100')
user.deposit(1000)
user.withdraw(600)
print(user.balance)