import pymysql
import datetime
from dateutil.relativedelta import relativedelta
from utils.config import Config


class SQL_OPR(object):
    def __init__(self):
        sql_cfg = Config()
        sql_info = sql_cfg.get('sql-info')
        sql_infos = [i for i in sql_info]
        self.uname = sql_infos[0].get('uname')
        self.pwd = sql_infos[0].get('pwd')
        self.host = sql_infos[0].get('host')
        self.port = sql_infos[0].get('port')
        self.db_name = sql_infos[0].get('db')

    def connect_sql(self):
        self.db = pymysql.connect(host=self.host, port=self.port, user=self.uname, password=self.pwd, db=self.db_name)
        return self.db

    def select_sql(self,db, sql):
        cur = db.cursor()
        try:
            cur.execute(sql)
            results = cur.fetchall()
            return results
        except Exception as e:
            raise e
        finally:
            db.close()

    def update_sql(self, db, sql):
        cur = db.cursor()
        try:
            cur.execute(sql)
            db.commit()
        except Exception as e:
            raise e
        finally:
            db.close()


if __name__ == "__main__":
    pre_month = datetime.date.today() - relativedelta(months=+1,day=+1)
    print(pre_month)
    # conn = pymysql.connect(user='root', password='111111',db="httprunner",port=3306)
    # print(conn)
    # sql = "SELECT * FROM djcelery_periodictask WHERE id=1"
    # cur = conn.cursor()
    # cur.execute(sql)
    # re = cur.fetchall()
    # print(re[0])
    test = SQL_OPR()
    db = test.connect_sql()
    sql = "SELECT CompletedTime FROM CM_UserTest WHERE UserID='C11571539' AND ServiceID='P90' AND TestRound=1;"
    update_sql = "UPDATE CM_UserTest SET CompletedTime='{} 16:35:37' WHERE UserID='C11571539' AND TestRound=1;".format(pre_month)
    print(update_sql)
    result = test.update_sql(db, update_sql)
