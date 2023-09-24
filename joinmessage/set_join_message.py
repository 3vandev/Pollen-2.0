import discord
from discord.ext import commands
from discord import app_commands

# Importing custom modules
from utilitys.embed_builder import embed_builder, field
from database.database import db

class set_join_message(commands.Cog):
    def __init__(self, client: commands.bot):
        self.client = client

    # Defining a slash command
    @app_commands.command(name="set-join-message", description="Set Join Message | <message> <channel>")
    @app_commands.describe(message='{user}, {guild}, {membercount}, {userping} will be replaced with the actual values', channel='The channel where the join message will be sent')
    async def set_join_message(self, interaction: discord.Interaction, message: str, channel: discord.TextChannel):
        try:
            join_message = db.get_join_message(interaction.guild_id)
        except:
            join_message = "None"

        # Building an embed to show the before and after message
        overview = embed_builder(
            "Join Message",
            "Join Message has been set",
            fields=[
                field("Before", join_message),
                field("After", message),
            ],
        )

        # Updating the join message in the database
        db.update_join_message(interaction.guild_id, message, channel.id)

        # Sending the embed as a response to the slash command
        await interaction.response.send_message(embed=overview)


# Setting up the cog
async def setup(client: commands.Bot) -> None:
    await client.add_cog(set_join_message(client))
