# 도서관리 프로그램 V1
# 도서명, 저자, 역자, 출판사, 출간일, 정가, 판매가, 할인율, 적립금
# bkname, author, publisher, pubdate, retail, price, pctoff, mileage
# 도서데이터는 데이터베이스 테이블에 저장
# 클래스 기반으로 재작성
import sys
import pppp1144.BookService as bksrv
import oracledb





while True:
    #프로그램 주 실행부
    menu = bksrv.show_menu()

    if menu == '1': bksrv.new_book()
    elif menu == '2':  bksrv.read_book()
    elif menu == '3':  bksrv.readone_book()
    elif menu == '4':  bksrv.modify_book()
    elif menu == '5':  bksrv.remove_book()
    elif menu == '0':  bksrv.exit_program()
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


