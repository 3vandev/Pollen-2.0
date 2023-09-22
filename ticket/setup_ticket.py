import discord
from discord.ext import commands
from discord import app_commands
from .create_ticket import create_ticket
from utilitys import embed_builder

class setup_ticket(commands.Cog):
    def __init__(self, client: commands.bot):
        self.client = client

    @app_commands.command(name="ticket-setup", description="Setup tickets")
    async def setup_ticket(self, interaction: discord.Interaction):
        # Use the class create_ticket to create a view and button
        view = create_ticket()
        # Create the embed
        embed = discord.Embed(
            colour=discord.Colour.yellow()
        )
        embed.add_field(name="Ticket", value="Press the button bellow to create a ticket")
        embed.set_footer(text="Pollen - Lightweight Discordbot",icon_url=self.client.user.avatar.url)
        await interaction.response.send_message(embed=embed, view=view)
        
async def setup(client: commands.Bot) -> None:
    await client.add_cog(setup_ticket(client))
    client.add_view(create_ticket())