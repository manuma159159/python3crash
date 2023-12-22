# 반복문
# 특정 문장 / 코드를 지정한 횟수/조건에 의해 반복실행하는 문장

#간단한 메세지 한번 출력
print('오늘 날씨 추워요!')

#메세지르 여러번 출력
print('오늘 날씨 추워요!')
print('오늘 날씨 추워요!')
print('오늘 날씨 추워요!')

# 메세지를 수정해야 할 필요가 생긴다면? - 수정 불편!
print('오늘 너무 날씨 추워요!')
print('오늘 날씨 추워요!')
print('오늘 날씨 추워요!')

# 만약, 반복문을 사용한다면?
# 반복의 용이성과 수정의 용이성을 제공

# 파이썬의 반복문
# for : 지정ㅇ한 횟수만큼 반복수행한다.
# while : 지정한 조건에 의해 반복 수행

#for 문
# for 변수 in range (시작값, 종료값, 증가/감소) :
#       반복할 문장
# 반복횟수는 range (시작값, 종료값)으로 유추 가능
# 즉 횟수는 종료값 - 시작값 - 1로 계산 됨
# range 함수는 시작값과 종료값-1 사이의 연속되는 정수들을 반환함

#1부터 10까지 정수 출력
print(1,2,3,4,5,6,7,8,9,10)
print(list(range(1,10, 2)))
# [1,3,5,7,9]

# iterable 객체
# 값을 차례대로 꺼내 볼 수 있는 객체를 의미
# 보통 리스트, 튜플, 딕셔너리등의 객체를 의미

# 반복문에 자주 사용함
#for i in range 91,10
# => for i in [1,2,3,4,5,6,7,8,9]


# 1~10 모든 정수 출력
for i in range (1, 10+1): #1,2,3,4,5,,,10
    print(i, end=',')

# 1 ~ 100까지 모든 정수들의 합을 출력
total_sum = 0

for i in range(1, 1000000+1):
    total_sum += i # total_sum = total_sum + i 이것도 됨.

print(total_sum)

# 1~ N까지의 합을 구하는 공식 : 가우스 덧셈 공식
# => (N * (N+1))/2
tot = (100* (100+1)) / 2
print(tot)

# 구구단중 특정 단을 입력받ㅇ아 출력
# 예를 들어 7 단을 출력한다면?

dan = int(input('구구단의 단은?'))

for i in range(1, 9+1):
    print(f'{dan} x {i} = {dan * i}')

print(dan)

# 2~8 사이 짝수 출력
for i in range(2,9,2):
    print(i, end=',')

for i in range(1, 12,2):
    print(i, end=',')
for i in range(0,8,2):
    print(i,end=',')
for i in range(-10,1,1):
    print(i, end=',')
for i in range(1,11,2):
    print(i, end=',')

#음수 출력하기
print(list(range(-10,0+1)))

# 시작값이 없는 range 함수
# 이럴 경우 시작값은 자동으로 0부터 시작
print(list(range(10)))

# 이터러블에 문자열을 넣으면 아이템에는
# 문자열의 첫 문자부터 끝 문자가 순차적으로 저장됨
# 결과적으로 실행문은 문자 개수만큼 반복 실행됨
for c in 'Hello':
    print(c, end='')

#이터러블에 리스트를 넣으면 아이템에는 리스트를 구성하는 요소들이
#순차적으로 저장된다. 결과적으로 실행문은 리스트의 요소수만큼 반복실행
menus = ['라면','돈까스','짜장면','냉면','정식','초밥','스테이크','파스타']
for menu in menus:
    print(menu,end=',')

for i in range(len(menus)):
    print(menus[i],end=',')


#pass 키워드
#반복문 사용시 코드만 작성해놓고
#실행문은 나중에 작성하고 싶을 경우
#pass 라는 키워드 사용
for i in range(1,100):
    pass

# 반복 수행시 이터러블 객체가 필요없는 경우
# 변수명 대신 _를 사용하기도 함
for _ in range(10):
    print('Hello, World!!')

#중첩
# *
# **
# ***
# ****
# ***** 모양 출력하기

for i in range(1,5+1):          #행 (비유하자면 시침)
    for j in range(1,5+1):      #열 (비유하자면 분침) (아래있는게 한바퀴 다 돌아야 위에있는 놈이 돈다)
        print('*', end='')
    print()                     #줄바꿈 (새로운 행에 만듦)

#2단부터 9단까지 구구단을 출력하는
#반복문을 작성하세요

for i in range(1, 9+1):
    print(f'{dan} x {i} = {dan * i}')

for dan in range(2,9+1):
    for j in range(1, 9 + 1):
        print(f'{dan} x {j} = {dan * j}', end=',')
    print()
#줄바꿈없이 출력하되 9개의 단을 출력하고 줄바꿈 추가
#자리수 맞추기

for dan in range(2,9+1):
    for j in range(1, 9 + 1):
        print(f'{j} x {dan} = {dan * j:2d}', end='  ,  ')
    print() # 2d 는 너비. 즉 정렬해서 보여준다.

# employees를 이용해서 사원정보를 입력하면
# list에 각각 저장하는 코드를 작성하세요
# 사번empno, 이름fname, 성lname, 이메일email,
# 입사일hdate, 직책jobid, 급여sal, 부서번호deptid

employees = []
empnos = []
fnames = []
lnames = []
emails = []
hdates = []
jobids = []
sals = []
deptids = []

empno = input('사번은?')
fname = input('이름은?')
lname = input('성은?')
email = input('이메일은?')
hdate = input('입사일은?')
jobid = input('직책은?')
sal = input('급여은?')
deptid = input('부서번호는?')

empnos.append(empno)
fnames.append(fname)
lnames.append(lname)
emails.append(email)
hdates.append(hdate)
jobids.append(jobid)
sals.append(sal)
deptids.append(deptid)

for i in range(len(empnos)):
    print(f'{empnos[i]} {fnames[i]} {lnames[i]}'
          f'{emails[i]} {hdates[i}} {jobids[i]}'
          f'{sals[i]} {deptids[i]}')


