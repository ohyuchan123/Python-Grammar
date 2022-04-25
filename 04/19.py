# 리스트[]
# 지하철 칸별로 10명 ,20명 , 30명

subway1=10
subway2=20
subway3=30

subway=[10,20,30]
print(subway)

subway=["이름1","이름2","이름3"]
print(subway)


#현재 리스트의 조세호의 위치
print(subway.index("이름2"))

#하하씨가 다음 정류장애서 다음 칸에 탐
subway.append("이름4")
print(subway)

# # 정현돈씨를 유재석 /조세호
# subway.insert(1,"정형돈")
# print(subway)

# 지하철에 있는 사람을 한 명씩 뒤애서 꺼냄
print(subway.pop())
print(subway)

#정렬도 가능
num_list=[5,4,3,2,1]
num_list.sort()
print(num_list)
