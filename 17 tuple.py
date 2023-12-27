# 튜플 자료형
# 순차적 데이터를 관리하는 자료형(순서가 존재)
# 리스트와 동일하지만, 변경 불가능 특성을 지님
# => 생성은 가능 / 추가,수정,삭제는 불가능
# 튜플 객체 생성은 ()를 사용
# **읽기 전용으로 할 때 쓰임**

tuple1 = ()
tuple2 = (1,2,3,4,5)
tuple3 = ('a','b','c','d','e')
tuple4 = (1,'b',3.14,'d',5)

print(tuple4)

# 튜플 추가/수정/삭제 해보기
tuple1.append(10)  # 튜플에는 append라는 함수가 매칭이 될 수 없음. 그래서 오류가 뜸. append 함수는 뒤에 추가하는 함수이기 때문
tuple2[4] = 10   # 색이 변한건 아예 안되는 함수라고 여기서 말해주는 것임.
tuple2.pop()
tuple2.remove(3) # 삭제까지 싹 다 안되는 모습.

# 튜플 합치기 : + 만 지원
print(tuple2 + tuple3) # 얘는 되는데
tuple2.extend(tuple3)  # 얘는 안됨. extend 함수를 지원하지 않음

# 만약, 튜플의 요소를 변경해야 한다면?
# 튜플을 리스트로 변환한 후 요소를 변경하고
# 다시 리스트를 튜플로 변환하면 됨
# 튜플을 리스트로 변환 : list(대상)
# 리스트를 튜플로 변환 : tuple(대상)

tuple1 = list(tuple1) # 튜플을 리스트로 바꾸고
tuple1.append('A')    # append 함수를 이용해 내용을 추가해주고
tuple1.append('B')
tuple1 = tuple(tuple1) # 다시 튜플로 변환 후
print(tuple1)  # 프린트해보면 내용이 추가된게 보임.

# 리스트/튜플의 요소 인덱스 알아내기

tuple4.index(3.14)
tuple4.index('b')

# 연습문제
numbers = (10,20,30,40,50,60)

print(numbers[1:3])
print(numbers[:2])
print(numbers[1:4])
print(numbers[3:len(numbers)-1])

# 1 ~ 45 사이 임의의 정수 6개를 추출해서
# 리스트와 튜플에 저장하는 코드를 작성하세요

# 난수 생성하기
# random이라는 모듈이 필요
# random()    : 0~1사이 임의의 부동소수점 숫자 출력
# randint(x,y) : x~y사이 임의의 정수 출력
# randrange(s,e,l) : 시작부터 끝 사이 임의의 출력

import random as rnd
rnd.seed(2312271045)
print(rnd.random())
print(rnd.randint(1,10)) # 1~ 10 사이 난수 생성
print(rnd.randrange(1,10,10)) # 1~9 난수 생성

# 1~100 사이 임의의 3의 배수 출력
print(rnd.randrange(3,100,3))

# 1~ 45 사이 임의의 정수 6개를 추출해서
# 리스트와 튜플에 저장하는 코드를 작성하세요.


lotto1 = []
lotto2 = ()

lotto2 = list(lotto2)
for _ in range (6):
    lotto1.append(rnd.randint(1,45))
    lotto2.append(rnd.randint(1,45))

lotto2 = tuple(lotto2)
print(lotto1)
print(lotto2)

# 1~ 45 사이 임의의 정수 6개를 추출해서
# 리스트와 튜플에 저장하는 코드를 작성하세요.
# 단, 중복된 값은 저장되지 않도록 함. 중복 제외

lottos = [] # 이걸 이해하는게 매우 중요하다.
cnt = 0 # 몇번만에 만들어지는지 확인하기 위해 돌리는 횟수를 나타낼 것
while len(lottos)<6:
    cnt += 1
    lotto =rnd.randint(1,45)
    if lotto not in lottos:
        lottos.append(lotto)
print(lottos, cnt)




