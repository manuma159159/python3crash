# bkname, author, publisher, pubdate, retail, price, pctoff, mileage

class Book:
    def __init__(self, bkname, author, publisher, pubdate, retail, pctoff):
        self.bkno = -1
        self.bkname = bkname
        self.author = author
        self.publisher = publisher
        self.pubdate = pubdate
        self.retail = retail
        self.price = 0
        self.pctoff = pctoff
        self.mileage = 0
        self.regdate = -1

# -1 하는 이유는 완전히 정해지지 않았기 때문에. 보통 0이상을 True 음의 정수를 False라
# 표현하기도 해서 -1 한것. 큰 의미는 x

    # bkname, author, publisher, pubdate, retail, price, pctoff, mileage
    def __str__(self):
        self.price = self.retail * (1-(self.pctoff/100))
        self.mileage = self.retail * (self.pctoff/100)

        result = (f'{self.bkno},{self.bkname},{self.author},{self.publisher},{self.pubdate}\n'
                  f'{self.retail},{self. price},{self.pctoff},{self.mileage},{self.regdate}')

        return result