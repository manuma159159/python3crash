
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#sqlalchemy 설정
musr = 'admin'
mpwd =  'bigdata2023'
murl = 'bigdata.ciefa0cprwiy.ap-northeast-2.rds.amazonaws.com'
mdbn = 'bigdata'

ousr ='bigdata'
opwd ='bigdata'
ourl = '3.35.238.195:1521'

# 이렇게 하면 보안 기능이 됨.
#database_url = 'sqlite:///bigdata.db'
database_url = f'mysql+pymysql://{musr}:{mpwd}@{murl}:3306/{mdbn}?charset=utf8mb4'
# database_url = f'oracle+cx_oracle://{ousr}:{opwd}@{ourl}'
engine = create_engine(database_url,echo=True)
Session = sessionmaker(autocommit=False, autoflush=False,bind=engine)