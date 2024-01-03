import json
import sys
from collections import OrderedDict

sjs={'response' : {'body': {'totalCount':0, 'items': []}}}
# sungjuks ={'response' : {'body': {'totalCount':999, 'items': []}}}
#sjs = {'sungjuks':[]}   # 이거로 대신하면 더 편함. show 랑 save쪽 'sungjuks'로 바꾸면 됨.

# 프로그램 시작시 sungjuks.json 파일을  읽어 sjs 변수에 초기화
def load_sungjuk():
    global sjs
    try:        # 만약 작업중에 오류가 발생하면
        with open('sungjuks.json',encoding='utf-8')as f :
            sjs = json.load(f)
    except:
        pass        # 프로그램 실행 중단없이 다음 코드 실행
def show_menu():
    main_menu = '''
    성적처리 프로그램 v6c
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
    sj = OrderedDict()
    sj['name'] = (input('이름은?:'))
    sj['kor'] = int(input('국어는?'))
    sj['eng'] = int(input('영어는?'))
    sj['math'] = int(input('수학은?'))
    return sj

def compute_sungjuk(sj):
    sj['tot'] = sj['kor'] + sj['eng'] + sj['math']
    sj['avg'] =float(f"{sj['tot'] / 3:.1f}")
    sj['grd'] = '수' if sj['avg'] >= 90 else '우' \
    '우' if sj['avg'] >= 80 else '미' \
    '미' if sj['avg'] >= 70 else '양' \
    '양' if sj['avg'] >= 60 else '가'

def save_sungjuk(sj):
    # 메모리 내에 생성된 json 객체에 방금 생성한 성적데이터 저장
    sjs['response']['body']['items'].append(sj)
    sjs['response']['body']['totalCount'] += 1 # 얘는 sjs = sungjuks 면 필요없음.
    # 메모리 내에 생성된 json 객체를 파일에 저장 ( w를 써야 덮어쓰기 가능)
    with open ('sungjuks.json', 'w', encoding='utf-8')as f:
        json.dump(sjs, f, ensure_ascii=False)



def addSungJuk():
    print('성적데이터 추가')
    sj = read_sungjuk()
    compute_sungjuk(sj)
    save_sungjuk(sj)


def show_sungjuk():
    print('성적데이터 조회')
    for sj in sjs['response']['body']['items']:
        print(f"이름: {sj['name']:s}, 국어: {sj['kor']},"
              f" 영어: {sj['eng']}, 수학:{sj['math']}")


def showone_sungonejuk():
    return None


def modify_sungjuk():
    return None


def remove_sungjuk():
    return None


def exit_sungjuk():
    print('프로그램 종료')
    sys.exit(0)

