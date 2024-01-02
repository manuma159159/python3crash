# 성적 데이터를 저장할 변수 선언
# [ {'name': 혜교, 'kor': 77, 'eng': 33, 'mat': 86},
#   {'name': 지현, 'kor': 66, 'eng': 44, 'mat': 54},
#   {'name': 수지, 'kor': 55, 'eng': 55, 'mat': 43} ]
sjs = []


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
    for sj in sjs:
        print(f"이름: {sj['name']:s}, 국어: {sj['kor']},"
              f" 영어: {sj['eng']}, 수학:{sj['math']}")


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
    global sjs
    with open ('sungjuks.csv', 'a',encoding='utf-8')as f:
        row = (f"{sj['name']},{sj['kor']},{sj['eng']},{sj['math']},{sj['tot']},"
               f"{sj['avg']:.1f},{sj['grd']}\n")
        f.write(row)
    sjs.append(sj) #메모리에 존재하는 sjs 변수에도 방금 추가한 성적데이터


def addSungJuk():
    print('성적데이터 추가')
    sj = read_sungjuk()
    compute_sungjuk(sj)
    save_sungjuk(sj)    # 성적데이터를 파일에 저장

# 프로그램 시작시 성적.dat 파일을 읽어 sjs 변수 초기화
def load_sungjuk():
    global sjs
    with open('sungjuks.csv', encoding='utf-8') as f:
        datas = f.readlines()

    # csv 형태로 저장되어 있는 성적 데이터를
    # dict 형태로 변환해서 메모리에 적재
    dicts = []
    for data in datas:
        # strip : 각종 제어문자를 제거
        item = data.strip().split(',')
        d = {'name': item[0], 'kor': item[1], 'eng': item[2],
             'math': item[3], 'tot':item[4], 'avg':item[5] ,
             'grd':item[6]}
        dicts.append(d)

    sjs = dicts # dict로 변환된 데이터를 sjs 변수에 저장