import discord
from discord import app_commands
from discord.ext import commands
from utilitys.embed_builder import embed_builder, field
from database import database
from io import BytesIO
import os

db = database.db

class enable_level_up(commands.Cog):
    def __init__(self, client: commands.bot):
        self.client = client

    @app_commands.command(name="level-up", description="Edit your level up message | [channel] [message]")
    @app_commands.describe(channel='Leave blank for the welcome message to be sent to the same channel as the user is typing in', message='Leave blank to use the default level up message')
    async def setup_ticket(self, interaction: discord.Interaction, channel: discord.TextChannel = None, message: str = None):
        # Check if the user has administrator permission
        if not interaction.user.guild_permissions.administrator:
            # Send a message to the user if they don't have the permission
            await interaction.response.send_message(embed=embed_builder(interaction.command.name, "You need the administrator permission to use this command"), ephemeral=True)
            return
        
        if not channel:
            channel = "None"
        else:
            channel = channel.id

        if not message:
            message = "Default"
        
        old = db.get_level_up(interaction.guild_id)
        db.set_level_up(interaction.guild_id, channel, message)
        
        if channel == "None":
            channel = "Same Channel as the user is typing in"
        else:
            channel = f"<#{channel}>"

        # Handle cases where `old` might be `None`
        if old is not None:
            before_text = f"Channel: {old[1]}\nMessage: {old[2]}"
        else:
            before_text = "No previous data available."

        # Create the embed
        overview = embed_builder(
            "Level Up Message",
            "Level Up Message has been set",
            fields=[
                field("Before", before_text),
                field("After", f"Channel: {channel}\nMessage: {db.get_level_up(interaction.guild_id)[2]}"),
            ],
        )

        # Send a message to the user that the panel has been created
        await interaction.response.send_message(embed=overview, ephemeral=True)

async def setup(client: commands.Bot) -> None:
    await client.add_cog(enable_level_up(client))
