import discord
from discord.ext import commands
from discord import app_commands

class rules(commands.Cog):
    def __init__(self, client: commands.bot):
        self.client = client
        
    @app_commands.command(name="rules", description="Display the rules")
    async def modal(self, interaction: discord.Interaction):
        await interaction.response.send_message("Go to <#1225379360828293211> for the rules.", ephemeral=True)

async def setup(client: commands.Bot) -> None:
    await client.add_cog(rules(client))
