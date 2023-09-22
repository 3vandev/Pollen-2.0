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

    cogslist = [
        "moderation.ban",
        "ticket.setup_ticket",
        "level.levelup",
    ]

    async def setup_hook(self):
        for ext in self.cogslist:
            await self.load_extension(ext)
        

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await self.tree.sync()
        print(f"Logged In >> {self.user.name}")
        
client = client()
client.run(config.TOKEN)
