#문자열

from cgi import print_arguments
from turtle import color


sentence="나는 소년입니다."
print(sentence)
sentence2='파이썬은 쉬워요'
print(sentence2)
sentence3="""
    나는 소년이고,
    파이썬은 쉬워요
"""
print(sentence3)

#슬라이싱

yuchan="939490-1234567"

print("성별 : "+yuchan[7])
print("연 : "+yuchan[0:2]) #0~2직전 까지
print("월 : "+yuchan[2:4]) 

print("생년월일 : "+yuchan[:6]) #처음부터 6직전까지
print("뒤 7자리 : "+yuchan[7:]) #7부터 끝가지
print("뒤 7자리(뒤에서부터) : "+yuchan[-7:]) #맨 뒤에서 부터 7자리 끝가지

# 문자열 처리 함수
python="Python is Amazing"
print(python.lower()) #모든 문자를 소문자로
print(python.upper()) #모든 문자를 대문자로
print(python[0].isupper()) #첫 번째 문자가 소문자면 False 대문자면 True
print(len(python)) #문자열의 길이를 표현
print(python.replace("Python","Java")) #Python을 Java로 교체

index=python.index("n")
print(index) #python 이라는 글자 중에서 n이라는 글자가 몇번째에 있는지 


#문자열 포맷

#방법 1
print("나는 %d살입니다"% 20)
print("나는 %s를 좋아해요"% "파이썬")
print("Apple 은 %c로 시작해요"% "A")

#방법 2
print("나는 {}살 입니다".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간"))


#방법3
print("나는 {age}살이며 {color}색을 좋아해요".format(age=20,color="빨간"))