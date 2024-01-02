# 함수 정의
def read_sungjuk() :
    sj = {}
    sj['name'] = (input('이름은?:'))
    sj['kor'] = int(input('국어는?'))
    sj['eng'] = int(input('영어는?'))
    sj['math'] = int(input('수학은?'))
    return sj


def show_sungjuk(sungjuks): # 성적데이터 출력
    for sjs in sungjuks['response']['body']['items']:
        print(f"이름: {sjs['name']:s}, 국어: {sjs['kor']}, 영어: {sjs['eng']}, 수학:{sjs['math']}")


def show_menu():
    main_menu = '''
    성적처리 프로그램 v5b
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


def compute_sungjuk(sj):
    sj['tot'] = sj['kor'] + sj['eng'] + sj['math']
    sj['avg'] = sj['tot'] / 3
    sj['grd'] = '수' if sj['avg'] >= 90 else '우' \
    '우' if sj['avg'] >= 80 else '미' \
    '미' if sj['avg'] >= 70 else '양' \
    '양' if sj['avg'] >= 60 else '가'