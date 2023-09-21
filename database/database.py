import sqlite3
import threading
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
db_filename = "pollen.db"
database_path = os.path.join(script_dir, db_filename)


class Database:
    conn = sqlite3.connect(database_path)
    c = conn.cursor()

    lock = threading.Lock()

    def __init__(self):
        pass

    def add_member(self, member_id, guild_id):
        self.c.execute(
            f"SELECT * FROM user WHERE userid='{member_id}' AND guildid='{guild_id}'"
        )
        data = self.c.fetchall()

        if not data:
            # UserID, Level, Warnings, GuildID, xp
            self.c.execute(
                f"INSERT INTO user VALUES (?, ?, ?, ?, ?)",
                (member_id, guild_id, 0, 0, 0),
            )
            self.conn.commit()
    
    def get_user_data(self, member_id, guild_id):
        self.c.execute(
            f"SELECT * FROM user WHERE userid='{member_id}' AND guildid='{guild_id}'"
        )
        print()
        return self.c.fetchone()
    
    def update_level(self, member_id, guild_id, new_level):
        self.c.execute(
            f"UPDATE user SET level={new_level} WHERE userid='{member_id}' AND guildid='{guild_id}'",
        )
        self.conn.commit()

# Accessing the database
db = Database()