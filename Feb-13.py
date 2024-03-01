# import mysql.connector
# conn=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="sajith@123",
#     database="employee")
#
#
# cursor=conn.cursor()
# print(conn.is_connected())
#
# mysql="SELECT ROLE, MIN(SALARY) AS MIN_SALARY, MAX(SALARY) AS MAX_SALARY FROM EMP_RECORD_TABLE GROUP BY ROLE;"
# mysql=("SELECT continent,country,"
#        " AVG(salary) AS average_salary"
#        " FROM emp_record_table"
#        " GROUP BY continent, country ;")
# cursor.execute(mysql)
# rows=cursor.fetchall()
# print(rows)
# for i in rows:
#     print(i)





#########################################
# import mysql.connector
# conn=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="sajith@123",
#     database="imbd"
# )
#
# cursor=conn.cursor()
# print(conn.is_connected())
#
# mysql=("SELECT * FROM emp_records")
#
# cursor.execute(mysql)
# my_sql=cursor.fetchall()
# for i in my_sql:
#     print(i)



# import mysql.connector
#
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="sajith@123",
#     database="imbd"
# )
#
# cursor = conn.cursor()
#
# print(conn.is_connected())
#
# mysql_query = "SELECT * FROM emp_records"
#
# cursor.execute(mysql_query)
#
# result = cursor.fetchall()
#
# for row in result:
#     print(row)

#############################################################################
# import mysql.connector
# conn=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="sajith@123",
#     database="employee"
# )
#
# cursor=conn.cursor()
# print(conn.is_connected())
#
# mysql_query="select * from emp_record_table"
#
# cursor.execute(mysql_query)
# result=cursor.fetchall()
#
# for mysql in result:
#     print(mysql)











#########################################################
#
# import mysql.connector
# conn=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="sajith@123",
#     database="imbd"
# )
#
# cursor=conn.cursor()
# print(conn.is_connected())
#
# mysql_query="select * from emp_records"
#
# cursor.execute(mysql_query)
# result=cursor.fetchall()
# for i in result:
#     print(i)





######
import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password="sajith@123",
    database="employee"
)

cursor=conn.cursor()
print(conn.is_connected())

# mysql_syntax="""SELECT EMP_ID, FIRST_NAME, LAST_NAME, GENDER, DEPT, EMP_RATING
# FROM EMP_RECORD_TABLE
# WHERE EMP_RATING BETWEEN 2 AND 4;
# """
mysql_syntax="""SELECT EMP_ID, FIRST_NAME, LAST_NAME, GENDER, DEPT, EMP_RATING
FROM emp_record_table
WHERE EMP_RATING<2;"""

cursor.execute(mysql_syntax)
result=cursor.fetchall()

for i in result:
    print(i)


















