import sqlite3

def add():
    conn = sqlite3.connect('pass.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS PASSDB(acc TEXT, url TEXT, uid TEXT, passwd TEXT)')
    
    acc = input('Account Name: ')
    url = input("Enter The Login URL: ")
    uid = input('Enter Username: ')
    passwd = input('Enter Password: ')
    c.execute('INSERT INTO PASSDB(acc, url, uid, passwd) VALUES(?, ?, ?)', (acc, url, uid, passwd))
    conn.commit()

    c.close()
    conn.close() 


'''def find():
    conn = sqlite3.connect('pass.db')
    c = conn.cursor()

    acc = input('Enter The Account Name: ')
    c.execute('SELECT * FROM PASSDB WHERE acc is VALUES(?)', (acc))

    conn.commit()
    c.close()
    conn.close()'''


#test
#add()
#find()