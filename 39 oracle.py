# 오라클 디비로 데이터다루기 1 - select
# cx_Oracle 모듈을 먼저 설치해야함 - pip install cx_Oracle
# (터미널로 오라클 깔고 client 설치하는거임)

# 1.Oracle instant Client 버전에 따라 비쥬얼스투디오 재배포 패키지 설치
# 2.Oracle instant Client 다운로드하고 c:\Java에 압축해제
# 3.Oracle instant client를 시스템의 path 환경변수에 등록
# 4.그리고 intellij 리부트

# For Instant Client 21 install VS 2019 or later. ( 이거 깔려면 비쥬얼 코드 설치되어야 함 )
# For Instant Client 19 install VS 2017.
# https://www.oracle.com/kr/database/technologies/instant-client/winx64-64-downloads.html

# INTELLIJ 에서 csv 파일 가져올 때
# 텍스트 컬럼은 자동으로 CLOB 타입으로 설정되기 때문에
# 이걸 테이블로 가져올 때 설정으로 바꿔서 VARCHAR로 바꿔야함.

# 2024-01-08 기준
# cx_Oracle 모듈이 oracledb로 업그레이드 됨
# oracle instant client 없이 데이터베이스 관련 작업 가능!
# pip install oracledb

import cx_Oracle
import oracledb

host = ''
userid = ''
passwd =  ''
sid = 'FREE'

# 디비 서버에 연결
# dsn_tns = cx_Oracle.makedsn(host, 1521, sid)
# conn = cx_Oracle.connect(userid, passwd, dsn_tns)
dsn_tns = oracledb.makedsn(host, 1521, sid)
conn = oracledb.connect(user = userid, password = passwd, dsn=dsn_tns)
cursor = conn.cursor()

sql = ' select first_name, last_name from employees '
cursor.execute(sql)

for fname, lname in cursor:
    print(fname,lname)

cursor.close()
conn.close()

# 국가별 메달 획득 수 조회
host = ''
userid = ''
passwd =  ''
sid = 'FREE'

dsn_tns = cx_Oracle.makedsn(host, 1521, sid)
conn = cx_Oracle.connect(userid, passwd, dsn_tns)

cursor = conn.cursor()

sql =(' select Country, Medal, count(Country) as cnt from summermedals2  group by Country, Medal order by cnt desc ')
cursor.execute(sql)

for country, medal,cnt in cursor:
    print(country,medal, cnt)

cursor.close()
conn.close()


# 승선위치별(embarked) 성별(sex) 생존자수(ALIVE) 조회

# dsn_tns = cx_Oracle.makedsn(host, 1521, sid)
# conn = cx_Oracle.connect(userid, passwd, dsn_tns)
dsn_tns = oracledb.makedsn(host, 1521, sid)
conn = oracledb.connect(user=userid, password=passwd, dsn=dsn_tns)

cursor = conn.cursor()

sql =("select EMBARK_TOWN, SEX, ALIVE, count(alive) alives from titanic3 "
      "WHERE ALIVE = 'no'"
      "group by SEX, ALIVE, EMBARK_TOWN "
      "order by EMBARK_TOWN, SEX ")
cursor.execute(sql)

for EMBARK_TOWN, SEX, ALIVE, alives in cursor:
    print(EMBARK_TOWN, SEX, ALIVE, alives)

cursor.close()
conn.close()


# 승선위치별(embarked) 사람별(who) 생존자수(alive) 조회

dsn_tns = cx_Oracle.makedsn(host, 1521, sid)
conn = cx_Oracle.connect(userid, passwd, dsn_tns)

cursor = conn.cursor()

sql =(" select EMBARK_TOWN, WHO, ALIVE, count(alive) alives from titanic3 "\
      " WHERE ALIVE = 'no' "\
      " group by WHO, ALIVE, EMBARK_TOWN")
cursor.execute(sql)

for EMBARK_TOWN, WHO, ALIVE, alives in cursor:
    print(EMBARK_TOWN, WHO, ALIVE, alives)

cursor.close()
conn.close()

