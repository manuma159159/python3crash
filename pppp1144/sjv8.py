#import oracledb dbinfo에 있어서 안씀
import sys
from pppp1144.SungJukService import SungJukService
from pppp1144.SungJukDAO import SungJukDAO
from pppp1144.SungJuk import Sungjuk



# 메뉴 출력
def show_menu():
    '''
    메뉴 출력하고 메뉴항목을 입력받음
    :return: 입력받은 메뉴번호
    '''
    main_menu = '''
    성적처리 프로그램 v8
    ------------------
    1. 성적 데이터 추가
    2. 성적 데이터 조회
    3. 성적 데이터 상세조회
    4. 성적 데이터 수정
    5. 성적 데이터 삭제
    0. 프로그램 종료
    ------------------
    '''
    print(main_menu, end='')
    menu = input('=> 메뉴를 선택하세요: ')
    return menu



def addSungJuk():
    """
    성적데이터 추가 (입력 - 처리 - 저장)
    :return:
    """
    print('성적데이터 추가')
    sj = SungJukService.read_sungjuk() # 리드성적 박스하고 컨트롤 d 하면 자세히 볼 수있음.
    SungJukService.compute_sungjuk(sj)

    rowcnt = SungJukDAO.insert_sungjuk(sj)
    print (f'{rowcnt} 건의 성적데이터 추가됨!!')





# 모든 성적 데이터 출력 (번호/이름/국어/영어/수학/등록일)
def show_sungjuk():
    """
    모든 성적 데이터 출력 (번호/이름/국어/영어/수학/등록일)
    :return: 이름,국어,영어,수학 데이터를 나타냄
    """

    print('성적데이터 조회')

    rows = SungJukDAO.select_sungjuk()
    for row in rows:
        print(f'{row[0]}{row[1]}{row[2]}{row[3]}'
              f'{row[4]}{str(row[5])[10]}')

#성적 상세 조회
def showone_sungonejuk():
    """
    성적 상세 조회
    :return: 이름부터 학점까지 전부 나타냄
    """
    sjno = input('상세 조회할 학생번호는?')
    row = SungJukDAO.selectone_sungjuk(sjno)

    print(f' {row[0]} {row[1]} {row[2]} {row[3]} {row[4]} '
          f' {row[5]} {row[6]} {row[7]} {row[8]} ')

# 성적 데이터 수정
def modify_sungjuk():
    """
    성적 데이터 수정
    :return: 수정된 성적데이터가 테이블에 저장
    """

    sjno = input('수정할 학생번호는?')
    # 튜플 객체를 수정하기 위해 리스트로 전환
    sj = list(SungJukDAO.selectone_sungjuk(sjno))

    if sj[0]: # 만일 수정할 데이터가 존재한다면
        sj[1] = input(f'새로운 이름은? ({sj[1]}): ')
        sj[2] = int(input(f'새로운 국어점수는? ({sj[2]}): '))
        sj[3] = int(input(f'새로운 영어점수는? ({sj[3]}): '))
        sj[4] = int(input(f'새로운 수학점수는? ({sj[4]}): '))
        # 조회한 결과를 클래스 타입으로 변경 후 다시 성적처리
        sj = Sungjuk(sj[1],sj[2],sj[3],sj[4])
        SungJukService.compute_sungjuk(sj)

        rowcnt = SungJukDAO.update_sungjuk(sj,sjno)
        print(f'{rowcnt}의 데이터가 수정되었습니다.')

    else:
        print('데이터가 존재하지않습니다.')


def remove_sungjuk():
    """
    성적데이터 삭제
    :return: 성적 데이터가 json파일에서 삭제됨. count도 줄어들음.
    """
    sjno = input('삭제할 번호는?')
    rowcnt = SungJukDAO.delete_sungjuk(sjno)
    print(f'{rowcnt}의 데이터가 삭제되었습니다.')



# 성적처리 프로그램 종료
def exit_sungjuk():
    """
    sungjuk program exit. 성적처리 프로그램 종료 함수
    :param: None
    :return: None
    """
    print('프로그램 종료')  # 위에 초록색은 주석을 달아놓은 것. 설명에 관한 주석임. 굳이 들어오지 않아도 볼 수 있도록.
    sys.exit(0)


