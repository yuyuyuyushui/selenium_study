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



if __name__=='__main__':
    t = File_read('tes.xlsx').excel_read('Sheet1')
    print(t)