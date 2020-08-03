import pymssql

db = pymssql.connect(server=".", database='master')  # 确保TCP/IP启用，相应IP地址启用
cursor = db.cursor()
cursor.execute("""SELECT TOP (1000) [isbn]
      ,[title]
      ,[authors]
      ,[publisher]
  FROM [StudentManagement].[dbo].[book]""")
data = cursor.fetchone()  # 返回单个元组
print(data)
db.close()
