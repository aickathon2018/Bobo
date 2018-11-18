import sqlite3 as sql
import datetime, hashlib, json, os.path, sys, os

class UserModel:
    def __init__(self, dbname):
        self.__database  = 'root/' + dbname + '.db'
        assert os.path.isfile(self.__database), 'database {} is not available'.format(self.__database)

    def authUser(self, username, password):
        con = sql.connect(self.__database)
        cur = con.cursor()
        password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        cur.execute('SELECT user_id, username, password FROM User WHERE username = ?', [username])
        con.commit()
        user = cur.fetchall()
        count = len(user)
        con.close()
        assert count < 2, 'the username is not unique'
        
        return ('' if count == 0 else user[0][0] if password_hash == user[0][2] else 'N')

    def authUserQuick(self, user_id):
        con = sql.connect(self.__database)
        cur = con.cursor()
        cur.execute('SELECT user_id, username FROM User WHERE user_id = ?', [user_id])
        con.commit()
        user = cur.fetchall()
        count = len(user)
        con.close()
        assert count < 2, 'the username is not unique'
        return ('' if count == 0 else user[0][1])

    def createUser(self, username, password, age, gender):
        con = sql.connect(self.__database)
        cur = con.cursor()
        password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        cur.execute('SELECT user_id, username FROM User WHERE username = ?', [username])
        user = cur.fetchall()
        count = len(user)
        if count != 0: return 'NOT_UNIQUE_USERNAME'
        cur.execute('INSERT INTO User(username, password, age, gender) VAlUES (?, ?, ?, ?)', [username, password_hash, age, gender])
        con.commit()
        con.close()
        return 'SUCCESS'

class style:
    def __init__(self, dbname):
        self.__database  = 'root/' + dbname + '.db'
        assert os.path.isfile(self.__database), 'database {} is not available'.format(self.__database)

    def addItem(self, file, style):
        con = sql.connect(self.__database)
        cur = con.cursor()
        cur.execute('SELECT image_id, filename FROM Style WHERE filename = ?', [file])
        user = cur.fetchall()
        count = len(user)
        if count != 0: return 'NOT_UNIQUE_FILENAME'
        cur.execute('INSERT INTO Style(filename, style) VAlUES (?, ?)', [file, style])
        con.commit()
        con.close()
        return 'SUCCESS'

    def searchStyle(self, style):
        con = sql.connect(self.__database)
        cur = con.cursor()
        cur.execute('SELECT filename, style FROM Style WHERE style = ?', [style])
        con.commit()
        user = cur.fetchall()
        con.close()
        
        return (user)