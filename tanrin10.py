import sqlite3

db = sqlite3.connect('tablesql.db')

cursor = db.cursor()

cursor.execute("CREATE TABLE  sql(id INTEGER PRIMARY KEY, Name TEXT,Family TEXT, year INTEGER)")

#INSERT

id= '1001'
Name= 'mona'
family='poriran'
year='2000'


cursor.execute(''' INSERT INTO Assets(id,Name,Family,year) VALUE(?,?,?,?) ''' ,(id1, Name2,family3,year4)

db.commit()

#UPDATE

newyears1 = '2001'
newyear2='2005'
sqlid1= '1'
sqlid2= '2'

cursor.execute('''UPDATE Assets SET Price = ? WHERE id = ?''',(newyear1, sqlid1))

cursor.execute('''UPDATE Assets SET Price = ? WHERE id = ?''',(newyear2 , sqlid2))

#DELETE & INSERT

delete_sqlid = '5'
delete_sqlid = '6'

new_sqlid = '1'
new_sqlname = 'mona'
new_sqlfamily='poriran'
new_sqlyear= '2005'

cursor.execute('''DELETE FROM sql WHERE id = ?''',(delete_sqlid = '1',))

cursor.execute('''DELETE FROM sql WHERE id = ?''',(delete_assets_id = '2',))

cursor.execute(''' INSERT INTO sql(id,Name,family,year) VALUE(?,?,?,?) ''' ,(new_sqlid , new_sqlname,new_sqlfamily,new_sqlyear)

db.commit()

#INSERT & UPDATE

new_sqlid1 = '5'
new_sqlname1 = 'maral'
new_sqlfamily1 = 'Kamali'
new_sqlyear1 = '2009'

new_sqlid2 = '6'
new_sqlname2 = 'mehdi'
new_sqlfamily2 = 'talbi'
new_sqlyear2 = '3000'


cursor.execute(''' INSERT INTO sql(id,Name,family,year) VALUE(?,?,?,?) ''' ,(new_sqlid1 , new_sqlname1,new_sqlfamily1,new_sqlyear1)

cursor.execute(''' INSERT INTO sql(id,Name,family,year) VALUE(?,?,?,?) ''' ,(new_sqlid2, new_sqlname2,new_sqlfamily2,new_sqlyear2)

cursor.execute('''UPDATE sql SET year= ? WHERE id = ?''',(new_sqlyear4, sqlid4))

db.commit

query = "SELECT * FROM sql;

cursor.execute(query)
print(cursor.fetchall())