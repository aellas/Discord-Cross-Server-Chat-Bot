import sqlite3

def create_table():
    conn = sqlite3.connect("src/database/channel_ids.db")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS channels (id INTEGER PRIMARY KEY)")

    conn.commit()
    conn.close()

def fetch_channel_ids():
    conn = sqlite3.connect("src/database/channel_ids.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM channels")
    rows = cursor.fetchall()
    channel_ids = [row[0] for row in rows]

    conn.close()
    return channel_ids

def add_channel_id(channel_id):
    conn = sqlite3.connect("src/database/channel_ids.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO channels (id) VALUES (?)", (channel_id,))

    conn.commit()
    conn.close()

def remove_channel_id(channel_id):
    conn = sqlite3.connect("src/database/channel_ids.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM channels WHERE id=?", (channel_id,))

    conn.commit()
    conn.close()
