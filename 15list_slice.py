# 슬라이싱(slicing)
# 연속적인 객체들(리스트, 튜플, 문자열을 지정하고 선택해서
# 부분적으로 객체를 가져오는 방법 및 표기법
# 리스트 객체에서 필요한 부분의 항목만 뽑아 사용하는 것
# 객체명 [시작:끝-1:스텝]

#다음 코드에서 생년월일 추출
jumin = '123456-1234567'

print(jumin[0:6])
print(jumin[:6]) # 맨처음은 그냥 생략해도 됨. 리스트의 인덱스느 0부터

# 생년월일과 - 를 제외한 나머지 추출
print(jumin[len(jumin) - 7:]) # 이건 역순으로 출력
print(jumin[7:]) # 끝을 생략하면 리스트의 맨  마지막 문장까지

# 다음 코드에서 짝수(홀수) 위치만 추출하고 싶을 때 (생략하고 쓸 수도 있음)
print(jumin[:14:2]) # 홀수 위치
print(jumin[::2]) # 홀수 위치

print(jumin[1:14:2]) # 짝수 위치
print(jumin[1::2]) # 짝수 위치

# 역순으로 추출 : step을 -로 세팅
print(jumin[14:0:-1]) # 0을 붙이니까 처음이 안나옴.
print(jumin[14::-1])
print(jumin[::-1])

# 슬라이스 확인 문제 p.108 (23번쨰)
alphabet = ['a','b','c','d','e','f','g','h','i','j']

print(alphabet[2:5+1])
print(alphabet[:4+1])
print(alphabet[3:7+1])
print(alphabet[5:])
print(alphabet[3:8+1])

# 슬라이스 예제 p.109 ** 이거 정확한거 아님 **
student = ['정우람','박으뜸','배힘찬','천영웅','신석기','배민규',
           '전민수','박건우','박찬호','이승엽']
#2
print(student)
#3
student.remove('박찬호')
print(student)
print(len(student))
#4
print(student[0:3])
#5
student.append('이병규')
#6
print(student[len(student)::-1])
#7
student[0] = '정잘남'


# 리스트 합치기 : extend, +
a = [1,2,3]
b = [4,5,6]
c = ['7','8','9']

a.extend(b) # a = a+b
print(a) # a에 b가 추가돼서 나옴

b.extend(c)
print(b)

# 리스트의 특정 요소 존재 파악
todo = ['cleaning','shoping','study','exercise','game']
print('drive' in todo)
print('shoping' in todo)

# 리스트의 모든 요소 존재 순회
for item in todo:
    print(item,end=',')

# 리스트의 모든 요소 존재 순회 : enumerate(항목의 인덱스(순번)도 출력)
for idx, item in enumerate(todo):
    print(idx, item)

# 리스트의 모든 요소 제거 : clear
print(todo)
todo.clear()
print(todo)

# 혈액보관 시스템. 실전 예제 p.111

bloods = []
a,b,ab,o = 0,0,0,0

for idx in range(1,11):
    print(f' 헌혈해주셔서 감사합니다. 혈액형을 선택하세요({idx}/10)')
    blood = input('A,B,AB,O : ')
    bloods.append(blood)

for bd in bloods :
    if bd == 'A' : a += 1
    elif bd == 'B' : b += 1
    elif bd == 'AB' : ab += 1
    elif bd == 'O' : o += 1

print(f'''
=================================
혈액형 : 개수
=================================
A형 : {a}
B형 : {b}
AB형 : {ab} 
O형 : {o}
================================''')

# 리스트의 항목별 빈도 계산 : count (값)
bloods.count('A')
bloods.count('B')
bloods.count('AB')
bloods.count('O')
#-------------------------------------------------------------
bloods = []
a,b,ab,o = 0,0,0,0

for idx in range(1,11):
    print(f' 헌혈해주셔서 감사합니다. 혈액형을 선택하세요({idx}/10)')
    blood = input('A,B,AB,O : ')
    bloods.append(blood)

bloods.count('A')
bloods.count('B')
bloods.count('AB')
bloods.count('O')



