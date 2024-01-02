# 성적처리 프로그램 V5
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균, 학점을 계산하고 출력함
# 데이터 입력 시 input 함수 사용
# 학점 기준 : 수우미양가
# 성적데이터 입력, 조회, 상세조회, 수정, 삭제 기능 구현
# 각 기능은 메뉴식으로 구현 - 기능별 메뉴 선택시 명령 수행
# 성적 데이터를 dict 자료구조로 구현
# 성적 처리기능을 함수로 구현
import sys
import pppp1144.sjv5b as sjv5b

# #입력데이터 선언
sungjuks ={'response' : {'body': {'totalCount':999, 'items': []}}}

names = []
kors = []
engs = []
maths = []

tots = []
avgs = []
grds = []

#프로그램 메뉴 출력을 위한 변수 선언

while True:
    #프로그램 주 실행부

    sjv5b.show_menu()
    menu = input('=> 메뉴를 선택하세요: ')

    # 선택한 메뉴에 따라 해당 기능 수행
    if menu == '1' :
        print('성적데이터 추가')

        sj = sjv5b.read_sungjuk()
        sjv5b.compute_sungjuk(sj)

        sungjuks['response']['body']['items'].append(sj)


    elif menu == '2':
        print('성적데이터 조회')
        sjv5b.show_sungjuk(sungjuks)

    elif menu == '3': print('성적데이터 상세조회')
    elif menu == '4': print('성적데이터 수정')
    elif menu == '5': print('성적데이터 삭제')
    elif menu == '0':
        print('프로그램 종료')
        sys.exit(0)
    else:print('메뉴를 잘못 선택하셨습니다.')



# # 성적 데이터 입력
# for i in range(3):
#     print(f'{i+1}번째 학생데이터 입력')
#     names.append(input('이름은?:'))
#     kors.append(int(input('국어는?')))
#     engs.append(int(input('영어는?')))
#     maths.append(int(input('수학은?')))
#
# #성적처리
# for i in range (len(names)):
#     tots.append(kors[i] + engs[i] + maths[i])
#     avgs.append(tots[i] / 3)
#     avg = avgs[len(avgs)-1]
#     grd = '수' if avg >= 90 else '우'\
#             '우' if avg >= 80 else '미' \
#             '미' if avg >= 70 else '양' \
#             '양' if avg >=60 else '가'
#     grds.append(grd)
# #결과 출력
# for i in range(len(names)):
#     print(f'이름: {names[i]:s}, 국어: {kors[i]}, 영어: {engs[i]}, 수학:{maths[i]}')
#     print(f'총점: {tots[i]:d}, 평균: {avgs[i]:.1f}, 학점 : {grds[i]}')


