#import oracledb dbinfo에 있어서 안씀
import sys
from pppp1144.BookDAO import BookDAO
from pppp1144.Book import Book


# 메뉴 출력
def show_menu():
    '''
    메뉴 출력하고 메뉴항목을 입력받음
    :return: 입력받은 메뉴번호
    '''
    main_menu = '''
    도서관리 프로그램 v1
    ------------------
    1. 도서 데이터 추가
    2. 도서 데이터 조회
    3. 도서 데이터 상세조회
    4. 도서 데이터 수정
    5. 도서 데이터 삭제
    0. 프로그램 종료
    ------------------
    '''
    print(main_menu, end='')
    menu = input('=> 메뉴를 선택하세요: ')
    return menu


def input_book():
    bkname = input('도서명은?')
    author = input('도서 저자는?')
    publisher = input('도서 출판사는?')
    pubdate = input('도서 출간일은?')
    retail = input('도서 소매가는?')
    pctoff = input('도서 할인율은?')

    bk = Book(bkname, author, publisher, pubdate, retail, pctoff)

    bk.price = bk.retail * (1-(bk.pctoff/100))
    bk.mileage = bk.retail * (bk.pctoff/100)
    return bk


def new_book():
    """
    도서데이터 추가 (입력 - 처리 - 저장)
    :return:
    """
    print('도서데이터 추가')

    bk = input_book()
    
    rowcnt = BookDAO.insert_book(bk)
    print(f'{rowcnt} 건의 도서데이터 등록됨')


# 모든 도서 데이터 출력 (번호/이름/국어/영어/수학/등록일)
def read_book():
    """
    모든 도서 데이터 출력 (번호/도서명/저자/출판사/판매가)
    :return: 이름,국어,영어,수학 데이터를 나타냄
    """

    print('도서데이터 조회')

    pass

#도서 상세 조회
def readone_book():
    """
    도서 상세 조회
    :return: 이름부터 학점까지 전부 나타냄
    """
    bkname = input('상세 조회할 도서명은?')
    pass

# 도서 데이터 수정
def modify_book():
    """
    도서 데이터 수정
    :return: 수정된 도서데이터가 테이블에 저장
    """

    bkno = input('수정할 도서번호는?')
    # 튜플 객체를 수정하기 위해 리스트로 전환
    pass

def remove_book():
    """
    도서데이터 삭제
    :return: 도서 데이터가 json파일에서 삭제됨. count도 줄어들음.
    """
    bkno = input('삭제할 번호는?')
    pass



# 도서처리 프로그램 종료
def exit_program():
    """
    book program exit. 도서처리 프로그램 종료 함수
    :param: None
    :return: None
    """
    print('프로그램 종료')  # 위에 초록색은 주석을 달아놓은 것. 설명에 관한 주석임. 굳이 들어오지 않아도 볼 수 있도록.
    sys.exit(0)


