# 소프트웨어의 좋은 설계
# 유지보수가 용이해야 함
# 높은 응집도와 낮은 결합도를 가지도록 요소(모듈)를 적절히 배치하는 것
# - 소프트웨어 설계 품질을 판단하는 기준
# 모듈: 크기와 상관없이 클래스나 패키지,
# 라이브러리와 같이 프로그램을 구성하는 임의의 요소를 의미

# 소프트웨어 레이어링은 소프트웨어를 계층으로 구성하는 디자인 패턴
# 각 계층은 특정 책임을 가지며, 다른 계층과는 독립적으로 개발 및 유지 관리할 수 있음

# 구조의 명확성: 소프트웨어의 구조와 각 계층의 책임을 명확하게 정의함으로써,
# 소프트웨어의 이해와 유지 관리 용이
# 확장성: 새로운 기능 추가시, 기존 레이어를 변경하지 않고, 새로운 레이어 추가
# 유지 보수성: 각 계층은 독립적으로 개발 및 유지 관리할 수 있으므로,
# 소프트웨어의 유지 보수 용이

# 3-tier 아키텍처
# 응용프로그램을 3개의 논리적 및 물리적 컴퓨팅 계층으로 구성하는 소프트웨어 아키텍처
# '프리젠테이션 계층', 데이터를 처리하는 '애플리케이션 계층',
# 그리고 애플리케이션과 연관된 데이터를 저장 및 관리하는 '데이터 계층'으로 구성
# 보다 신속한 개발, 확장성 개선, 안정성 향상, 보안성 강화

# 그냥 import 하면 잡히지가 않음. 파일이 다르면 꼭 from 써야함,
# from pppp1144.SungJuk import Sungjuk
#
#
# # class Sungjuk:
# #
# #     def __init__(self,name,kor,eng,math):
# #         self.name = name
# #         self.kor = kor
# #         self.eng = eng
# #         self.math = math
# #         self.tot = 0
# #         self.avg = 0.0
# #         self.grd = '가'
# #
# #     def __str__(self):
# #         result = f'{self.name}, {self.kor}, {self.eng}, {self.math}'
# #         return result
# # 성적처리에 필요한 기능으로 구성된 클래스 정의
# class SungJukService:
#
#     def read_sungjuk(self):
#         name = input('이름은 ?')
#         kor = int(input('국어는 ?'))
#         eng = int(input('영어는 ?'))
#         math = int(input('수학은 ?'))
#
#         #return name,kor,eng,math 비교를 하기 위해 가져왓음. 41.opp.py
#         #return[name,kor,eng,math]
#         #return['name':name,'kor':kor,'eng':eng,'math':math] 이렇게 다양한 방식이 있음
#         #위에는 딕셔너리 형태로 보내보린 것.
#         return Sungjuk(name,kor,eng,math) # 위에는 맥주 6캔 사는거고 이거는 6개 포장된거 사는 느낌. 이게 더 편함
#     def compute_sungjuk(self, sj):
#         sj.tot = sj.kor + sj.eng + sj.math
#         sj.avg = sj.tot / 3
#         sj.grd = '가'
#         if (sj.avg >= 90):           grd = '수'
#         elif (sj.avg >= 80):         grd = '우'
#         elif (sj.avg >= 70):         grd = '미'
#         elif (sj.avg >= 60):         grd = '양'




# 성적 서비스 호출1
# sjsrv = SungJukService() # 서비스 클래스에 대한 객체 생성 자료에 대한 데이터는 많아도 이런 실행을 하는거는 하나만 만들어도 됨
# sj = sjsrv.read_sungjuk()
# print(sj)
#
# sjsrv.compute_sungjuk(sj)
# print(sj)


# 성적 서비스 호출 2


from pppp1144.SungJuk import Sungjuk


# class Sungjuk:
#
#     def __init__(self,name,kor,eng,math):
#         self.name = name
#         self.kor = kor
#         self.eng = eng
#         self.math = math
#         self.tot = 0
#         self.avg = 0.0
#         self.grd = '가'
#
#     def __str__(self):
#         result = f'{self.name}, {self.kor}, {self.eng}, {self.math}'
#         return result
# 성적처리에 필요한 기능으로 구성된 클래스 정의
class SungJukService:
    @staticmethod # 정적 메서드 : 객체선언없이 바로 쓸 수 있는 메서드
    #여기 골뱅이는 데코레이터(@) : 함수에 추가기능을 부여할 때 사용
    # g 호출방법 : 클래스명, 함수명
    # 정적 메서드로 정의된 함수에는 self 지정 x
    def read_sungjuk():
        name = input('이름은 ?')
        kor = int(input('국어는 ?'))
        eng = int(input('영어는 ?'))
        math = int(input('수학은 ?'))

        #return name,kor,eng,math 비교를 하기 위해 가져왓음. 41.opp.py
        #return[name,kor,eng,math]
        #return['name':name,'kor':kor,'eng':eng,'math':math] 이렇게 다양한 방식이 있음
        #위에는 딕셔너리 형태로 보내보린 것.
        return Sungjuk(name,kor,eng,math) # 위에는 맥주 6캔 사는거고 이거는 6개 포장된거 사는 느낌. 이게 더 편함

    @staticmethod
    def compute_sungjuk(sj):
        sj.tot = sj.kor + sj.eng + sj.math
        sj.avg = sj.tot / 3
        sj.grd = '가'
        if (sj.avg >= 90):           grd = '수'
        elif (sj.avg >= 80):         grd = '우'
        elif (sj.avg >= 70):         grd = '미'
        elif (sj.avg >= 60):         grd = '양'


#성적 서비스 호출2
sj2 = SungJukService.read_sungjuk()
SungJukService.compute_sungjuk(sj2)
print(sj2)
