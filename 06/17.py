# for문
from calendar import c
from tkinter.ttk import Style
from turtle import st


for waiting_number in [0,1,2,3,4]:
    print("대기번호 : {0}".format(waiting_number))

for i in range(5):
        print("대기번호 : {0}".format(i))

for i in range(1,6):
    print("대기번호 : {0}".format(i))


starbucks = ["아이언맨","토르","그루트"]
for customer in starbucks:
    print(customer)

# while
customer ="토르"
index = 5
while index>=1:
    print("{0} ,커피가 준비 되었습니다. {1}번 남았어요.".format(customer,index))
    index -=1
    if index ==0:
        print("커피는 폐기처분 되었습니다")


customer ="토르"
person = "Unkown"
while person !=customer:
    print("{0} ,커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")

# continue 와 break
absent = [2,5] #결석
no_book =[7] #책을 깜밖했음
for student in range(1,11):
    if student in absent:
        # student가 absent 안에 포함 되어있는지
        continue
    elif student in no_book:
        print("오늘 수업 여기까지 {0}는 교무실로 따라와.".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))

# 한줄 for문
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 반환
students = ["Iron man","Thor","groot"]
students = [len(i) for i in students] # len(길이)
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man","Thor","groot"]
students = [i.upper() for i in students] # 이름을 대문자로
print(students)