import xlrd,os
# def get(files):
#     rows=[]  #srore rows
#     book = xlrd.open_workbook(files)  #读取整个文件
#     print(book.sheet_names())
#     table = book.sheet_by_index(0)  #获取excel中的一张表
#     for row_idx in range(1,table.nrows):
#         rows.append(table.row_values(row_idx,start_colx=0,end_colx=table.ncols))#返回所在行的数据对象列表
#     return rows
# t = get('test.xlsx')
# print(t)
class File_read(object):
    def __init__(self,file_path):
        self.file_path =file_path
        if not os.path.exists(self.file_path):
            print(self.file_path+"不存在")

    def excel_read(self, sheet_name):
        rows = []
        try:
            self.book = xlrd.open_workbook(self.file_path)
            print('111')
            if sheet_name in self.book.sheet_names():
                table = self.book.sheet_by_name(sheet_name)
                for row_idx in range(0, table.nrows):
                    rows.append(table.row_values(row_idx, start_colx=0, end_colx=table.ncols))  # 返回所在行的数据对象列表
                return rows
            else:
                raise NotImplemented
        except Exception as e:
            print('找不到文件的目录')
            raise e
# class oracle_database():
import cx_Oracle
from conf.setting import *
class oracle_database():
    def __init__(self):
        self.conn_message = oracle_conn['username']+'/'+oracle_conn['password']+'@'+oracle_conn['ip']+':'+oracle_conn['port']+'/'+oracle_conn['service_name']
        print(self.conn_message)
        try:
            self.conn = cx_Oracle.connect(self.conn_message)
        except:
            print('连接有误')

    def select(self, table, value, where=None):
        if where==None:
            sql = 'select %s from %s'(value,table)
            self.curs = self.conn.cursor()
            self.curs.execute(sql)
            return self.curs.fetchone() #关闭游标
        else:
            sql = 'select %s from %s where '
    def insert(self,table,value):
        sql = 'insert into %s()'
        self.curs = self.conn.cursor()
        self.curs.execute(sql)
        return self.conn.submit()

if __name__=='__main__':
    # t = File_read(r'C:\Users\Administrator\Desktop\修改密码.xlsx').excel_read('Sheet1')
    # print(t)
    r = oracle_database().select('insert into customer_table () values ()')
    print(r)