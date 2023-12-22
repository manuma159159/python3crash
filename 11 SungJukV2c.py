# 성적처리 프로그램 V2
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균, 학점을 계산하고 출력함
# 데이터 입력 시 input 함수 사용
# 학점 기준 : 수우미양가
#입력데이터 선언
names = []
kors = []
engs = []
maths = []

tots = []
avgs = []
grds = []

# 성적 데이터 입력
for i in range(3):
    print(f'{i+1}번째 학생데이터 입력')
    names.append(input('이름은?:'))
    kors.append(int(input('국어는?')))
    engs.append(int(input('영어는?')))
    maths.append(int(input('수학은?')))

#성적처리
for i in range (len(names)):
    tots.append(kors[i] + engs[i] + maths[i])
    avgs.append(tots[i] / 3)
    avg = avgs[len(avgs)-1]
    grd = '수' if avg >= 90\
        '우' if avg >= 80 else '미' \
        '미' if avg >= 70 else '양' \
        '양' if avg >=60 else '가'
            grds.append(grd)
#결과 출력
for i in range(len(names)):
    print(f'이름: {names[i]:s}, 국어: {kors[i]}, 영어: {engs[i]}, 수학:{maths[i]}')
    print(f'총점: {tots[i]:d}, 평균: {avgs[i]:.1f}, 학점 : {grds[i]}')


#
result = '수' if '90'< kors,engs,maths <='100' else '탈락'
print(f'{result}')