# import pymysql
#
#
# def read_from_db(sql):
#
#     #connect to db
#
#     connection=pymysql.connect(host='127.0.0.1', port=8889,user='root',password='root')
#
#
#     #read from db
#
#     try:
#
#         cursor = connection.cursor(pymysql.cursors.DictCursor)
#         cursor.execute(sql)
#         db_data = cursor.fetchall()
#         cursor.close()
#
#     finally:
#
#         connection.close()
#
#     #return the result
#
#     return  db_data
#
#
# def get_order_from_db_by_orderno(order_no):
#
#     sql=f"SELECT * FROM abc where ID={order_no}"
#     db_order=read_from_db(sql)