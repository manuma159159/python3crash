# 변수
# 어떠한 값을 저장하는 장소를 기억하기 쉽게 문자형태로 나타낸 것
# 변수에 값이 저장되는 공간을 메모리라 함
# 변수에 값을 넣으라고 선언하면,
# 시스템상의 메모리 어딘가에 공간을 확보하고
# 그 공간의 실제주소와 이름을 매핑함

a = '홍길동'
b = 99

name = '홍길동' # 의미있는 단어로 변수 선언
age = 99

#변수 명은 대소문자 구분
Name = '일지매'

# 변수에 저장된 값을 출력하려면 print 함수 사용
print(name,age,Name)

# 파이썬의 자료형(data-type)
# 정적 타입 : 변수 선언시 자료형도 같이 표시
#            (String name = "홍길동")
#            (name = 123) (오류발생-선언시 자료형과 값의 유형이 다름)

# 동적 타입 : 변수 선언시 자료형은 생략 가능, 추론기능으로 자동할당,
#            또한, 변수에 대입하는 값에 따라 자료형이 바뀜
#            (name = '홍길동')
#            (name = 123) (문제없음-변수의 자료형은 자동으로 변경)

# 변수의 자료형을 알아보기 위해 type 함수 사용
print (type(name))

name = 123 # 동적 자료형 변환 시험
print (type(name))

# ex) 회원정보 저장용 변수 선언
# 아이디, 비번, 이름, 나이, 이메일,
# 결혼여부, 보유금액, 등록일

userid = 'abc123'
passwd = 'clouds'
name = '김성은'
age = 27
email = abc123@987xyz.com
isMarriage = True
hadMoney = 1000000000
regdate = '2023-12-19 16:15:55'

# 파이썬 자료형 - 정수, 실수, 문자, 불리언 boolean
# 정수 자료형 - 소수점 이하의 값이 없는 수
int1 = 123
int2 = 0b01010101  # 2진수

print (int1, int2, bin(int2))

# 실수 자료형 - 소수점 이하의 값이 있는 수

# 부동소수점 floating point 실수 : 국제표준에 따라 실수를 표기한다
# 즉 , 실수를 정수부와 정수의 곱으로 된 지수로 표현하는 것을 나타낸다.
# 예 ) 123.456 => 123456 x 10^-3
# 단, 파이썬에서는 유효숫자 e 지수를 이용해서 지수부를 표현
float1 = 10.0
float2 = 123456e-3
print (float1,float2)
#부동소수점과 오차
# 컴퓨터에서는 숫자는 비트를 이용해서 표기하기 때문에
# 실수는 정확하게 나타낼 수 없으므로 바로 아래거인 0.1+0.2=0.3 이게 false가 뜨는거임
%precision 55
0.1 + 0.2 == 0.3

round(0.1, 0) + round(0.2, 0) == round(0.3, 0)

round(0.1 + 0.2, 5) == round(0.3, 5)

# 문자 자료형
# 파이썬에서 글자 char를 문자열 string이라 표현
# 문자열은 ''나 "" 를 이용해서 정의 가능 - '' 추천.

#여러줄 문자열(텍스트) 작성할 때는 ''' '''를 사용
str1 = 'Hello World!!'
str2 = 'Hello, \nWorld!!'
str3 = 'Hello \
World!!' #긴 문장은 \ 로 나눠 작성 가능
str4 = '''Hello, 
World!!'''

print(str1)
print(str2)
print(str3)
print(str4)

# 불리언 자료형
# 참 , 거짓을 나타내는 자료형
#True , False 등으로 표현.
# 한편 숫자가 0이거나 빈 문자열이면 False로 표현
bool1 = True
bool2 = False
bool3 = 0
bool4 = ''

print(bool1,bool2)
print(bool(bool3), bool(bool4))


다음 숫자를 유효숫자 e 지수 표현