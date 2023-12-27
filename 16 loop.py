# while 문
# 조건을 만족할 때 까지 반복을 실행
# 변수 = 초기값
# while 조건식:
#       반복할 문장
#       변수 증가/감소

# 1~ 10 까지 모든 정수 출력
# for i in range(1,11):
#   print (i,end= ' ')
i = 1
while i <= 10: # 반복 조건
    print(i, end=',')
    i = i + 1 # 반복 증감

# 1~50 까지 모든 정수 중 홀수만 출력
while i <= 50 :
    print(i , end=',')
    i = i + 2

while i <= 50:   # 짝수의 경우임. 홀수도 = 하나 빼고 ! 넣으면 홀수 구해짐
    if i % 2 == 0 : print(i, end= ',')
    i = i+1

# 1~50 까지 모든 정수 중 7의 배수만 출력
i = 7
while i <= 50:
    print(i, end= ',')
    i = (i+7)

i = 1
while i <= 50:
    if i % 7 == 0 : print(i, end= ',')
    i = i+1

# 1~200 까지 모든 정수의 합 출력
sum = 0
i = 1
while i <=200:
    sum = sum+i
    i= i+1

print(sum)

# 1부터 100까지의 모든 정수 중 3과 8의 공배수와 최소공배수 출력
i = 1
mincm = 0

while i <= 100 :
    if i % 3 == 0 and i % 8 == 0 :
        print(i)
        if mincm == 0 : mincm =i # 최소공배수 저장 | 그리고 한번만 나오는 이유는 mincm이 24가 되어서 0이 아니라 한번만 실행 됨.
    i= i+1

print(mincm)


#반복문 내 실행중지 : break
# for, while 문 내에서 반복흐름을 벗어나기 위해 사용

# 1~10000 까지의 정수 합을 출력
#단, 정수 합이 123457보다 크면 계산을 중단한다
sum = 0

for i in range(1,10000):
    if sum > 12345678:
        print(i, sum)
        break      # 반복 중단
    sum = sum + i

print(sum) #50005000


i = 1
while i <= 10000:
    if sum > 1234567:
        print(sum)
        break
    sum = sum + i

print(sum)

#반복문 내 반복 건너뛰기 : continue
# for, while문 내에서 반복흐름을 일시적으로 건너뛰기 위해 사용

# 1~100 정수 합 출력
# 단, 3의 배수나 7의 배수는 제외하고 합을 계산하세요

sum = 0
i = 1
for i in range(1,100+1):
    if i % 3 == 0 or i % 7 ==0: continue # 컨티뉴 조건 만족하면 sum = sum+ i 안하고 다시 반복
    sum = sum + i

print(sum)

sum = 0
i = 0
while i < 100:
    i = i + 1
    if i % 3 == 0 or i % 7 == 0: continue  # 컨티뉴 조건 만족하면 sum = sum+ i 안하고 다시 반복
    sum = sum + i
print(sum)

# 실전 예제 1 p.57 (23)
# 1~99 사이에서 3,6,9 있으면 짝이라고 출력하기

for i in range(1,99+1):
    jjak = ''
    if '3' in str(i): jjak += '짝!'
    if '6' in str(i): jjak += '짝!'
    if '9' in str(i): jjak += '짝!'
    if i == 33 or i == 66 or i == 99: jjak += '짝!'
    print(f' {i} {jjak}')

# 1~9 : 3의 배수 여부 확인
# 10~99 : 개별 문자가 3,6,9인지 확인 (즉 , 3의 배수)
for i in range(1,99+1):
    if i <= 9 : #1 ~ 9 사이 3/6/9
        if i % 3 == 0 : print(i, '짝!')
        else: print(i)
    else:
        print(i, end='')

        num1 =int(str(i)[0])
        num2 =int(str(i)[1])

        if num1 % 3 == 0: print( '짝!',end=',' )
        if num2 != 0 and num2 % 3 ==0: print( '짝!',end=',' )

    print()


# 실전예제 2
# 열차 교차시간 알아내기

trainA = 10
trainB = 25
trainC = 30

for m in range(1,540+1): #오전 9시 ~ 오후 6시 분으로 환산하면 540분 m = minute.
    if m % 10 ==0:
        if m % trainA == 0 and m % trainB == 0 : # 이게 중간에 낀 것. 원래 141,142,144 이렇게만 하는게 시간을 출력하는 기본 코드.
            print(f'{9 + m // 60:0d}시 {m%60:0d}분 A-B') # //이건 몫을 구하는 것. 9를 더하는 것은 시간을 나타내기 위해. 분은 나머지가 분이기 때문 이건 그냥 시간을 나타낸 것.
        if m % trainA == 0 and m % trainC == 0:
            print(f'{9 + m // 60:0d}시 {m % 60:0d}분 A-C')
        if m % trainB == 0 and m % trainC == 0:
            print(f'{9 + m // 60:0d}시 {m % 60:0d}분 B-C')
        if m % trainA == 0 and m % trainB == 0 and m % trainC == 0:
            print(f'{9 + m // 60:0d}시 {m % 60:0d}분 A-B-C')




# 실전예제 3
# 관리자 로그인 기능

logincnt = 1
passwd = 'hanbitac'

while True:
    if logincnt > 5:
        print('로그인 실패. 횟수 초과')
        break
    pwd = input('관리자 암호를 입력하세요..')

    if passwd != pwd:
        print('암호를 다시 확인하세요')
        logincnt +=1 # logincnt = logincnt + 1
    else:
        print('로그인 됐습니다.')






