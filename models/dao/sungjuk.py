from pppp1144.dbfactory import Session
from pppp1144.model.sungjuk import SungjukRes
from pppp1144.orm.sungjuk import Sungjuk
from pppp1144.SungJukService import SungJukService
from sqlalchemy import insert, update, delete

class SungjukDAO:
    @staticmethod
    def select_sungjuk():
        with Session()as sess:result = sess.query(Sungjuk).offset(0).limit(10).all()
        return result

    @staticmethod
    def selectone_sungjuk(sjno):
        with Session()as sess:
            result = sess.query(Sungjuk).filter_by(sjno=sjno).first()
        return result

    @staticmethod
    def insert_sungjuk(data):
        with Session() as sess:
            stmt = insert(Sungjuk).values(data)
            result = sess.execute(stmt)
            sess.commit()
        return result

    @staticmethod
    def update_sungjuk(data,sjno):
        with Session() as sess:
            stmt = update(Sungjuk).values(data).filter_by(sjno=sjno)
            result = sess.execute(stmt)
            sess.commit()
        return result

    @staticmethod
    def delete_sungjuk(sjno):
        with Session() as sess:
            stmt = delete(Sungjuk).filter_by(sjno=sjno)
            result = sess.execute(stmt)
            sess.commit()
        return result