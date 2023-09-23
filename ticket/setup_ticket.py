import discord
from discord.ext import commands
from discord import app_commands

# Importing the classes from other files
from .create_ticket import create_ticket
from .delete_ticket import delete_ticket
from .close_ticket import close_ticket
from utilitys.embed_builder import embed_builder

class setup_ticket(commands.Cog):
    def __init__(self, client: commands.bot):
        self.client = client

    # Defining a slash command
    @app_commands.command(name="create-ticket-pannel", description="Create a ticket panel which will create a ticket when pressed")
    async def setup_ticket(self, interaction: discord.Interaction):
        # Check if the user has administrator permission
        if not interaction.user.guild_permissions.administrator:
            # Send a message to the user if they don't have the permission
            await interaction.response.send_message(embed=embed_builder("Ticket", "You need the administrator permission to use this command"), ephemeral=True)
            return

        # Use the class create_ticket to create a view and button
        view = create_ticket()

        # Create the embed
        embed = discord.Embed(
            colour=discord.Colour.yellow()
        )
        embed.add_field(name="Ticket", value="Press the button bellow to create a ticket")
        embed.set_footer(text="Pollen - Lightweight Discordbot",icon_url=self.client.user.avatar.url)

        # Send the embed and view to the channel
        await interaction.channel.send(embed=embed, view=view)

        # Send a message to the user that the panel has been created
        await interaction.response.send_message("Ticket Panel Created!", ephemeral=True)
        
# Defining a setup function to add the cog and views to the bot
async def setup(client: commands.Bot) -> None:
    await client.add_cog(setup_ticket(client))
    client.add_view(create_ticket())
    client.add_view(delete_ticket())
    client.add_view(close_ticket())