import psycopg2
class Pet:
    def __init__(self,pname,pbreed,oname):
        self.pname = pname
        self.pbreed =pbreed
        self.oname = oname

class DBconnection:
    conn = None
    cur = None
    def __init__(self):
        pass
    @classmethod
    def connect_db(self):
        self.conn = psycopg2.connect(host = 'localhost',
                            database = 'Flask_db',
                            user = 'postgres',
                            password = 'Finserv@2023')
        self.cur = self.conn.cursor()

    @classmethod
    def create_table(self,tablename,f1,f2,f3,):
        #self.cur.execute('DROP TABLE IF EXISTS ' + str(tablename))
        self.cur.execute('CREATE TABLE '+ str(tablename)+'(id serial PRIMARY KEY,' + str(f1)+ ' varchar (20) NOT NULL,' + str(f2) + ' varchar (20) NOT NULL,' + str(f3) + ' varchar(20) NOT NULL);')
        self.conn.commit()

    @classmethod
    def insert_db(self,tablename,f1,f2,f3):
        self.cur.execute('INSERT INTO '+ str(tablename)+ ' (pet_name,pet_breed,owner) VALUES(%s, %s, %s);',(str(f1),str(f2),str(f3)))
        self.conn.commit()
    
    @classmethod
    def select_result(self,tablename):
        self.cur.execute('SELECT * FROM '+str(tablename)+';')
        return self.cur.fetchall()

    @classmethod
    def delete_row(self,tablename,ids):
        self.cur.execute('DELETE FROM '+str(tablename)+' Where id = %s;',(ids,))
        self.conn.commit()

    @classmethod
    def select_row(self,tablename,ids):
        self.cur.execute('SELECT * FROM '+ str(tablename) + ' WHERE id = %s;',(ids,))
        return self.cur.fetchall()
    
    @classmethod
    def edit(self,tablename,f1,f2,f3,ids):
        self.cur.execute("UPDATE "+str(tablename)+ " SET pet_name = '" + str(f1) + "',pet_breed = '" + str(f2) + "',owner = '" + str(f3) + "' WHERE id = %s;",(ids,))   
        self.conn.commit()
        
        
    @classmethod
    def close(self):
        self.cur.close()
        self.conn.close()
