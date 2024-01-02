# 함수 정의
def read_sungjuk() :
    sj = {}
    sj['name'] = (input('이름은?:'))
    sj['kor'] = int(input('국어는?'))
    sj['eng'] = int(input('영어는?'))
    sj['math'] = int(input('수학은?'))
    return sj


def show_sungjuk(): # 성적데이터 출력
    print('성적데이터 조회')
    with open('sungjuks.csv', encoding='utf-8')as f:
        sjs = f.readlines()
    for sj in sjs:
        item = sj.split(',')
        print(f"이름: {item[0]:s}, 국어: {item[1]}, 영어: {item[2]}, 수학:{item[3]}")


def show_menu():
    main_menu = '''
    성적처리 프로그램 v6b
    ------------------
    1. 성적 데이터 추가
    2. 성적 데이터 조회
    3. 성적 데이터 상세조회
    4. 성적 데이터 수정
    5. 성적 데이터 삭제
    0. 프로그램 종료
    ------------------
    '''
    print(main_menu, end= '')
    menu =  input('=> 메뉴를 선택하세요: ')
    return menu


def compute_sungjuk(sj):
    sj['tot'] = sj['kor'] + sj['eng'] + sj['math']
    sj['avg'] = sj['tot'] / 3
    sj['grd'] = '수' if sj['avg'] >= 90 else '우' \
    '우' if sj['avg'] >= 80 else '미' \
    '미' if sj['avg'] >= 70 else '양' \
    '양' if sj['avg'] >= 60 else '가'


def save_sungjuk(sj):
    with open ('sungjuks.csv', 'a',encoding='utf-8')as f:
        row = (f"{sj['name']},{sj['kor']},{sj['eng']},{sj['math']},{sj['tot']},"
               f"{sj['avg']:.1f},{sj['grd']}\n")
        f.write(row)


def addSungJuk():
    print('성적데이터 추가')
    sj = read_sungjuk()
    compute_sungjuk(sj)
    save_sungjuk(sj)    # 성적데이터를 파일에 저장