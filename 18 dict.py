# 딕서너리
# 이름key과 값value으로 구성된 연관배열의 일종
# 자료구조 만들때 {}를 사용하고
# 이름과 값은 : 으로 구분해서 정의함
# 다른 언어의 JSON과 유사한 구조
# 데이터분석시 주로 사용하는 자료구조 : mongodb
# 키를 통해 자료를 찾는 해쉬테이블을 이용하므로 검색속도가 빠름

# 확인문제 2 p.26 -24
mids = {'C/C++': 'A','Java': 'B+', '네트워킹': 'C',
        '보안': 'A+', '해킹': 'F', '시스템': 'C+'} # 과목명으로 하는 이유는 유니크해서
print(mids)

# 회원정보를 dict로 선언
# key : 이름, 아이디, 비번, 이메일, 주소, 성적(국영수)
member = {'name': '채리','userid': 'pppp1144',
          'passwd':'123','email': '123','addr': '123',
          'sungjuk': [99,98,97]}
print(member)
# 딕셔너리 다루기
# 조회 : 변두명[키], 변수명/{get})키

print(member)
# 딕셔너리 수정하기
member['name'] = '성은'
member['passwd'] = member['passwd'] + str(1)
print(member['passwd'])

# 존재하지 않는 키 지정식
member['zipcode'] ='12345'
member['addr'] ='서울시'

print(member)
#기존항목삭제 :del 변수명[키] ,변수명.pop(값
del member['zipcode']
print(member)

#존재하지 않는 키 삭제시

del member['blood']   #오류 발생
member.pop('blood')   #오류 발생
member.pop('blood', None)

# 항목수 조회 : len
print(len(member))

# dict의 모든 키/값 조회 : keys, values
print(member.keys())
print(member.values())

# dict 전체 항목 출력
# 출력형식은 '키 = 값'
for key in member.keys():
    print(f'{key} = {member[key]}')

# 문제 p.33 -34 중간고사 성적 관리하기

#1
mids = {'C/C++': 'A','Java': 'B+', '네트워킹': 'C',
        '보안': 'A+', '해킹': 'F', '시스템': 'C+'}
#2
print(mids['Java'], mids['시스템'])
#3
mids['파이썬'] = 'A'
mids['OS'] = 'A+'
print(mids)
#4
mids['Java'] = 'F'
mids['시스템'] = 'A'
#5
for key in mids.keys():
    print(f'{key} : {mids[key]}')

#예제 p.37 -24 수학시험 프로그램
quizes = (('3+2는? (3점)', 5, 3), ('5÷2의 몫은? (5점)', 2, 5),('10-2는? (3점)', 8, 3),('10^2*2는? (5점)',200, 5),
          ('1 - (10÷4)의 나머지는? (5점)', -1, 5),('2^4은? (3점)', 16, 3),('4 ÷ 2는? (3점)', 2, 3))

trueCount = 0
falseCount = 0
totalCount = 0

for idx, q in enumerate(quizes):
    print(f'문제 {idx+1}/7 : ', q[0])
    answer = int(input('정답을 입력하세요 : '))

    if answer == q[1] :
        trueCount += 1
        totalCount += q[2]
    else : falseCount += 1

print((f'''
-------------------------
정답 개수 : {trueCount}
오답 개수 : {falseCount}
점수 : {totalCount}
'''))

# 예제 p. 38 -24 회원가입 프로그램
users = {}

# while True:    이게 뼈대
#     menu = input('1. 회원가입, 2. 프로그램 종료 : ')
#     if menu == '1':
#         pass
#     elif menu == '2':
#         break
#     else :
#         print('잘못입력하셨습니다.')
users = {}
while True:
    menu = input('1. 회원가입, 2. 프로그램 종료 : ')
    if menu == '1':
        userid = input('아이디를 입력하세요')
        passwd = input('비밀번호를 입력하세요')
        users[userid] = passwd
    elif menu == '2':
        print('---------------------')
        print('아이디 : 비밀번호')
        print('---------------------')
        for k in users.keys():
            print(f'{k} : {users[k]}')
        print('---------------------')
        break
    else:
        print('잘못입력하셨습니다.')

# 회원가입 version 2 ****************
users =  {'response' : {'body': {'totalCount':999, 'items': []}}}

# print(users['response']['body']['totalCount'])
# print(users['response']['body']['items'])    # 이건 그냥 예시
# users['response']['body']['items'].append('aaaaa')
print(users['response']['body']['items'].append({'uid':'abc', 'pwd' :'123'}))
print(users['response']['body']['items'].append({'uid':'xyz', 'pwd' :'987'}))
print(users['response']['body']['items'])

# for item in users['response']['body']['items']:
#     print(item)

for item in users['response']['body']['items']:
    for key in item.keys():
        print(key,item[key])

while True:
    menu = input('1. 회원가입, 2. 프로그램 종료 : ')
    if menu == '1':
        userid = input('아이디를 입력하세요')
        passwd = input('비밀번호를 입력하세요')
        user = {}
        user['userid'] = userid
        user['passwd'] = passwd
        users['response']['body']['items'].append(user)
    elif menu == '2':
        print('---------------------')
        print('아이디 : 비밀번호')
        print('---------------------')
        for item in  users['response']['body']['items']:
            for k in item.keys():
                print(f'{k} : {item[k]}')
        print('---------------------')
        break
    else:
        print('잘못입력하셨습니다.')

