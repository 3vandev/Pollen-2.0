import discord
from discord.ext import commands
import config
from database import database
from utilitys import embed_builder

# Define some variables
field = embed_builder.field
db = database.db

# Define a client class that inherits from commands.Bot
class client(commands.Bot):
    bot = None

    def __init__(self):
        # Call the constructor of the parent class
        super().__init__(command_prefix="!", intents=discord.Intents.all())
        self.synced = False

    # Define a list of cogs to load
    cogslist = [
        "moderation.ban",
        "ticket.setup_ticket",
        "level.levelup",
        "joinmessage.set_join_message",
        "joinmessage.test_join_message",
    ]

    # Define a setup hook to load all the cogs
    async def setup_hook(self):
        for ext in self.cogslist:
            await self.load_extension(ext)

    # Define an on_ready event handler
    async def on_ready(self):
        # Wait until the bot is ready
        await self.wait_until_ready()
        # Sync the database if it hasn't been synced yet
        if not self.synced:
            await self.tree.sync()
        # Print a message to indicate that the bot has logged in
        print(f"Logged In >> {self.user.name}")

# Create an instance of the client class and run it
client = client()
client.run(config.TOKEN)
