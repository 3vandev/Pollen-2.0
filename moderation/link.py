import discord
from discord.ext import commands
from discord import app_commands

class link(commands.Cog):
    def __init__(self, client: commands.bot):
        self.client = client
        
    @app_commands.command(name="link", description="Game link!")
    async def modal(self, interaction: discord.Interaction):
        await interaction.response.send_message("https://www.roblox.com/games/6804602922/Boxing-Beta", ephemeral=True)

async def setup(client: commands.Bot) -> None:
    await client.add_cog(link(client))
