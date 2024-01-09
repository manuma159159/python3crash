import pppp1144.dbinfo as dbinfo

class SungJukDAO:
    @staticmethod
    def insert_sungjuk(sj):
        '''
        성적데이터를 sungjuk테이블에 저장
        :param sj: 성적데이터
        :return: 저장된 성적데이터 건수
        '''
        sql = ' insert into sungjuks(name, kor, eng, math, tot, avg, grd) ' \
              ' values (:name,:kor,:eng,:math,:tot,:avg,:grd) ' # 이렇게 걸어놔야함
        #' values (:1,:2,:3,:4,:5,:6,:7) ' 이것도 됨 이걸 더 많이 씀
        #' values (?,?,?,?,?,?,?) ' 이건 오라클에서 안됌. 마리아디비에서만

        cursor, conn = dbinfo.openConn() # 일종의 캡슐화

        params = [sj.name,sj.kor,sj.eng,sj.math,sj.tot,sj.avg,sj.grd]
        cursor.execute(sql,params)
        conn.commit()
        rowcount = cursor.rowcount
        return rowcount

        dbinfo.closeConn(cursor,conn)

    @staticmethod
    def select_sungjuk():
        '''
        성적테이블에서 모든 성적 데이터 출력 (번호/이름/국어/영어/수학/등록일)
        :return: 조회된 성적데이터 객체
        '''
        sql = ' select sjno,name,kor,eng,math,grd from sungjuks' \
              ' order by sjno desc '

        cursor,conn = dbinfo.openConn()
        cursor.execute(sql)
        rows = cursor.fetchall()

        dbinfo.closeConn(cursor,conn)
        return rows

    @staticmethod
    def selectone_sungjuk(sjno):
        '''
        sungjuk테이블에서 특정 학생의 성적데이터 가져오기
        :param sjno: 상세조회할 학생번호
        :return: 조회된 학생 성적 데이터
        '''

        sql = ' select * from sungjuks where sjno = :1 '

        cursor,conn = dbinfo.openConn()
        cursor.execute(sql,[sjno])

        row = cursor.fetchone()

        dbinfo.closeConn(cursor,conn)
        return row

    @staticmethod
    def update_sungjuk(sj,sjno):

        sql = ' update sungjuks set name = :1, kor = :2, eng = :3, math = :4, ' \
              ' tot = :5, avg = :6, grd = :7, regdate=sysdate where sjno = :8 '

        cursor,conn = dbinfo.openConn()

        params = [sj.name,sj.kor,sj.eng,sj.math,sj.tot,sj.avg,sj.grd,sjno]
        cursor.execute(sql,params)
        conn.commit()

        rowcnt = cursor.rowcount

        dbinfo.closeConn(cursor,conn)
        return rowcnt

    @staticmethod
    def delete_sungjuk(sjno):
        '''
        지정한 학생 데이터를 sungjuk테이블에서 삭제
        :param sjno: 삭제할 학생 번호
        :return: 삭제된 성적 데이터 건수
        '''
        sql = ' delete from sungjuks where sjno = :1 '
        cursor,conn = dbinfo.openConn()

        cursor.execute(sql,[sjno])
        conn.commit()

        rowcnt = cursor.rowcount
        dbinfo.closeConn(cursor,conn)

        return rowcnt