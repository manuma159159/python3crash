# 성적처리 프로그램 V1
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균을 계산하고 출력함.

#입력데이터 선언
name = '김성은'
kor = 90
eng = 90
math = 90
#성적 처리
print(kor + eng + math)
avg = (tot/3)
tot = (kor + eng + math)
print(tot)
print (avg)

# 결과출력
print (f'이름: {name:s}, 국어: {kor}, 영어: {eng}, 수학: {math}')
print (f'총점: {tot:d}, 평균: {avg:.1f}')