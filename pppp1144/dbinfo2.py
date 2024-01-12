import oracledb
import pymysql
import os


# 시스템 환경변수 등록
# linux : export 키 = 값
# window : set 키+값

url = os.getenv('URL1')
userid = os.getenv('USR1')
passwd = os.getenv('PWD1')
dbname = os.getenv('DBN1')

def openConn():
    '''
    데이터베이스 커서와 커넥션 객체 생성
    :return: 커서, 커넥션 객체 반환
    '''
    conn = pymysql.connect(host=url, user=userid, password=passwd, database=dbname, charset='utf8')
    cursor = conn.cursor()
    return cursor,conn

def closeConn(cursor,conn):
    '''

    데이터 베이스 커서와 연결 종료
    :param cursor: 접속중인 커서 객체
    :param conn: 접속중인 커넥션 객체
    :return: 없음
    '''
    cursor.close
    conn.close