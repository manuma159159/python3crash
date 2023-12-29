# 할인된 상품 가격 출력 프로그램 p.65 -25 문제
products = {'쌀 ':9900,'상추':1900,'고추':2900,'마늘':8900,
             '통닭':5600,'햄 ':6900, '치즈':3900}
#
# print('''
# --------------------------------------
# ----한빛마트 오늘의 할인 가격표 출력 시스템----
# ''')
# rate = int(input('오늘의 할인율은?'))
#
# prices = []
# for val in products.values():
#     price = val * (1- (rate/100)) # 이거 그냥 공식. 외워두는게 좋음. 할인율에 따른 할인금액 계산
#     prices.append(price)
#
# for idx, key in enumerate(products.keys()):
#     print(f'{key:3s}: {products[key]:,}원 {rate}%할인 => {prices[idx]:,.0f}원')


def readDiscount():
    print('''
    --------------------------------------
    ----한빛마트 오늘의 할인 가격표 출력 시스템----
    ''')
    rate = int(input('오늘의 할인율은?'))
    return rate

def getdiscountprice(rate):
    prices = []
    for val in products.values():
        price = val * (1 - (rate / 100))  # 이거 그냥 공식. 외워두는게 좋음. 할인율에 따른 할인금액 계산
        prices.append(price)
    return prices # return prices 쓰는 이유는 이렇게 안하면 이 함수에서만 prices가 쓰임. 다른 함수에서도 쓰이려면 이거 써야함.

def printDiscountPrice(rate, prices):
    for idx, key in enumerate(products.keys()):
        print(f'{key:3s}: {products[key]:,}원 {rate}%할인 => {prices[idx]:,.0f}원')


rate = readDiscount()
prices = getdiscountprice(rate)
printDiscountPrice(rate, prices)


# 26 연봉과 결혼 여부 - 세금 계산    ***자바 기초 문제 풀이***
# isMarried = input('결혼여부는? (1:미혼, 2:기혼)')
# sal = int(input('연봉은?'))
#
# if (isMarried == '1') :
#     if sal >= 3000: tax = sal * 0.25
#     else: tax= sal * 0.1
# else:
#     if sal >= 6000: tax = sal * 0.35
#     else: tax= sal * 0.15
#
# print(f'{isMarried}, {sal}, {tax}')

def marryData():
    isMarried = input('결혼여부는? (1:미혼, 2:기혼)')
    sal = int(input('연봉은?'))
    return isMarried, sal

def salary(ismarried, sal):
    tax = 0
    if (isMarried == '1'):
        if sal >= 3000:
            tax = sal * 0.25
        else:
            tax = sal * 0.1
    else:
        if sal >= 6000:
            tax = sal * 0.35
        else:
            tax = sal * 0.15

    return tax

def printMarrySalary(ismarried, sal, tax):
    print(f'{isMarried}, {sal}, {tax}')

isMarried, sal = marryData()
tax = salary(isMarried, sal)
printMarrySalary(isMarried, sal, tax)

# 한글 출력시 간격 일정하게 맞추기
from hamgleUtil import preFormat
def printDiscountPrice2(rate, prices):
    for idx, key in enumerate(products.keys()):
        print(f'{preFormat(key,5)}: {preFormat(str(products[key]), 6)}원, '
              f'{preFormat(str(rate),3)}%할인 => {preFormat(str(prices[idx]), 6)}원')


rate = readDiscount()
prices = getdiscountprice(rate)
printDiscountPrice2(rate, prices)


# 변수의 유효범위 : scope
# 지역변수 : 블럭내에 선언한 변수, 특정 블럭내에서만 유효
# 전역변수 : 소스내에 선언한 변수, 모든 범위에서 유효
# 함수 내에서 선언한 변수는 함수 밖에서 접근 가능?
# => 함수내에서 선언한 변수는 함수내에서만 사용가능

num1 =10        # 전역global 변수
print(num1)     # 전역 변수 출력

def function1():
    global num3     # global 지역변수로 선언
    num2 = 100      # 지역local 변수
    num3 = 999      # 지역 변수
    print(num1)     # 함수내에서 전역변수 출력
    print(num2)     # 함수내에서 지역변수 출력
    print(num3)
function1()
print(num2) # 지역함수라 먹히지가 않음. func1함수내에서만 됨.
print(num3) # func1함수 내에 선언된 global 지역변수 출력

# 만일, 함수내에서 전역변수의 값을 수정하고 싶다면?
# => global 문 사용 (비추!)
# => 매개변수, return문 사용 (추천!)

num1 = 99       # 얘는 전역변수
num2 = 'abc'
def func2():
    global num2 #하면 전역변수가 함수 내에서 지역함수가 선언한 내용대로 변경됨.
    num1 = 77   # 얘는 지역변수. 즉, 이름은 같지만 아예 다른 전역변수, 지역변수
    print(num1)
    num2 = 'xyz' # 여기서 앞에 global 붙이면 전역함수 지역에서도 xyz로 변경된다.
    print(num2)
func2()
print(num1)
print(num2) # 여기서 만약에 global num2 하고 선언해하면 'abc'가 아닌 'xyz'로 나오게 된다.

num3 = 33
def func3(num3):
    print('func3: ', num3)
    num3 =44
    print('func3: ', num3)

print(num3)
func3(num3)
print(num3)

# call by value vs call ba reference
# 파이썬에서는 기본자료형 변수를 함수의 매개변수로 넘기는 경우
# call by value(값에 의한 호출)가 발생하기 때문에
# 함수 내 매개변수와 호출시 전달한 변수는 서로 다른 것으로 인식된다.


# 반면, 참조자료형(문자형, 컨테이너형) 변수를 함수의 매개변수로 넘기는 경우,
# call by reference(주소에 의한 호출)가 발생하기 때문에
# 함수 내 매개변수와 호출시 전달한 변수는 서로 동일한 것으로 인식됨.

# 단, 파이썬은 call by value/reference라기보다
# passed by assignment로 인식

# 웹사이트 누적 방문 횟수 프로그램 p.37 -25
visits = 0
# while True:
#     job = input('작업은? (1.웹사이트방문, 2.종료)')
#     if job == '1':
#         visits += 1
#         print('누적 방문 횟수', visits)
#     elif job == '2':
#         break

def visittime():
    #visits = 0 지역변수
    global visits
    while True:
        job = input('작업은? (1.웹사이트방문, 2.종료)')
        if job == '1':
            visits += 1
            print('누적 방문 횟수', visits)
        elif job == '2':
            break

visittime()

#=============

# 주민번호를 입력받아 유효성을 검사하는
# checkJumin 함수를 작성하세요
# 1. 주민번호 맨 끝자리를 제외한 나머지 번호들의
#    각자리를 2,3,4,5,6,7,8,9,2,3,4,5 가중치로 곱합

 # 1 2 3 4 5 6 - 1 2 3 4 5 6 7
 # * * * * * *   * * * * * *
 # 2 3 4 5 6 7   8 9 2 3 4 5
 #
 # 2+6+12+20+30+42+8+18+6+12+20+30


# 2. 곱한 결과를 각각 모두 더함
# 3. 더한 값을 11로 나눠 구한 나머지를 11에서 뺌
# 4. 이렇게 구한 결과와 주민번호 맨 마지막 자리의 일치여부 검사
# 5. 만약, 구한 결과가 2자리라면 맨 끝자리와 비교함

# jumin = input('주민번호는? ')
# jumin = '111111-1111118'
# sum = 0
# sum += int(jumin[0]) * 2
# sum += int(jumin[1]) * 3
# sum += int(jumin[2]) * 4
# sum += int(jumin[3]) * 5
# sum += int(jumin[4]) * 6
# sum += int(jumin[5]) * 7
# sum += int(jumin[7]) * 7
# sum += int(jumin[7]) * 8
# sum += int(jumin[8]) * 9
# sum += int(jumin[9]) * 2
# sum += int(jumin[10]) * 3
# sum += int(jumin[11]) * 4
# sum += int(jumin[12]) * 5
#
# mod = sum % 11
# checker = 11 - mod
# print(checker)
#
# if checker == int(jumin[13]):
#     print('주민번호 유효!')
# else:
#     print('주민번호 유효!')


# def checkerJumin():
#     jumin = input('주민번호는? ')
#     result = '주민번호 불일치'
#     sum = 0
#     sum += int(jumin[0]) * 2
#     sum += int(jumin[1]) * 3
#     sum += int(jumin[2]) * 4
#     sum += int(jumin[3]) * 5
#     sum += int(jumin[4]) * 6
#     sum += int(jumin[5]) * 7
#     sum += int(jumin[7]) * 7
#     sum += int(jumin[7]) * 8
#     sum += int(jumin[8]) * 9
#     sum += int(jumin[9]) * 2
#     sum += int(jumin[10]) * 3
#     sum += int(jumin[11]) * 4
#     sum += int(jumin[12]) * 5
#
#     mod = sum % 11
#     checker = 11 - mod
#
#     if checker == int(jumin[13]) : result='주민번호 유효!'
#
#     print(result)
#
# checkerJumin()

def checkerJumin2():
    jumin =input('주민번호는? ')
    pos = [0,1,2,3,4,5, 7,8,9,10,11,12]
    weight = [2,3,4,5,6,7, 8,9,2,3,4,5,]
    sum = 0
    result = '주민번호 불일치'
    for i in range(len(pos)):
        sum += int(jumin[pos[i] ]) * weight[i]

    checker = (11 - (sum % 11)) %10

    if checker == int(jumin[13]) : result='주민번호 유효!'

    print(result)

checkerJumin2()