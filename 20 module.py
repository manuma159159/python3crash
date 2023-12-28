# 모듈과 패키지
# 매우 복잡하고 긴 파일을 하나의 파일에
# 모두 작성하는 것은 비효율적일 수 있음 - 유지보수 힘듦
# 또한, 여러 사람과 같이 개발하는 경우
# 업무분답, 작업결과물 통합 역시 어려움

# 모듈방식을 이용하면 사용용도에 따라
# 파일별로 구분해서 작성가능
# 타인이 만들어둔 코드를 자신의 프로그램에서 활용가능
# 즉, 모듈은 변수/함수/클래스들을 모아둔 파일

# 모듈은 현재 디렉토리에 있는 파일이나
# 파이썬 라이브러리 디렉토리에 있는 파일을 불러올 수 있음
# 사용자/venv/py39/Lib/site-packages

# 모듈 불러오기
# import 명령을 이용해서 불러옴
# 모듈내 정의된 변수/함수/클래스를 사용하려면
# 모듈명.변수, 모듈명.함수, 모듈명.클래스 형식으로 코드작성

# don't reinvent the wheel!
# 이미 있는 것을 다시 만드느라 시간을 낭비하지 마라!

# 모듈의 종류
# 내장(표준) 모듈 : 파이썬에서 기본적으로 제공하는 모듈
# 사용자 정의 모듈 : 직접 개발자/조직/회사가 만든 모듈

# sys 모듈 : 파이썬 인터프리터가 제공하는
# 여러가지 기능을 다룰수 있는 함수 제공
# exit : 스크립트 종료 함수
# path : 시스템 내 모듈의 전체 경로 출력

import sys

print(sys.path) #패스의 경로가 다 보임
sys.exit()

# os 패키지
# 시스템 환경변수,디렉토리,파일등을 다루는 함수가 있는 패키지
# environ : 시스템 환경변수 확인
# chdir : 현재 디렉토리 변경
# getcwd : 현재 디렉토리 확인
# mkdir : 디렉토리 생성
# listdir : 현재 디렉토리의 파일/하위디렉토리 목록 출력
# rmdir : 디렉토리 삭제
# rename : 파일명 변경

import os

print(os.environ)  # 이건 전체적으로 보여주는 건데 path 보고싶으면 아래처럼 하면 됨. 딕셔너리로 구성되어있음
print(os.environ['PATH'])
print(os.environ['USERNAME'])

print((os.getcwd())) # 작업 디렉토리 출력
os.chdir('c:/Java')  # 경로 변경
os.mkdir('python39') # 디렉토리 생성
os.listdir()         # 디렉토리 내용 출력
os.listdir('c:/Java/python39')  # 저장한 디렉토리의 내용 출력. (탐색기 기능 구현 가능)

# 시간, 날짜 패키지
# 시간과 관련된 정보를 다루는 함수가 있는 패키지
# time : 현재시간을 실수형태로 출력 (1970.1.1 기준)
# localtime : 실수형태로 출력된 시간을
# 년/월/일 시/분/초 형태로 바꿔 출력
# ctime : 현재시간을 간단하게 출력
# strftime : 시간/날짜 관련 형식지정자를 이용해서 출력
# sleep : 지정한 시간만큼 스크립트 실행을 지연시킴

import time

print(time.time()) # time에서 time을 검색하면 1970 기준 얼마나 지났는지 보여줌
print(time.localtime(time.time()))
print(time.ctime())

# 날짜/시간을 의미하는 형식 문자열
fmt1 = '%Y-%m-%d %H:%M:%S %a'  # 24시간 format의 약자 (서식이라는 뜻)
fmt2 = '%Y-%m-%d %p %I:%M:%S %A'   # 12시간
fmt3 = '%j %w %W' # 누적일 요일 누적 주
fmt4 = '%x %X'      # 시간 날짜
# strftime (string format time) = (형식문자열, 날짜시간정보) *** 꽤 많이 사용 ***
today = time.localtime(time.time())
print(time.strftime(fmt1, today)) # (fmt1 = 형식문자열, today = 날짜시간정보)
print(time.strftime(fmt2, today))
print(time.strftime(fmt3, today))
print(time.strftime(fmt4, today))
# 공부하려면 python strftime 검색해서 들어가면 다양한 도움말을 볼 수 있음.

# 로케일, 국제화, 지역화
# 로케일 : UI에서 사용되는 언어, 지역, 출력 형식을 의미하는 문자열
# 보통 언어,지역,코드집합으로 구성됨 (ko_KR.UTF-8) 저기 fmt2에 오전,오후를 한글로 나오게 하려면 이거 하면 됨.
# 프로그램 내 UI의 텍스트가 올바르게 출력되도록 만듦 (지역에 따라)

import locale

# 전역 로케일설정 : LC_ALL 싸그리 다 바꾸는거임.
locale.setlocale(locale.LC_ALL, 'ko_KR.UTF-8')

# 국제화 (i18n) Internationalization 약자. 18의 의미는 글자 개수
# 프로그램이 특정 지역이나 언어에 종속되는 것을 피하고
# 다양한 지역, 언어로 정상적으로 작동되도록 설계하고 개발하는 것

# 현지화 (localization) 국제화와 반대
# 기존에 이미 개발된 프로그램을
# 특정 지역, 언어에 맞춰 프로그램을 설계하고 개발하는 것

# datetime 모듈
# time 모듈과 달리 시간대를 이용한 현지 시간 출력기능이 추가
# 날싸/시간 차이 계산 등 기능들이 추가

import datetime

#print(datetime.datetime.now())
today = datetime.datetime.now()
print(today)

print(today.strftime(fmt1))
print(today.strftime(fmt2))
print(today.strftime(fmt3))
print(today.strftime(fmt4))

# 달력 패키지
# 달력과 관련된 정보를 다루는 함수가 있는 패키지
# calendar : 지정한 년도 달력 출력
# prmonth : 지정한 월 달력 출력
# weekday : 지정한 일자의 요일 출력 (0:월요일)
# monthrange : 지정한 월의 첫날의 요일과 마지막날 출력 (0:월요알)
# isleap : 윤년여부를 True/False로 출력

import calendar

print(calendar.calendar(2023))
print(calendar.prmonth(2023,12))

# 0 = 월요일 그래서 목요일이 3인거임
print(calendar.weekday(2023,12,28))

print(calendar.isleap(2023))
print(calendar.isleap(2024))

# 난수생성 패키지
# 난수를 생성하는 함수를 포함하는 패키지
# randint : 지정한 범위 내 난수 생성
# choice : 리스트 내에서 무작위 항목 복원 추출  # 확률할 때 배운 것. 주머니에서 공 빼고 다시 공 넣음
# pop : 리스트 내에서 무작위 항목 비복원 추출   # 주머니에서 공 빼고 공 다시 안넣음.
# 리스트 내에서 무작위 항목 비복원 추출 직접 해야할듯 pop 안됨;;
import random

for _ in range(6):
    print(random.randint(1,45), end= ',')

menu = ['라면','짜장','돈까스','카레','해장국']
# 복원 추출
for _ in range(5):
    print(random.choice(menu),end=',')
# 비복원 추출
for _ in range(5):
    item =random.choice(menu)
    print(item, end=',')
    menu.remove(item)  # 선택한 메뉴는 리스트에서 제거 두번은 안돼. 비복원 추출이라 더이상 뽑을게 없어서 그럼

# 비복원 추출방식으로 로또 6/45 작성
nums = list(range(1,46))
for _ in range (6):
    move = random.choice(nums)
    print(move, end=',')
    nums.remove(move)

# 직렬화/역직렬화 패키지
# 메모리에 생성된 객체를 그대로 파일에 저장하고
# 불러오도록 해주는 패키지
# 데이터 분석 결과 모델을 파일로 저장하거나 불러올때
# 주로 많이 사용함
# dump : 객체를 지정한 파일에 저장(직렬화)
# load : 파일에 저장된 객체를 메모리에 저장(역직렬화)
# 데이터를 그냥 냉동밥 같이 저장해버리는게 직렬화. 냉동실에서 꺼내서 전자렌지 돌린 밥 상태가 역직렬화

person = {'name': '아이유', 'addr': '서울 관악구', 'age': 32, 'email': 'sdfon@naver.com' }
print(person)

import os
import pickle  # pickle은  파이썬에서 객체를 직렬/역직렬 하는데 사용되는 모듈이다.
               # 1.객체 저장 및 불러오기, 2.프로세스 간 데이터 공유, 3. 캐싱

# 직렬화.
os.chdir('c:/Java/python39')
# 파일 저장 : with open(파일경로, 파일모드)
with open('person.pickle','wb') as f: # person.pickle파일을 wb(쓰기)파일로 실행하는 이걸 f 라고 칭하라는 뜻.
    # dump (객체명, 대상)
    pickle.dump(person, f)

# 역직렬화
person = ''
os.chdir('c:/Java/python39')
# 파일 저장 : with open(파일경로, 파일모드)
with open('person.pickle','rb') as f: # person.pickle파일을 rb(읽기)파일로 실행하는 이걸 f 라고 칭하라는 뜻.
    # load (대상)
    person = pickle.load(f)



# 테스트