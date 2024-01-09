from pppp1144.SungJuk import Sungjuk



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
