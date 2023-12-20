#1
#프로그래밍 언어 실습시 글꼴은 고정폭 글꼴을 사용할 것을 추천
print ('*   *     *     ****     ****      *    *'    )
print ('*   *   *  *    *    *   *   *     *    *'  )
print ('*****  *    *   *****    ****        * *'  )
print ('*   *  ******   *   *    *    *       *'  )
print ('*   *  *    *   *     *  *     *      *'  )


#3
rate 1, myprogram.java
rate1 = 1
#1stPlayer = 2
#myprogram.java = 3
long=4
TimeLimit = 5
numberOfWindows = 6

# 학생 테이블의 각 컬럼 데이터도 변수로 선언하고 값으로 초기화
stno = 1
hakbun = 201350050
name = '김태희'
addr = '경기도 고양시'
bith = '1985.3.22'
deptid = 1
profid = 4
regdate = '2028.12.20 14:43:15'
#4
x, y, z = 10, 20, 30
s0, v0, t, g =4, 5, 6, 9.8
print (3 * x, 3 * x + y, (x + y) /7, (3 * x +y) / (z + 2))
print ( s0 + v0 * t + 1/2 * g * t ** 2)

#5
print ((1 / 3) * 3) # 부동소수점 연산의 헛점이 원인
print (7 / 3, 7 % 3, 7 //3)
result = 2
result /= 2 # result = result /2
print (result)


#6
x, y, m, n = 2.5, 1.5, 18, 4
print(x + n * y - (x + n) * y)
print (m / n + m % n)
print (5 * x - n / 5)
print(1 - (1 - (1 - (1 - (1 - n)))))

#7
print (3 + 4.5 * 2 + 27 / 8) #가
print(True || False && 3 < 4 || (5 == 7)) #나 #우선순위대로 잘 풀어야함.
print (True || (3 < 5 && 6 >= 2)) #다
!true > 'A' #라
7 % 4 + 3 - 2 / 6 * 'Z' #마
print(bool('D') + 1 + bool('M') % 2 / 3)  #바
5.0 / 3 + 3 / 3 #사
53 % 21 < 45 / 18 #아
(4 < 6) || true && false || false && (2 > 3) #자
7 - (3 + 8 * 6 + 3) - (2 + 5 * 2) #차


#9
#   true && false && true || true      나. true || true && true && false
#   (true && false) || (true && ! false) || (false && !false)
#   (2 < 3) || (5 > 2) && !(4 == 4) || 9 != 4
#.   6 == 9 || 5 < 6 && 8 < 4 || 4 > 3  전부 프린트 붙이고 계산 해보면 됨.

#10
가.   27 / 13 + 4
나.   27 / 13 + 4.0
다.   42.7 % 3 + 18
라.   (3 < 4) && 5 / 8
마.   23 / 5 + 23 / 5.0
print (2.0 + bool('a')) #문자와 실수간 산술연산 불가
사.   2 + 'a'
print( bool('a') + bool('b') ) # 문자간 산수 연산 불가
print (bool('a') / bool('b')) #  'a' / 'b'
print (float(bool('a') / bool('b')))  # 'a' && ! 'b'
print ('a' and not 'b')  # ( double ) 'a' / 'b'
# 논리식과 산술식이 결합된 수식에서는 논리식의 결과가 True 라면 값이 출력
# 논리식의 결과가 False 라면 False 가 출력

#11
name = '홍길동'
weight = 32/5
age = 19
print (name, weight, age)
#12
# k-나이 :
# 세는 나이 : 출생시 1살, 해가 지나면 +1
# 만나이 : 출생시 0 살, 생일 지나면 + 1
# 연나이 : 현재 년도 - 출생년도

bithyear = 1997
currentyear = 2023

age = currentyear - bithyear

print ('연나이 : ', age)

#13
print ('7 x 1 = 7')
print ('7 x 2 = 14')
print ('7 x 3 = 21')
print ('7 x 4 = 28')
print ('7 x 5 = 35')
print ('7 x 6 = 42')
print ('7 x 7 = 49')
print ('7 x 8 = 56')
print ('7 x 9 = 63')

dan = 7

print (f'{dan} x 1 = {dan * 1}')
print (f'{dan} x 2 = {dan * 2}')
print (f'{dan} x 3 = {dan * 3}')
print (f'{dan} x 4 = {dan * 4}')
print (f'{dan} x 5 = {dan * 5}')
print (f'{dan} x 6 = {dan * 6}')
print (f'{dan} x 7 = {dan * 7}')

print ('%d x 1 = %d' % (dan, dan * 1))
print ('%d x 2 = %d' % (dan, dan * 1))
print ('%d x 3 = %d' % (dan, dan * 1))
print ('%d x 4 = %d' % (dan, dan * 1))
print ('%d x 5 = %d' % (dan, dan * 1))
print ('%d x 6 = %d' % (dan, dan * 1))

print ('{} x 1 = {}'.format(dan, dan*1))