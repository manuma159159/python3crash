# 개선된 성적 클래시ㅡ - 생성자를 통해서 변수 초기화
class Sungjuk2:
    # 생성자
    def __init__(self,name,kor,eng,math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.tot = 0
        self.avg = 0.0
        self.grd = '가'


        # __str__ : 멤버변수들의 값을 문자열화해서
        # 객체 정보를 외부에 표현할 때 사용하는 특수한 함수

    def __str__(self):
        result = f'{self.name}, {self.kor}, {self.eng}, {self.math}'
        return result

# 성적 객체 생성 및 초기화
sj = Sungjuk2('iu',99,88,99) # 나는 왜 'iu' 옆에 name: 이게 안되는 것인가

print(sj.name, sj.kor, sj.eng, sj.math)

sj = Sungjuk2(input('이름은?'), int(input('국어는?')),int(input('영어는?')), int(input('수학은?')))
print(sj.name, sj.kor, sj.eng, sj.math)

# Sungjuk 클래스의 __str__ 을 호출해서 객체의 내용을 출력
print(sj)