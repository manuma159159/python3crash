# 마리아 디비로 데이터다루기 1 - select
# pymysql 모듈을 먼저 설치해야함 - pip install pymysql (이건 수동 설치. 자동 설치는 사진 첨부)

import pymysql

# 데이터베이스 서버 접속정보 동의
url = ''
userid = ''
passwd = ''
dbname = 'bigdata'

# 디비서버에 연결

conn = pymysql.connect(host=url, user=userid, password=passwd, database=dbname, charset='utf8')

cursor = conn.cursor()

sql = ' select * from member '
cursor.execute(sql)


rows = cursor.fetchall()

cursor.close()
conn.close()

result = ''
for row in rows:
    result += f'{row[0]} {row[1]} {row[2]} {row[3]}\n'


print(result)