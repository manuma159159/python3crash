# 함수와 모듈
# 함수는 일정한 작업을 수행하는 코드 집합체
# 보통 여러곳에 반복적으로 사용되는 코드들을 함수로 정의해서 사용

# 즉, 반복적으로 사용할 가치가 있는 코드를 한 뭉치로 묶고
# (어떤 입력값을 주면) 결과가 반환되도록 사용

# 또한, 여러 코드들을 함수화하면 프로그램의 흐름을
# 일목요연하게 파악하기 쉬움

# 코드의 이식성이나 재샤용성이 높아짐 -개발 속도가 빨라짐

# 다른 사람과의 협업시 코드가 섞이지 않게 하기 위한
# 목적도 있음 - 모듈

# 함수 정의
# def 함수명(매개변수):
#     함수몸체(코드들)

print('선생님~ 미워요') # 단순출력

print('선생님~ 미워요') # 반복 출력
print('선생님~ 미워요') #

for _ in range(3):
    print('선생님 ~ 미워요') # 개선된 반복

# 이러한 반복문을 여러번 사용해야한다면?
# 또, 만약, 미워요 대신 싫어요나 좋아요로 바꿔야한다면?

# 1개의 사용위치 신규*
def saymsg():  # def = definition
    for _ in range(3):
        print('선생님 ~ 미워요')

#함수호출
#함수명(), 함수명(입력값)
saymsg()

# 신규 *
def saymsg2(): # 입력값x, 함수내에서 출력처리 (반환값 x)
    msg = '좋아요'
    for _ in range(3):
        print(f'선생님 ~ {msg}!')
saymsg2()

def saymsg3(msg):  # 입력값o, 함수내에서 출력처리 (반환값 x)
    for _ in range(3):  # 개선된 반복
        print(f'선생님 ~ {msg}!')
saymsg3('좋아요')
saymsg3('미워요')
saymsg3('싫어요')


# 문제 해결 p.17 -25 함수 이름 짓기
def sensorOn():
    print('온도센서 작동을 시작한다.')
def sensorOff():
    print('온도센서 작동을 중지한다.')

# 문제 해결 p.21 # 내 노트북은 몇인치일까?
def nbsize():
    note = int(input('길이를 입력하세요. (cm)'))
    a = note / 2.54
    print (f'{note}cm = {a:.2f} inch')
nbsize()

length = int(input('길이를 입력하세요. (cm)'))
print(f'{length}cm = {length * 0.3937} inch')

def notebooksize():  # 선생님이 하신 것.
    length = int(input('길이를 입력하세요. (cm)'))
    cminch = length * 0.3937
    print(f'{length}cm = {cminch:.3f} inch')
notebooksize()

# p.22 이동거리를 계산하는 함수

times = int(input('이동 시간을 입력하세요.'))
speeds = int(input('이동 속도를 입력하세요.'))
dist = times * speeds
print(f'이동거리는 {dist}km 입니다.')

def mount():
    times = int(input('이동 시간을 입력하세요.'))
    speeds = int(input('이동 속도를 입력하세요.'))
    dist = times * speeds
    print(f'이동거리는 {dist}km 입니다.')
mount()

# 함수의 유형
# 입력값 x   반환값 x
# 입력값 x   반환값 o   !! -많이 쓰는 형태
# 입력값 o   반환값 x
# 입력값 o   반환값 o   !!! - 이것도

def saymsg4(msg):  # 입력값o, 처리 결과 반환 (반환값 o)
    text = ''
    for _ in range(3):  # 개선된 반복
        text += f'선생님 ~ {msg}!\n'
    return text # 결과를 처리하지 않고 넘김

print(saymsg4('미워요'))


def notebooksize2():  # 선생님이 하신 것.
    print('길이를 입력하세요. (cm)', end=',')
    length = int(input())
    cminch = length * 0.3937
    return cminch

print(f'{notebooksize2()} inch')
print(f'{notebooksize2()} 인치')

def notebooksize3():  # 선생님이 하신 것.
    print('길이를 입력하세요. (cm)', end=',')
    length = int(input())
    cminch = length * 0.3937
    return length, cminch

length, cminch = notebooksize3()

print(f'{length}cm = {cminch:.3f} inch')
print(f'{length}센티미터 = {cminch:.3f} 인치')

def mount2(): # 이건 p.22 return 버전
    times = int(input('이동 시간을 입력하세요.'))
    speeds = int(input('이동 속도를 입력하세요.'))
    dist = times * speeds
    return dist

dist = mount2()
print(f'이동거리는 {dist}km 입니다.')

# p.30 계산기 프로그램 return 버전

nums1 = int(input('숫자를 입력하세요.'))
four = input('연산자를 선택하세요. 1.덧셈. 2.뻴셈 3.곱셈 4.나눗셈')
nums2 = int(input('숫자를 입력하세요.'))

result = 0
if four == '1' :
     result = nums1 + nums2
     four = '덧셈'
elif four == '2' :
    result = nums1 - nums2
    four = '뻴셈'
elif four == '3' :
      result = nums1 * nums2
      four = '곱셈'
elif four == '4' :
     result = nums1 / nums2
     four = '나눗셈'
print(f'{four} 결과 : {result:.1f}')

# 프로그램 객체지향 설계 5 원칙
# SOLID
# Single responsibility
#
def readData():  # 데이터 입력부, 데이터 계산
    nums1 = int(input('숫자를 입력하세요.'))
    four = input('연산자를 선택하세요. 1.덧셈. 2.뻴셈 3.곱셈 4.나눗셈')
    nums2 = int(input('숫자를 입력하세요.'))
    return  nums1, four, nums2


def computeNumber(nums1, four, nums2):
    result = 0
    if four == '1' :
        result = nums1 + nums2
        four = '덧셈'
    elif four == '2' :
        result = nums1 - nums2
        four = '뻴셈'
    elif four == '3' :
        result = nums1 * nums2
        four = '곱셈'
    elif four == '4' :
        result = nums1 / nums2
        four = '나눗셈'
    print(f'{four} 결과 : {result:.1f} ')
    return four, result
def computer():
    # 데이터 입력부
    nums1,four,nums2 = readData()

    # 데이터 계산
    four, result = computeNumber(nums1,four,nums2)

    # 처리 결과 넘김
    return four, result


four, result = computer()

print((f'{four} 결과 : {result:.1f}'))

# 함수에 값 전달하기
# 매개변수 parameter : 함수 정의시 함수에서 사용할 변수 정의
# 매개변순느 함수 호출시 전달받은 인수로 초기화되어 사용됨
# 인수 argument : 함수 호출시 매개변수에 전달할 실제 값

# 실전예제 1 p.64  단위 환산 프로그램

#unit convert
mm = int(input('길이(mm)를 입력하세요.'))

cm = mm * 0.1
m = mm * 0.001
inch = mm / 2.54
ft = mm / 304.8

print(f'''
{mm}mm --> {cm:.2f} cm
{mm}mm --> {m:.2f} m
{mm}mm --> {inch:.2f} inch
{mm}mm --> {ft:.2f} ft

''')
def readMM():
    mm = int(input('길이(mm)를 입력하세요.'))
    return mm

def convertAll(mm):
    cm = mm * 0.1
    m = mm * 0.001
    inch = mm * 0.03937
    ft = mm * 0.003281

    return mm,cm, m, inch, ft

def convertUnit():
    mm = readMM()

    return convertAll(mm)

mm,cm, m, inch, ft = convertUnit()
print(f'''
{mm}mm --> {cm:.2f} cm
{mm}mm --> {m:.2f} m
{mm}mm --> {inch:.2f} inch
{mm}mm --> {ft:.2f} ft
''')







