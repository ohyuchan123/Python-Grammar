# 숫자형 자료형
print(5)
print(-10)
print(3.14)
print(1000)

print(5+3)
print(5*3)
print(6/2)
print(25//5) #소숫점 이하의 수를 버리고, 정수 부분의 수만 구함
print(25%5) #나누기 연산 후 몫이 아닌 나머지를 구함

# 문자형 자료형
print('python')
print("spring") # 큰따옴표와 작은 따옴표의 차이는 없다 어느 것을 써도 상관 없음
print('s'*5)

#boolean 자료형

#참/거짓
print(5>10) #false
print(5<10) #true
print(True) #true
print(False) #False
print(not True) #False
print(not False) #True
print(not (5<10)) # false

#변수

# 애완 동물
animal='강아지'
name='연탄'
age=4
hobby='산책'
is_adult=age>=3

print('현재 강아지를 키우고 있는데 강아지의 이름은 연탄')
print('연탄이는 4살이며, 산책을 아주 좋아해요')
print('연탄이는 어른일까요 ? True \n')


print('현재 {0}를 키우고 있는데 {0}의 이름은 {1}'.format(animal,name))
print('{0}이는 {1}살이며, {2}을 아주 좋아해요'.format(name,age,hobby))
print('{0}이는 어른일까요 ? {1} \n'.format(name,is_adult))

#연산자

print(1+1) # 더하기 : (결과 : 2)
print(3-2) #빼기 : (결과 :1)
print(5*2) #곱하기 : (결과 : 10)
print(6/3) #나누기 : (결과 :2)

print(2**3) #제곱 : (결과 : 8)
print(5%3) # 나머지 구하기 : (결과 : 2)
print(10//3) # 소숫점 이하의 수를 버리고, 정수 부분의 수만 구함 (결과 : 1)

print(10>3) # True
print(4>=7) # False
print(10<3) # False
print(5<=5) # True

# 숫자 처리 함수

print(abs(-5)) #절대값 5
print(pow(4,2)) #4의 2승 16
print(max(5,12)) #최댓값 12
print(min(5,12)) #최솟값 5
print(round(3.14)) #반올림 3

from math import * #math 라이브러리에 있는 모든 것을 이용하겠다
print(floor(4.99)) #내림 4
print(ceil(3.14)) #올림 4
print(sqrt(16)) #근을 구함 4

# 랜덤 함수

from random import*

print(random()) #0.0~1.0 미만의 임의의 값을 생성
print(random()*10) #0.0~10.0 미만의 임의의 값을 생성
print(int(random()*10)) #0~10 미만의 임의 값을 생성
print(randrange(1,46)) #1~45 미만의 값을 생성
 