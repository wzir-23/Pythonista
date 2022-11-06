from datetime import datetime
import os
import sqlite3
import ui



def ToggleFasting(sender):
    ''' The start/stop button was pressed '''
    started = get_status(cursor)
    if fasting_started:
        sender.title = 'Start fasting'
    else:
        sender.title = 'Stop fasting'
    add_time_to_db(db_connection, cursor, started)


def RefreshPressed(sender):
    ''' The refresh button was pressed '''
    pass


def connect_db(fname):
    """ connect to sqlite3 db or create if missing """
    create_tables = False
    if not os.path.isfile(fname): # no such file
        create_tables = True
    db_connection = sqlite3.connect(fname)
    cursor = db_connection.cursor()
    if create_tables:
        cursor.execute('''CREATE TABLE fasting(start_time text,
                          stop_time text)''')
    return db_connection, cursor
        

def list_database(cursor):
    ''' list all database intries '''
    sql = 'SELECT rowid, start_time, stoptime FROM fasting'
    cursor.execute(sql)
    return cursor.fetchall()


def last_db_entry(cursor):
    sql = 'SELECT rowid,* FROM fasting ORDER BY start_time DESC LIMIT 1'
    cursor.execute(sql)
    return cursor.fetchall()


def get_status(cursor):
    last_entry = last_db_entry(cursor)
    if not last_entry:   # db empty
        return False
    rowid, start_time, stop_time = last_entry[0]
    if start_time and stop_time:  # last was started and stopped
        return False
    return True


def add_time_to_db(db_connection, cursor, started):
    ''' Add current time on format "2022-11-05 21:51" to database '''
    now_time = datetime.now()
    time_string = now_time.strftime('%Y-%m-%d %H:%M')
    if not started:
        cursor.execute('''INSERT INTO fasting(start_time, stop_time)
                       VALUES(?,?)''', (time_string, ''))
        db_connection.commit()
    else:
        rowid, started, stopped = last_db_entry(cursor)[0]
        cursor.execute('''UPDATE fasting SET stop_time=? where rowid=?''',
                       (time_string, rowid))
        db_connection.commit()


                        
        
# The loading must appear after defining the ui actions

def main():
    fname = 'FastFasting.db'
    db_connection, cursor = connect_db(fname)
    v = ui.load_view('FastFasting')
    v.present('sheet')


if __name__ == "__main__":
    main()
