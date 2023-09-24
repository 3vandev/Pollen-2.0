from database.database import db
from discord.ext import commands
from database.database import db
from joinmessage import join_message


class send_join_message(commands.Cog):
    def __init__(self, client: commands.bot):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # Get the guild ID
        guild_id = member.guild.id

        # Get the welcome channel ID
        join_channel_id = db.get_join_message_channel(guild_id)

        # If the welcome channel ID is not "None"
        if join_channel_id != None:
            # Get the welcome channel
            welcome_channel = self.client.get_channel(join_channel_id)

            # Send the join message
            await welcome_channel.send(embed=join_message.send_join_message(member, guild_id))

async def setup(client: commands.Bot) -> None:
    await client.add_cog(send_join_message(client))

# Setting up the cog