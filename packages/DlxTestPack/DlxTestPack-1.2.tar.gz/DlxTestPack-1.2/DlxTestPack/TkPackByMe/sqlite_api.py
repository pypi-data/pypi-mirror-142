import sqlite3
import os
import time


table_head=('id','create_time','lastchange_time','jira_number','item_name','task','tester','if_finish','remark','sendtest_time' ,'finish_time')

database_addr = r'.\test_table.db'

class sqlite_deal():

    def __init__(self):

        if os.path.exists(database_addr):
            pass

        else:

            sql='CREATE TABLE IF NOT EXISTS table1(id INTEGER PRIMARY KEY AUTOINCREMENT,create_time INTEGER,lastchange_time INTEGER,jira_number TEXT,item_name TEXT,task TEXT,tester TEXT,if_finish INTEGER,remark TEXT,sendtest_time INTEGER,finish_time INTEGER)'

            self.sql_excute(sql,'create table fail')


    def sql_excute(self,sql,message):

        open_file = sqlite3.connect(database_addr)

        cur = open_file.cursor()

        try:

            cur.execute(sql)

            open_file.commit()

        except sqlite3.Error as e:
            print(e)

            print(message)

        finally:

            open_file.close()


    def lastChangeTimeUpdate(self,id):

        str_time_now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(time.time())))

        sql = "UPDATE table1 SET lastchange_time = '\''"+str_time_now+"'\'' WHERE id = "+str(id)

        self.sql_excute(sql,'update data fail')

    def create_row(self):

        str_time_now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(time.time())))
        sql = "INSERT INTO table1 (id,create_time,lastchange_time,if_finish) VALUES (NULL,'\''"+str_time_now+"'\'','\''"+str_time_now +"'\'',0)"

        self.sql_excute(sql,'insert fail')

    def change_single_item(self,id,name_x,value):

        sql = "UPDATE table1 SET {}= {} WHERE id = {}".format(table_head[name_x],'\''+value+'\'',str(id))

        print(sql)

        self.sql_excute(sql,"change")
        self.lastChangeTimeUpdate(id)

    def serch_by_create_time(self):
        open_file = sqlite3.connect(database_addr)

        cur = open_file.cursor()

        # return_data=[]

        try:
            cur.execute("SELECT * FROM table1 WHERE create_time >2021-05-24")

            return_data= cur.fetchall()

        except sqlite3.Error as e:
            print(e)
            print('error')

        finally:

            open_file.close()
            print(return_data)
            return return_data

    def serch_by_lastchange_time(self):
        pass
    def serch_by_jira_number():
        pass

    def get_all_data(self):

        open_file = sqlite3.connect(database_addr)

        cur = open_file.cursor()

        # return_data=[]

        try:

            cur.execute("select * from table1")

            return_data= cur.fetchall()

        except sqlite3.Error as e:
            print(e)
            print('error')

        finally:

            open_file.close()
            print(return_data)
            return return_data


    def delete(self,id):

        sql = 'DELETE FROM table1 WHERE id='+str(id)

        self.sql_excute(sql,'delete fail')
        

    def change(self):
        pass

    def write(self):
        pass

    def output(self):
        pass


