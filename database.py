import sqlite3

DB_NAME = "certificates.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            message TEXT,
            priority TEXT,
            status TEXT DEFAULT 'Pending',
            reply TEXT DEFAULT ''
        )
    ''')

    conn.commit()
    conn.close()


def add_reply(req_id, reply):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("UPDATE requests SET reply=? WHERE id=?", (reply, req_id))
    conn.commit()
    conn.close()

def insert_request(name, email, message, priority):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO requests (name, email, message, priority) VALUES (?, ?, ?, ?)",
              (name, email, message, priority))
    conn.commit()
    conn.close()

def get_all_requests():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM requests ORDER BY id DESC")
    data = c.fetchall()
    conn.close()
    return data

def update_status(req_id, status):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("UPDATE requests SET status=? WHERE id=?", (status, req_id))
    conn.commit()
    conn.close()