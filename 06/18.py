# 함수 
from dbm import gnu
from io import open_code
from random import randint, random
from tkinter.tix import Balloon


def open_account ():
    print("새로운 계좌가 생성되었습니다.")

    open_account()

def depoist(balance,money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다. ".format(balance+money))
    return balance+money

def withdraw(balance,money):
    if balance>=money: #잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance-money))
        return balance-money
    else :
        print("출금이 완료되지 않았습니다. 잔액은{0} 원입니다.".format(balance))
        return balance
balance = 0
balance = depoist(balance,money=randint(500,10000))
balance = withdraw(balance,money=randint(500,10000))
print(balance)


# 기본값

def profile(name,age,main_lang):
    print("이름 : {0}\n나이:{1}\n주 사용 언어 : {2}".format(name,age,main_lang))

profile("홍길동",18,"Java")


# 키워드 값
def profile(name,age,main_lang):
    print("이름 : {0}\n나이:{1}\n주 사용 언어 : {2}".format(name,age,main_lang))

profile(name="유재석",main_lang="자바",age=20)


# 가변 인자
def profile(name,age,lang1,lang2,lang3,lang4):
    print("이름 : {0}\n나이:{1}\n".format(name,age),end=" ")
    print(lang1,lang2,lang3,lang4)

profile("유재석",20,"java","python","C#","js")


# 지역변수와 전역변수
gun = 10 # 지역변수
def checkpoint(soldiers):
    gun = 20 # 전역변수
    gun = gun-soldiers
    print('[함수 내] 남은 총 : {0}'.format(gun))

print("전체 총 : {0}".format(gun))

checkpoint(2)
print("남은 총 : {0}".format(gun))