import discord
from discord.ext import commands
import config
from database import database
from utilitys import embed_builder

field = embed_builder.field
db = database.db

class client(commands.Bot):
    bot = None

    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())
        self.synced = False

    #async def setup_hook(self):
        #for ext in self.cogslist:
            #await self.load_extension(ext)

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await self.tree.sync()
        print(f"Logged In >> {self.user.name}")
client = client()

@client.event
async def on_message(message):
    if message.author.bot:
        return
    
    #"userid"	INTEGER,
	#"guildid"	INTEGER,
	#"level"	INTEGER,
	#"xp"	INTEGER,
	#"warnings"	INTEGER

    db.add_member(message.author.id, message.guild.id)
    user_data = db.get_user_data(message.author.id, message.guild.id)
    db.update_level(message.author.id, message.guild.id, user_data[2] + 1)
    await message.reply(f"Your level is now {user_data[2] + 1}")
        
client.run(config.TOKEN)
