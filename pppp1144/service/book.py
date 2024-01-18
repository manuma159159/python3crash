from pppp1144.model.book import BookRes
from pppp1144.orm.book import Book

class BookService():
    @staticmethod
    def compute_bookprice(bk):
        bk.price = int(bk.retail) * (1-(int(bk.pctoff)/100))
        bk.mileage = int(bk.retail) * (int(bk.pctoff)/100)


    @staticmethod
    def convert_book(bk):
        data = bk.model_dump()
        bk = Book(**data)
        BookService.compute_bookprice(bk)
        data = {'bkname':bk.bkname,'author':bk.author, 'publisher':bk.publisher,
                'pubdate':bk.pubdate, 'retail':bk.retail, 'pctoff':bk.pctoff,
                'price':bk.price, 'mileage': bk.mileage}

        return data