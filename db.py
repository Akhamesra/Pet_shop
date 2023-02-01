import psycopg2
from config import info
class Pet:
    def __init__(cls,pname,pbreed,oname):
        cls.pname = pname
        cls.pbreed =pbreed
        cls.oname = oname

class DBconnector:
    conn = None
    def __init__(cls):
        pass

    @classmethod
    def connect_db(cls):
        return psycopg2.connect(host = info['host'],
                             database = info['database'],
                            user = info['user'],
                            password = info['password'])
    

    def __exit__(cls):
        cls.conn.close()

class DBconnection:
    conn = None
    @classmethod
    def get_connection(cls,new=False):
        if new or not cls.conn:
            db = DBconnector()
            cls.conn  =db.connect_db()
        return cls.conn

    @classmethod
    def create_table(cls,tablename,f1,f2,f3,):
        try:
            conn = cls.get_connection()
            cur = conn.cursor()
        except:
            conn = cls.get_connection(new = True)
            cur = conn.cursor()
        cur.execute('CREATE TABLE '+ str(tablename)+'(id serial PRIMARY KEY,' + str(f1)+ ' varchar (20) NOT NULL,' + str(f2) + ' varchar (20) NOT NULL,' + str(f3) + ' varchar(20) NOT NULL);')
        conn.commit()
        cur.close()
    

    @classmethod
    def insert_db(cls,tablename,f1,f2,f3):
        try:
            conn = cls.get_connection()
            cur = conn.cursor()
        except:
            conn = cls.get_connection(new = True)
            cur = conn.cursor()
        cur.execute('INSERT INTO '+ str(tablename)+ ' (pet_name,pet_breed,owner) VALUES(%s, %s, %s);',(str(f1),str(f2),str(f3)))
        conn.commit()
        cur.close()
    
    @classmethod
    def select_result(cls,tablename):
        conn = cls.get_connection()
        try:
            cur = conn.cursor()
        except:
            conn = cls.get_connection(new = True)
            cur = conn.cursor()
        conn.commit()
        cur.execute('SELECT * FROM pet_shop3;')
        pet_list = cur.fetchall()
        conn.commit()
        cur.close()
        return pet_list

    @classmethod
    def delete_row(cls,tablename,ids):
        try:
            conn = cls.get_connection()
            cur = conn.cursor()
        except:
            conn = cls.get_connection(new = True)
            cur = conn.cursor()
        cur.execute('DELETE FROM '+str(tablename)+' Where id = %s;',(ids,))
        conn.commit()
        cur.close()

    @classmethod
    def select_row(cls,tablename,ids):
        try:
            conn = cls.get_connection()
            cur = conn.cursor()
        except:
            conn = cls.get_connection(new = True)
            cur = conn.cursor()
        cur.execute('SELECT * FROM '+ str(tablename) + ' WHERE id = %s;',(ids,))
        pet_list = cur.fetchall()
        conn.close()
        cur.close()
        return pet_list
    
    @classmethod
    def edit(cls,tablename,f1,f2,f3,ids):
        try:
            conn = cls.get_connection()
            cur = conn.cursor()
        except:
            conn = cls.get_connection(new = True)
            cur = conn.cursor()
        cur.execute("UPDATE "+str(tablename)+ " SET pet_name = '" + str(f1) + "',pet_breed = '" + str(f2) + "',owner = '" + str(f3) + "' WHERE id = %s;",(ids,))   
        conn.commit()
        cur.close()
        
        
