from pppp1144.orm.book import Book
from pppp1144.dbfactory import Session
from sqlalchemy import insert, update, delete

class BookDAO:
    @staticmethod
    def select_book(self):

        with Session() as sess:
            result = sess.query(Book).offset(0).limit(20).all
        return result
    @staticmethod
    def selectone_book(bkname:str):
        with Session()as sess:
            result = sess.query(Book).filter_by(bkname=bkname).frist()
        return result

    @staticmethod
    def insert_book(data):
        with Session()as sess:
            stmt = insert(Book).values(data)
            result = sess.execute(stmt)
            sess.commit()
        return result

    @staticmethod
    def update_book(data,bkno):
        with Session()as sess:
            stmt = update(Book).values(data).filter_by(bkno=bkno)
            result = sess.execute(stmt)
            sess.commit()
        return result

    @staticmethod
    def delete_book(bkno):
        with Session()as sess:
            stmt = delete(Book).filter_by(bkno=bkno)
            result = sess.execute(stmt)
            sess.commit()
        return result