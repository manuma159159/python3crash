import sys
import json
from collections import OrderedDict
emps = {'response': {'body': {'totalCount':0, 'items': []}}}
items = []
totalCount = 0

def load_employees():
    print('프로그램을 초기화합니다!')
    global emps
    global items
    global totalCount
    try:
        with open('employees.json',encoding='utf-8')as f:
            emps = json.load(f)
            items = emps['response']['body']['items']
            totalCount = emps['response']['body']['totalCount']

    except:
        items = emps['response']['body']['items']


    print('프로그램이 성공적으로 초기화되었습니다.')
def showmenu():
    main_menu = '''
    사원관리 프로그램 
    ------------------
    1. 사원 정보 추가
    2. 사원 정보 조회
    3. 사원 정보 상세조회
    4. 사원 정보 수정
    5. 사원 정보 삭제
    0. 프로그램 종료
    ------------------
    '''
    print(main_menu, end='')
    menu = input('=> 메뉴를 선택하세요: ')
    return menu


def input_employee():
    emp = OrderedDict()
    emp['empno'] = input('사원번호는?')
    emp['fname'] = input('이름은?')
    emp['lname'] = input('성은?')
    emp['email'] = input('이메일은?')
    emp['hdate'] = input('입사일은?')
    emp['jobid'] = input('직책은?')
    emp['sal'] = input('급여는?')
    emp['deptid'] = input('부서번호는?')
    return emp

def save_employee(emp):
#    emps['response']['body']['items'].append(emp)
    items.append(emp)
    emps['response']['body']['totalCount'] += 1
    with open('employees.json', 'w', encoding='utf-8') as f:
        json.dump(emps, f,ensure_ascii=False)


def add_employee():
    global emp
    print('사원 정보를 등록합니다..')
    emp = input_employee()
    save_employee(emp)

def read_employee():
    print('모든 사원 정보를 조회합니다..')
    result = ''
    for emp in items:
        result += (f"{emp['empno']}\t{emp['fname']}"
                   f"\t{emp['jobid']}\t{emp['deptid']}\n")
    print(result)


def readone_employee():
    empno = input('상세 조회할 사원 번호를 입력하시오')
    info = '찾는 데이터가 없습니다'
    for emp in items:
        if emp['empno'] == empno:
            info = (f"{emp['empno']} {emp['fname']} {emp['lname']} {emp['email']} "
                    f"{emp['hdate']} {emp['jobid']} {emp['sal']} {emp['deptid']}")
            break
    print(info)


def read_again(data,empno):
    emp = OrderedDict()

    emp['fname'] = input(f'새로운 이름은? ({data["fname"]})')
    emp['lname'] = input(f'새로운 성은? ({data["lname"]})')
    emp['email'] = input(f'새로운 이메일은? ({data["email"]})')
    emp['hdate'] = input(f'새로운 입사일은? ({data["hdate"]})')
    emp['jobid'] = input(f'새로운 직책은? ({data["jobid"]})')
    emp['sal'] = input(f'새로운 급여는? ({data["sal"]})')
    emp['deptid'] = input(f'새로운 부서번호? ({data["deptid"]})')

    return emp


def flush_employee():
    with open('employees.json', 'w', encoding='utf-8') as f:
        json.dump(emps, f,ensure_ascii=False)


def modify_employee():
    empno = input('상세 조회할 사원 번호를 입력하시오')
    data = None
    idx = None
    for i,emp in enumerate(items):
        if emp['empno'] == empno:
            data = emp
            idx = i

    if data :
            data = read_again(data,empno)
            items [idx] = data

            flush_employee()
    else:
        print('찾으시는 데이터가 없습니다')



def remove_employee():
    empno = input('삭제할 사원번호는?')

    data = None
    for emp in items:
        if emp['empno'] == empno:
            data = emp
            break

    if data :
        confirm = input('정말로 삭제하시겠습니까?')
        if confirm == 'yes':
            items.remove(data)
            emps['response']['body']['totalCount'] -= 1
            print(f'{empno}의 데이터가 삭제되었습니다.')
            flush_employee()
        else:
            print('삭제가 취소되었습니다.')


def exit_program():
    print('프로그램을 종료합니다!')
    sys.exit(0)