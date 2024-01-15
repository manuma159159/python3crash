# sqlalchemy
# python용 데이터베이스 ORM 도구
# 2.0.25/1.4.51(추천!) (2024-1-15 기준)
# pip install sqlalchemy
from sqlalchemy import create_engine, Column, String, Integer, Sequence
from sqlalchemy.orm import sessionmaker, declarative_base

# 데이터베이스 연결준비
# database_url = 'sqlite:///bigdata.db'
#database_url = 'mysql+pymysql://admin:bigdata2023@bigdata.ciefa0cprwiy.ap-northeast-2.rds.amazonaws.com:3306/bigdata?charset=utf8mb4' # mariadb
database_url = 'oracle+cx_oracle://bigdata:bigdata@3.35.238.195:1521'

engine = create_engine(database_url,echo=True)

# 데이터베이스 엔진을 이용해서 세션 생성
Session = sessionmaker(bind=engine)
sess = Session()

# ORM 객체 생성을 위한 Base 클래스 선언
Base = declarative_base()
class Zipcode(Base):
    __tablename__='Zipcode'# 매핑할 테이블 지정
    zipcode = Column(String(7)) # zipcode가 일곱글자라 7이 오는거임
    sido = Column(String(7)) #
    gugun = Column(String(50))
    dong = Column(String(50))
    ri = Column(String(50))
    bunji = Column(String(100))
    seq = Column(Integer,Sequence('zipseq'), primary_key=True)

# ORM 객체와 실제 테이블과 연결
Base.metadata.create_all(engine)

# 우편번호 조회 테스트 1
zips = sess.query(Zipcode).offset(0).limit(20).all()
for zip in zips:
    print(f'{zip.zipcode}{zip.sido}{zip.gugun}{zip.dong}')

# 우편번호 조회 테스트 2
zips = sess.query(Zipcode).filter_by(dong='자양1동').all()
for zip in zips:
    print (f'{zip.zipcode}{zip.sido}{zip.gugun}{zip.dong}')

# 우편번호 조회 테스트 2
dong = '신림'
zips = sess.query(Zipcode).where(Zipcode.dong.like(f'{dong}%')).all()
for zip in zips:
    print (f'{zip.zipcode}{zip.sido}{zip.gugun}{zip.dong}')


