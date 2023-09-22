import discord
from discord.ext import commands
from discord import app_commands, ui
import os
from importlib.machinery import SourceFileLoader
from discord.interactions import Interaction

class say(commands.Cog):
    def __init__(self, client: commands.bot):
        self.client = client
    @app_commands.command(name="hey", description="Say something!")
    async def modal(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hey")


async def setup(client: commands.Bot) -> None:
    await client.add_cog(say(client))
