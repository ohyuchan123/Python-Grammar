# 5.2 사전
cabinet = {3:"이름1",4:"이름2"}

print(cabinet[3]) # 키 값 : 3번 키에는 유재석
print(cabinet[4]) # 4번 키에는 김태호

print(cabinet.get(3)) # 똑같이 3번 키에는 유재석
print(cabinet.get(4)) # 4번 키에는 김태호

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"이름1","A-4":"이름2"}

print(cabinet["A-3"])
print(cabinet["A-4"])

# 새 손님
print(cabinet)

cabinet["A-3"] = "이름3"
cabinet["C-3"] = "이름4"

print(cabinet)

# 간 손님

del cabinet["A-3"]
print(cabinet)

# key 만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key value 쌍으로 출력
print(cabinet.items())

# claer()
cabinet.clear()
print(cabinet)

# 5.3 튜플
menu = ("돈까스","치즈까스")
print(menu)
print(menu[0])
print(menu[1])

(name,age,hobby) = ("이름",20,"코딩")
print(name,age,hobby)

# 5.4 집합
# 중복 안됨,순서 없음
my_set={1,2,3,3,3}
print(my_set)

java ={"이름","이름1","이름2"}
python =set(["이름","이름1"])

# 교집합 (java 와 python을 모두 할 수 있는 개발자)
print(java&python)
print(java.intersection(python))


# 합집함(java도 할 수 있거나 python도 할 수 있는 개발자)
print(java|python)
print(java.union(python))

# 차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java-python)
print(java.difference)

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 잊었어요
java.remove
print(java)


# 5.5 자료구조의 변경
menu ={"커피","우유","주스"}
print(menu,type(menu)) # 집합 set

menu = list(menu)
print(menu,type(menu))

menu = tuple(menu)
print(menu,type(menu))


menu = set(menu)
print(menu,type(menu))