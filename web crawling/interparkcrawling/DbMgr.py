# 디비 처리, 연결, 해제, 검색어 가져오기, 데이터 삽입
import pymysql as my
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class DBHelper:

    conn = None


    def __init__(self):
        self.db_init()

    def db_init(self):
        self.conn = my.connect(
            host='localhost',
            user='root',
            password='passwd',
            db='pythonDB',
            charset='utf8',
            cursorclass=my.cursors.DictCursor
        )
    def db_free(self):
        if self.conn:
            self.conn.close()

    # 검색 키워드 가져오기
    def db_selectkeyword(self):
        #커서 오픈
        rows = None
        with self.conn.cursor() as cursor:

            sql = 'select * from tbl_keyword;'
            cursor.execute(sql)
            rows = cursor.fetchall()
        return rows

    def db_insertcrawlingdata(self,title,price,area,contents,keyword):

        with self.conn.cursor() as cursor:

            sql = '''
            insert into `tbl_crawling`
            (title,price,area,contents,keyword)
            values(%s,%s,%s,%s,%s)
            '''
            cursor.execute(sql,(title,price,area,contents,keyword))
        self.conn.commit()

# 단독으로 수행시에만 작
if __name__ == '__main__':
    db = DBHelper()
    print(db.db_selectkeyword())
    print(db.db_insertcrawlingdata('1','2','3','4','5'))
    db.db_free()
