from pppp1144.dbfactory import Session
from pppp1144.orm.zipcode import Zipcode



class ZipcodeDAO:
    @staticmethod
    def select_zipcode():
        with Session()as sess:
            result = sess.query(Zipcode).offset(0).limit(20).all()
        return result



    @staticmethod
    def findbydong_zipcode(dong:str):
        with Session()as sess:
            result = sess.query(Zipcode).where(Zipcode.dong.like(f'{dong}%')).all()
        return result
