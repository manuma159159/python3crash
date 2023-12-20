# 성적처리 프로그램 V2
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균을 계산하고 출력함
# 단, 리스트를 이용해서 학생 3명에 대해 성적처리를 진행함

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

subs = ['kor','eng','math']

print(subs)

names = ['채리','종서','세경']
subs[0] = [77,57,97]
subs[1] = [89,69,89]
subs[2] = [77,100,57]

print (names[0])
print (names[0],grades2[0])

print (names[0],grades1[0],grades3[0])
print(names[0],grades3)
print(names[0],subs[0])
print(names[0],subs[0][1])
