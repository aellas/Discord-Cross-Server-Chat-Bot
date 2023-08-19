import sqlite3

def create_table():
    conn = sqlite3.connect("database/channel_ids.db")
    cursor = conn.cursor()

    # Drop the existing table if it exists
    cursor.execute("DROP TABLE IF EXISTS channels")

    # Recreate the table with the correct primary key constraint
    cursor.execute("CREATE TABLE channels (id INTEGER PRIMARY KEY, guild_id INTEGER UNIQUE)")

    conn.commit()
    conn.close()

def fetch_channel_ids():
    conn = sqlite3.connect("database/channel_ids.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM channels")
    rows = cursor.fetchall()
    channel_ids = [row[0] for row in rows]

    conn.close()
    return channel_ids

def add_channel_id(channel_id, guild_id):
    conn = sqlite3.connect("database/channel_ids.db")
    cursor = conn.cursor()

    cursor.execute("SELECT guild_id FROM channels WHERE guild_id=?", (guild_id,))
    existing_guild = cursor.fetchone()

    if existing_guild:
        conn.close()
        return False
    else:
        cursor.execute("INSERT INTO channels (id, guild_id) VALUES (?, ?)", (channel_id, guild_id))
        conn.commit()
        conn.close()
        return True
    
def remove_channel_id(channel_id):
    conn = sqlite3.connect("database/channel_ids.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM channels WHERE id=?", (channel_id,))

    conn.commit()
    conn.close()
