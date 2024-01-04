import json
import sys
from collections import OrderedDict

sjs = {'response' : {'body': {'totalCount':0, 'items': []}}}
items = []
totalCount = 0
# sungjuks ={'response' : {'body': {'totalCount':999, 'items': []}}}
#sjs = {'sungjuks':[]}   # 이거로 대신하면 더 편함. show 랑 save쪽 'sungjuks'로 바꾸면 됨.

# 프로그램 시작시 sungjuks.json 파일을  읽어 sjs 변수에 초기화
def load_sungjuk():
    global sjs
    global items
    global totalCount
    try:        # 만약 작업중에 오류가 발생하면
        with open('sungjuks.json',encoding='utf-8')as f :
            sjs = json.load(f)
            items = sjs['response']['body']['items']
            totalCount = sjs['response']['body']['totalCount']
    except:
        items = sjs['response']['body']['items']
        totalCount = sjs['response']['body']['totalCount']
        # 프로그램 실행 중단없이 다음 코드 실행
        # pass

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



# def read_sungjuk() :
#     sj = OrderedDict()
#     sj['name'] = (input('이름은?:'))
#     sj['kor'] = int(input('국어는?'))
#     sj['eng'] = int(input('영어는?'))
#     sj['math'] = int(input('수학은?'))
#     return sj

def read_sungjuk() :
    sungjuk = input('이름과 성적을 입력하세요 (예: 홍길동 99 88 99) : ')
    data = sungjuk.split() # 빈칸으로 문자열 분리
    sj = OrderedDict()
    sj['name'] = data[0]
    sj['kor'] = int(data[1])
    sj['eng'] = int(data[2])
    sj['math'] = int(data[3])
    return sj

def compute_sungjuk(sj):
    sj['tot'] = sj['kor'] + sj['eng'] + sj['math']
    sj['avg'] =float(f"{sj['tot'] / 3:.1f}")
    sj['grd'] = '수' if sj['avg'] >= 90 else '우' \
    '우' if sj['avg'] >= 80 else '미' \
    '미' if sj['avg'] >= 70 else '양' \
    '양' if sj['avg'] >= 60 else '가'

# def save_sungjuk(sj):
#     # 메모리 내에 생성된 json 객체에 방금 생성한 성적데이터 저장
#     sjs['response']['body']['items'].append(sj)
#     sjs['response']['body']['totalCount'] += 1 # 얘는 sjs = sungjuks 면 필요없음.
#     # 메모리 내에 생성된 json 객체를 파일에 저장 ( w를 써야 덮어쓰기 가능)
#     with open ('sungjuks.json', 'w', encoding='utf-8')as f:
#         json.dump(sjs, f, ensure_ascii=False)

def save_sungjuk(sj):
    # 메모리 내에 생성된 json 객체에 방금 생성한 성적데이터 저장
    items.append(sj)
    sjs['response']['body']['totalCount'] += 1 # 얘는 sjs = sungjuks 면 필요없음.
    # sjs['response']['body']['totalCount'] 대신 totalCount를 쓰면 기록이 안됨. 그래서 그냥 씀.
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
    for sj in items: #sjs['response']['body']['items']:
        print(f"이름: {sj['name']:s}, 국어: {sj['kor']},"
              f" 영어: {sj['eng']}, 수학:{sj['math']}")


# def showone_sungonejuk():
#     name = input('상세 조회할 학생이름은?')
#
#     info = '찾는 데이터가 없어요!'
#     for sj in sjs['response']['body']['items']:
#         if sj['name'] == name:
#             info = (f"{sj['name']} {sj['kor']} {sj['eng']} {sj['math']} {sj['tot']}"
#                     f"{sj['avg']} {sj['grd']}")
#             break # 찾고나면 검색 작업 중단
#     print(info)

def showone_sungonejuk():
    name = input('상세 조회할 학생이름은?')

    info = '찾는 데이터가 없어요!'
    for sj in items:
        if sj['name'] == name:
            info = (f"{sj['name']} {sj['kor']} {sj['eng']} {sj['math']} {sj['tot']} "
                    f"{sj['avg']} {sj['grd']}")
            break  # 찾고나면 검색 작업 중단
    print(info)

def read_again(data,name):
    kor = int(input(f'새로운 국어점수는? ({data["kor"]})'))
    eng = int(input(f'새로운 영어점수는? ({data["eng"]})'))
    math = int(input(f'새로운 수학점수는? ({data["math"]}) :'))

    data = OrderedDict()
    data['name'] = name
    data['kor'] = kor
    data['eng'] = eng
    data['math'] = math
    
    return data


def flush_sungjuk():
    with open('sungjuks.json', 'w', encoding='utf-8') as f:
        json.dump(sjs, f, ensure_ascii=False)


def modify_sungjuk():
    name = input('수정할 학생의 이름은')
    # 수정할 학생 데이터를 이름으로 찾음
    data = None
    idx = None
    for i,sj in enumerate(items):
        if sj['name'] == name:
            data = sj
            idx = i
            
    # 수정할 학생 데이터를 찾았다면 새로운 값을 입력받고 다시 성적처리함
    if data:
        data = read_again(data,name)
        compute_sungjuk(data)
        # 리스트에 기존 데이터를 버리고 새로운 데이터로 재설정
        items [idx] = data
        
        # 변경 사항을 json 파일에 반영
        flush_sungjuk()
    else:
        print('찾으시는 데이터가 없습니다.')
def remove_sungjuk():
    return None


def exit_sungjuk():
    print('프로그램 종료')
    sys.exit(0)


