import pppp1144.dbinfo2 as dbinfo

insertsql = ' insert into book (bkname, author, publisher, pubdate, retail, price, pctoff, mileage) '\
            ' values (%s,%s,%s,%s,%s,%s,%s,%s)'
selectsql = 'select bkname, author, publisher, pubdate, retail, price from book'
selectonesql ='select * from book where bkname = %s'
updatesql =('update book set bkname= %s, author=%s, publisher=%s, pubdate=%s, '
            'retail= %s, price=%s, pctoff= %s, mileage=%s, regdate=current_timestamp where bkno = %s')
deletesql = 'delete from book where bkno=%s'
class BookDAO:
    @staticmethod
    def insert_book(bk):


        cursor,conn = dbinfo.openConn()

        params = [bk.bkname,bk.author,bk.publisher,bk.pubdate,
                  int(bk.retail),int(bk.price),int(bk.pctoff),bk.mileage]
        cursor.execute(insertsql,params)
        conn.commit()
        rowcnt = cursor.rowcount

        dbinfo.closeConn(cursor,conn)
        return rowcnt

    @staticmethod
    def select_book():
        cursor,conn = dbinfo.openConn()

        cursor.execute(selectsql)
        rows = cursor.fetchall()

        dbinfo.closeConn(cursor,conn)
        return rows


    @staticmethod
    def selectone_book(bkname):
        cursor,conn = dbinfo.openConn()

        cursor.execute(selectonesql,[bkname])
        row = cursor.fetchone()

        dbinfo.closeConn(cursor,conn)
        return row
        if row :
            print(f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} '
                  f'{row[5]:,} {row[6]:,} {row[7]:%} {row[8]:,} {row[9]}')
        else:
            print('데이터가 없습니다.')


    @staticmethod
    def update_book(bk):
        cursor,conn = dbinfo.openConn()

        params =[bk.bkname, bk.author, bk.publisher, bk.pubdate, int(bk.retail),
                 int(bk.price), int(bk.pctoff), int(bk.mileage), bk.bkno]
        cursor.execute(updatesql,params)
        conn.commit()
        rowcnt = cursor.rowcount

        dbinfo.closeConn(cursor,conn)
        return rowcnt


    @staticmethod
    def delete_book(bkno):
        cursor,conn = dbinfo.openConn()

        cursor.execute(deletesql,[bkno])
        conn.commit()
        rowcnt = cursor.rowcount

        dbinfo.closeConn(cursor,conn)
        return rowcnt
