class Student:
    def __init__(self,stno,name,addr,birth,dept,prof):
        self.stno = stno
        self.name = name
        self.addr = addr
        self.birth = birth
        self.dept = dept
        self.prof = prof


    def __str__(self):
        info = (f'{self.stno}{self.name}{self.addr}{self.birth}{self.dept}'
                f'{self.prof}')
        return info

class Professor:
    def __init__(self,name,major,tech,dept,):
        self.name = name
        self.major = major
        self.tech = tech
        self.dept = dept

    def __str__(self):
        info = (f'{self.name},{self.major}'
                f'{self.tech},{self.dept}')
        return info


class Subject:
    def __init__(self,sjno,sjname,sjdesc,sjsect,sjprof):
        self.sjno = sjno
        self.sjname = sjname
        self.sjdesc = sjdesc
        self.sjsect = sjsect
        self.sjprof = sjprof

    def __str__(self):
        info = (f'{self.sjno},{self.sjname},{self.sjdesc},'
                f'{self.sjsect},{self.sjprof}')
        return info


class Department:
    def __init__(self,dname,phone,dpos,chief):
        self.dname = dname
        self.phone = phone
        self.dpos = dpos
        self.chief = chief

    def __str__(self):
        info = f'{self.dname},{self.phone},{self.dpos},{self.chief}'
        return info





taehee = Student(201350050,'김태희','경기도 고양시',
             '1985.3.22','컴퓨터',504)
print(taehee)
taehee.addr = '서울시 관악구' # 이렇게 하면 주소가 바뀜.


lee = Professor('이순신','프로그래밍',
                '[자바,파이썬]','컴퓨터')
print(lee)


programming = Subject('0205','프로그래밍',
                      '자바프로그래밍','컴퓨터',301)
print(programming)


computer = Department('컴퓨터공학','123-4567-8901',
                      'E동 2층',504)
print(computer)