import discord
from discord.ext import commands
from discord import app_commands
from utilitys.embed_builder import embed_builder

class setup_ticket(commands.Cog):
    def __init__(self, client: commands.bot):
        self.client = client

    # Define a slash command named "ticket-clean-up" with a description
    @app_commands.command(name="ticket-clean-up", description="Delete all closed tickets")
    async def ticket_clear(self, interaction: discord.Interaction):
        # Check if the user has administrator permission
        if not interaction.user.guild_permissions.administrator:
            # Send a message to the user if they don't have the permission
            await interaction.response.send_message(embed=embed_builder("Ticket", "You need the administrator permission to use this command"), ephemeral=True)
            return
        
        # Get all channels in the server
        channels = interaction.guild.channels
        
        # Loop through all channels
        for channel in channels:
            # Check if the channel name starts with "closed-" and ends with "-pln-archive"
            if channel.name.startswith("closed-") and channel.name.endswith("-pln-archive"):
                # Delete the channel
                await channel.delete()
        
        # Send a message to the user after deleting the channels
        await interaction.response.send_message(embed=embed_builder("Ticket", "If they were any closed tickets they have now been deleted"), ephemeral=True)
        
# Define a function to add the cog to the bot
async def setup(client: commands.Bot) -> None:
    await client.add_cog(setup_ticket(client))