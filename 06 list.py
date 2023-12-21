
# 파이썬 자료구조
# 자료구조는 대량의 데이터를
# 효율적으로 저장,조회,수정,삭제하기 위해
# 요구되는 기능과 기법을 의미
# 대표적인 자료구조 : 리스트, 튜플, 셋, 딕셔너리

# 성적프로그램 v2
# 이름,국어,영어,수학을 이용해서
# 총점,평균을 처리해서 결과출력
# 단, 3명의 학생에 대해 성적처리를 진행함
# 변수 초기화
name1, name2, name3 = '혜교', '지현', '수지'
kor1, kor2, kor3 = 99, 65, 75
# ...
# 처리할 데이터 갯수에 따라 변수를 일일이 선언해야 함 - 불편!

# tot1 = kor1 + eng1 + mat1
# tot2 = kor2 + eng2 + mat2
# tot3 = kor3 + eng3 + mat3
# ...
# 성적처리시에도 동일한 코드를 여러번 반복해 작성함 - 번거로움
# => 이러한 문제를 해결하기 위해 자료구조와 관련된 기술을 사용


# 리스트list
# 다른 프로그래밍 언어에서는 배열array과 유사
# 동일한(동일하지 않은) 형식의 데이터를
# 1차원 형태로 순차적으로 저장하는 자료구조 (중복 허용)
# 선언방법은 값들을 []안에 정의하고 사용
# 리스트의 각 요소에 접근(참조)하려면 변수[인덱스] 형식을 사용

# 과일 데이터 저장
fruits = ['사과','포도','수박','참왜','배','자두','복숭아','바나나']
print (fruits)

# 저녁메뉴를 리스트로 선언
menus = ['라면','돈까스','짜장면','냉면','정식','초밥','스테이크','파스타']
print (menus)

#리스트에서 일부 요소 element, item만 출력
#단 첫번째 요소의 위치값 index는 0임
print (menus[0], menus[5])

#동적으로 리스트 생성하기
menus = []

#리스트에 요소를 추가하려면 append 함수 사용
#추가된 요소는 리스트의 맨 뒤에 부착 - FIFO
menus.append('라면')
menus.append('돈까스')  # 파스타 뒤에 라면 뒤에 다시 위치함.

# 지정한 위치에 새로운 요소 추가 : insert (위치, 값)
# 지정한 위치에 이미 값이 존재한다면 기존에 있던 값은 뒤로 밀림.
menus.insert(2,'냉면')

print(menus)

#리스트 요소 수정 : 리스트명[위치] = 새로운 값
print(menus[3])
menus[3] = '탕수육'

#리스트 요소 삭제 1 : remove(값)
menus.remove('탕수육')
print(menus)
#리스트 요소 삭제 2 : pop(위치)
#지정한 위치 뒤에 값이 존재한다면 그 값은 앞으로 당겨짐
menus.pop(2)
#리스트 요소 삭제 3 : pop () - 위치로 삭제. 맨 뒤 요소 삭제
menus.pop()

#리스트로 다양한 데이터 다루기
sjs = []
sj = ['아이유',77,89,77]
sjs.append(sj)

sj = ['종서',57,69,100]
sjs.append(sj)

sj = ['세경',97,89,57]
sjs.append(sj)

print(sjs)
print(sjs[0])
print(sjs[1])
print(sjs[2])

#참석자 명단 선언
attendList = ['민우', '병수', '병헌']

#참석자 수 확인 : len
len(attendList)

#문자열에 len 함수 적용시 문자열의 길이 출력
str = 'HEllo World!!'
print(len(str))

#사용자로부터 데이터 입력받기 : input
name = input('이름을 입력하세요 :')

#사용자에게 정수 2개를 입력받아 더한 후 출력
#input 으로 입력받은 내용은 무조건 문자로 처리
# 만약, 숫자를 입력받길 원한다면, 적절한 변환 필요.
num1 = input('첫번째 정수는?')
num2 = input('첫번째 정수는?')

print (num1, num2, num1 + num2)

username = input ('이름을 입력하세요')

print (username)
# 날씨 예보

date = input ('날짜는?')
day = input('아침기온을 입력하세요')
mtemp = input ('최저기온을 입력하세요')
ntemp = input('낮기온 확률을 입력하세요')
rainprop = input('비 올 확률 입력하세요')
air = input('미세먼지수치 입력하세요')
rsun = input('일출 시간을 입력하세요')
dsun = input ('일몰를 입력하세요')
swave = input ('남해앞바다를 입력하세요')
wwave = input ('서해앞바다를 입력하세요')
ewave = input ('동해 앞바다 물결은?')

weather = f''''
내일 날씨 예보입니다.
{day}요일인 {date}의 아침 최저 기온은 {mtemp}도, 낮 최고 기온은 {ntemp}. 비올 확률은 {rainprop}%
이고 미세먼지는 {air}수준일 것으로 예상됩니다. 일출 시간은 {rsun}이고, 일몰시간은 {dsun} 입니다.
바다의 물결은 남해 앞바다 {swave}m, 동해 앞바다 {ewave}m, 서해앞바다는 {swave}m 입니다. 지금까지 {date}{day}요일 날씨 예보였습니다.
'''
print (weather)
print(('''
    내일 날씨 예보입니다.
    요일인 의 아침예보 됐습니다.
    예상됩니다.~~~

'''))

# 입력한 글자 수 확인하기
# 메세지 입력받아 메세지의 문자길이 출력

message = input('메시지를 입력하세요')
print(message)
print(len(message))