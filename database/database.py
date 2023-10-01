import sqlite3
import threading
import os

# Get the path of the script directory and the database filename
script_dir = os.path.dirname(os.path.abspath(__file__))
db_filename = "pollen.db"

# Join the script directory and database filename to get the full database path
database_path = os.path.join(script_dir, db_filename)


class Database:
    # Connect to the database and create a cursor object
    conn = sqlite3.connect(database_path)
    c = conn.cursor()

    # Create a lock object to ensure thread safety
    lock = threading.Lock()

    def __init__(self):
        pass

    def add_member(self, member_id, guild_id):
        # Check if the user is already in the database
        self.c.execute(
            f"SELECT * FROM user WHERE userid='{member_id}' AND guildid='{guild_id}'"
        )
        data = self.c.fetchall()

        # If the user is not in the database, add them
        if not data:
            self.c.execute(
                f"INSERT INTO user VALUES (?, ?, ?, ?, ?)",
                (member_id, guild_id, 0, 0, 0),
            )
            self.conn.commit()

    def get_user_data(self, member_id, guild_id):
        # Get the user's data from the database
        self.c.execute(
            f"SELECT * FROM user WHERE userid='{member_id}' AND guildid='{guild_id}'"
        )
        return self.c.fetchone()

    def update_level(self, member_id, guild_id, new_level):
        # Update the user's level in the database
        self.c.execute(
            f"UPDATE user SET level={new_level} WHERE userid='{member_id}' AND guildid='{guild_id}'",
        )
        self.conn.commit()

    def update_xp(self, member_id, guild_id, new_xp):
        # Update the user's XP in the database
        self.c.execute(
            f"UPDATE user SET xp={new_xp} WHERE userid='{member_id}' AND guildid='{guild_id}'",
        )
        self.conn.commit()

    def update_join_message(self, guild_id, welcome_message, channel_id):
        # Delete the old join message for the guild and insert the new one
        self.c.execute(
            f"DELETE FROM guild WHERE guildid='{guild_id}'",
        )
        self.c.execute(
            f"INSERT INTO guild VALUES (?, ?, ?)",
            (guild_id, welcome_message, channel_id),
        )
        self.conn.commit()

    def get_join_message(self, guild_id):
        # Get the join message for the guild
        self.c.execute(
            f"SELECT * FROM guild WHERE guildid='{guild_id}'"
        )
        return self.c.fetchone()[1]

    def get_join_message_channel(self, guild_id):
        # Get the channel ID for the join message for the guild
        self.c.execute(
            f"SELECT * FROM guild WHERE guildid='{guild_id}'"
        )
        return self.c.fetchone()[2]
    

    # Level up
    # guildid, channelid, message

    def get_level_up(self, guild_id):
        # Get the channel ID for the join message for the guild
        self.c.execute(
            f"SELECT * FROM levelup WHERE guildid='{guild_id}'"
        )
        return self.c.fetchone()
    
    def set_level_up(self, guild_id, channel_id, message):
        self.c.execute(
            f"DELETE FROM levelup WHERE guildid='{guild_id}'",
        )
        self.c.execute(
            f"INSERT INTO levelup VALUES (?, ?, ?)",
            (guild_id, channel_id, message),
        )
        self.conn.commit()

    # Define the structure of the user table in the database
    #"userid"	INTEGER,
    #"guildid"	INTEGER,
    #"level"	INTEGER,
    #"xp"	INTEGER,
    #"warnings"	INTEGER,


# Create an instance of the Database class to access the database
db = Database()