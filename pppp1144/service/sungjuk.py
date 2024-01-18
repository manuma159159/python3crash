from pppp1144.orm.sungjuk import Sungjuk
from pppp1144.SungJukService import SungJukService



class SungjukService1():
    @staticmethod
    def convert_sungjuk(sj):
        data = sj.model_dump()
        sj = Sungjuk(**data)

        SungJukService.compute_sungjuk(sj)
        data = {'name': sj.name, 'kor': sj.kor, 'eng': sj.eng, 'math': sj.math,
                'tot': sj.tot, 'avg': sj.tot, 'grd': sj.grd}

        return data



    @staticmethod
    def compute_sungjuk(sj):
        sj.tot = sj.kor + sj.eng + sj.math
        sj.avg = sj.tot / 3
        sj.grd = '가'
        if (sj.avg >= 90):           grd = '수'
        elif (sj.avg >= 80):         grd = '우'
        elif (sj.avg >= 70):         grd = '미'
        elif (sj.avg >= 60):         grd = '양'