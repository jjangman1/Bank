

user = []

class Account:
    def __init__(self, number = "", name = "", balance = 0):
        if (number == ""):
            self.number = int(input("게좌번호 : "))
            self.name = input("이름은 : ")
            self.balance = int(input("예금은 : "))



    def send_money(self, sender, receiver, money):
        sender.balance -= money
        print(sender.name, '가', receiver.name, '에게', money, '원 송금')
        print('출금 후 잔액은', sender.name, sender.balance, '원', receiver.name, receiver.balance, '원')
