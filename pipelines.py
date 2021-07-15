import sqlite3

class BooksPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()
    
    def create_connection(self):
        self.conn = sqlite3.connect("books.db")
        self.curr = self.conn.cursor()
        
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS books_tb""")
        self.curr.execute(""" create table books_tb(
                    title text,
                    price text
                    )""")
    
    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into books_tb values(?,?)""",
                          (
                             str(item['title']),
                             str(item['price']),
                             #str(item['image_url']),
                             #str(item['book_url'])
                              ))
        self.conn.commit()
        #we wont close the connection as we need to add multiple quotes
