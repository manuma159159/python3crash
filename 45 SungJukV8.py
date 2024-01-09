# 성적처리 프로그램 V7
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균, 학점을 계산하고 출력함
# 데이터 입력 시 input 함수 사용
# 학점 기준 : 수우미양가
# 성적데이터 입력, 조회, 상세조회, 수정, 삭제 기능 구현
# 각 기능은 메뉴식으로 구현 - 기능별 메뉴 선택시 명령 수행
# 성적 데이터는 데이터베이스 테이블에 저장
# 클래스 기반으로 재작성
import sys
import pppp1144.sjv8 as sjv8
import oracledb





while True:
    #프로그램 주 실행부
    menu = sjv8.show_menu()

    if menu == '1': sjv8.addSungJuk()
    elif menu == '2':  sjv8.show_sungjuk()
    elif menu == '3':  sjv8.showone_sungonejuk()
    elif menu == '4':  sjv8.modify_sungjuk()
    elif menu == '5':  sjv8.remove_sungjuk()
    elif menu == '0':  sjv8.exit_sungjuk()
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


