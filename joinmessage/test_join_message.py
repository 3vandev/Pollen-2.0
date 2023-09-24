import discord
from discord.ext import commands
from discord import app_commands

from utilitys.embed_builder import embed_builder, field
from database.database import db
from joinmessage.join_message import send_join_message


class test_join_message(commands.Cog):
    def __init__(self, client: commands.bot):
        self.client = client

    # Define a slash command called "test-join-message"
    @app_commands.command(name="test-join-message", description="Test out your join message")
    async def test_join_message(self, interaction: discord.Interaction):
        # Get the channel where the join message will be sent
        channel = self.client.get_channel(db.get_join_message_channel(interaction.guild_id))
        
        # Send the join message to the channel
        await channel.send(embed=send_join_message(interaction.user, interaction.guild_id))
        
        # Send a response message to the user who triggered the command
        await interaction.response.send_message(embed=embed_builder("Join Message", "Join Message has been sent"))


async def setup(client: commands.Bot) -> None:
    await client.add_cog(test_join_message(client))
