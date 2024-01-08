import oracledb
import sys

# 데이터베이스 연결정보
host = ''
userid = '' # 빅데
passwd =  ''
sid = 'FREE'


dsn_tns = oracledb.makedsn(host, 1521, sid)

# 메뉴 출력
def show_menu():
    '''
    메뉴 출력하고 메뉴항목을 입력받음
    :return: 입력받은 메뉴번호
    '''
    main_menu = '''
    성적처리 프로그램 v7
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


def read_sungjuk() :
    '''

    :return:
    '''
    sungjuk = input('이름과 성적을 입력하세요 (예: 홍길동 99 88 99) : ')
    data = sungjuk.split() # 빈칸으로 문자열 분리
    name = data[0]
    kor = int(data[1])
    eng = int(data[2])
    math = int(data[3])
    sj = [name,kor,eng,math]  # 입력받은 성적데이터를 리스트에 담음
    return sj

# 성적 처리 ( 총점 / 평균 / 학점 계산 )
def compute_sungjuk(sj):
    """
    성적 처리 ( 총점 / 평균 / 학점 계산 )
    :param sj: read_sungjuck
    :return: 성적처리되니 성적데이터
    """
    tot = sj[1] + sj[2] + sj[3]
    avg = float(f"{tot/ 3:.1f}")
    grd = '수' if avg >= 90 else '우' \
    '우' if avg >= 80 else '미' \
    '미' if avg >= 70 else '양' \
    '양' if avg >= 60 else '가'

    return [sj[0],sj[1],sj[2],sj[3],tot,avg,grd]


# 성적 데이터 저장 (sungjuks 테이블)
def save_sungjuk(sj):
    """
    성적 데이터 저장 (sungjuks 테이블)
    :param sj: 입력받아 처리된 성적데이터
    :return: sungjuks 테이블에 저장을 하게 함
    """
    sql = ' insert into sungjuks(name, kor, eng, math, tot, avg, grd) '\
          ' values (:name,:kor,:eng,:math,:tot,:avg,:grd) ' # 이렇게 걸어놔야함
            #' values (:1,:2,:3,:4,:5,:6,:7) ' 이것도 됨 이걸 더 많이 씀
           #' values (?,?,?,?,?,?,?) ' 이건 오라클에서 안됌. 마리아디비에서만

    conn = oracledb.connect(user=userid, password=passwd, dsn=dsn_tns)
    cursor = conn.cursor()

    cursor.execute(sql,sj)
    conn.commit()
    print(cursor.rowcount, '건의 성적데이터 추가됨')

    cursor.close()
    conn.close()

# 성적데이터 추가 (입력 - 처리 - 저장)
def addSungJuk():
    """
    성적데이터 추가 (입력 - 처리 - 저장)
    :return:
    """
    print('성적데이터 추가')
    sj = read_sungjuk()
    sj = compute_sungjuk(sj)
    save_sungjuk(sj)


# 모든 성적 데이터 출력 (번호/이름/국어/영어/수학/등록일)
def show_sungjuk():
    """
    모든 성적 데이터 출력 (번호/이름/국어/영어/수학/등록일)
    :return: 이름,국어,영어,수학 데이터를 나타냄
    """

    sql = ' select sjno,name,kor,eng,math,grd from sungjuks'\
          ' order by sjno desc '

    conn = oracledb.connect(user=userid, password=passwd, dsn=dsn_tns)
    cursor = conn.cursor()

    cursor.execute(sql,)

    for sjno, name, kor, eng, math, regdate in cursor:
        print(sjno, name, kor, eng, math, str(regdate)[:10])

    cursor.close()
    conn.close()

    print('성적데이터 조회')


#성적 상세 조회
def showone_sungonejuk():
    """
    성적 상세 조회
    :return: 이름부터 학점까지 전부 나타냄
    """
    sjno = input('상세 조회할 학생번호는?')

    sql = ' select * from sungjuks where sjno = :1 '

    conn = oracledb.connect(user=userid, password=passwd, dsn=dsn_tns)
    cursor = conn.cursor()

    cursor.execute(sql,[sjno])


    for sjno, name, kor, eng, math, tot, avg, grd, regdate in cursor:
        print(sjno, name, kor, eng, math,tot, avg, grd, regdate)

    cursor.close()
    conn.close()



# 성적 데이터 수정시 수정할 데이터 입력 받기
def read_again(sjno):
    """
    성적 데이터 수정시 수정할 데이터 입력 받는 함수
    :param sjno: 기존에 저장된 성적데이터
    :param sjno: 수정할 데이터의 이름
    :return: 새롭게 생성된 성적데이터
    """
    sql = ' select name, kor, eng, math from sungjuks where sjno = :1 '
    conn = oracledb.connect(user=userid, password=passwd, dsn=dsn_tns)
    cursor = conn.cursor()

    cursor.execute(sql,[sjno])

    sj = [None,None,None,None]
    for name, kor, eng, math in cursor:
        sj = [name, kor, eng, math]

    cursor.close()
    conn.close()

    if sj[0]: # 만일 수정할 데이터가 존재한다면
        sj[0] = input(f'새로운 이름은? ({sj[0]}): ')
        sj[1] = int(input(f'새로운 국어점수는? ({sj[1]}): '))
        sj[2] = int(input(f'새로운 영어점수는? ({sj[2]}): '))
        sj[3] = int(input(f'새로운 수학점수는? ({sj[3]}): '))
        sj = compute_sungjuk(sj)

    
    return sj


# 성적 데이터 수정
def modify_sungjuk():
    """
    성적 데이터 수정
    :return: 수정된 성적데이터가 테이블에 저장
    """

    sjno = input('수정할 학생번호는?')

    # 수정할 학생 데이터를 찾았다면 새로운 값을 입력받고 다시 성적처리함

    sj = read_again(sjno)

    if sj[0] : # 수정할 데이터를 찾았다면
        sql = ' update sungjuks set name = :1, kor = :2, eng = :3, math = :4, '\
              ' tot = :5, avg = :6, grd = :7, regdate=sysdate where sjno = :8 '
        sj.append(sjno)
        conn = oracledb.connect(user=userid, password=passwd, dsn=dsn_tns)
        cursor = conn.cursor()
        cursor.execute(sql,sj)
        conn.commit()

        print(f'{cursor.rowcount} 건의 데이터가 수정되었습니다!')

        cursor.close()
        conn.close()


    else:
        print('찾으시는 데이터가 없습니다.')

# 성적데이터 삭제
def remove_sungjuk():
    """
    성적데이터 삭제
    :return: 성적 데이터가 json파일에서 삭제됨. count도 줄어들음.
    """

    sjno = input('삭제할 학생번호는?')
    sql = ' delete from sungjuks where sjno = :1 '
    conn = oracledb.connect(user=userid, password=passwd, dsn=dsn_tns)
    cursor = conn.cursor()


    cursor.execute(sql,[sjno])
    conn.commit()
    print(f'{cursor.rowcount}의 데이터가 삭제되었습니다.')
    cursor.close()
    conn.close()



# 성적처리 프로그램 종료
def exit_sungjuk():
    """
    sungjuk program exit. 성적처리 프로그램 종료 함수
    :param: None
    :return: None
    """
    print('프로그램 종료')  # 위에 초록색은 주석을 달아놓은 것. 설명에 관한 주석임. 굳이 들어오지 않아도 볼 수 있도록.
    sys.exit(0)


