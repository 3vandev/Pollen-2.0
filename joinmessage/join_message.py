from database.database import db
from utilitys.embed_builder import embed_builder
import discord
def send_join_message(target_member = None, guild_id = None):
    # Try to get the join message from the database
    try:
        join_message = db.get_join_message(guild_id)
    except:
        # If there's an error, set the join message to "None"
        join_message = None
    
    # {user} - The user that joined
    # {guild} - The guild that the user joined
    # {membercount} - The membercount of the guild
    # {userping} - The user that joined, but with a ping

    # Now we are going to use .replace() to replace the placeholders with the actual values
    join_message = join_message.replace("{user}", target_member.name)
    join_message = join_message.replace("{guild}", f"**{target_member.guild.name}**")
    join_message = join_message.replace("{membercount}", str(target_member.guild.member_count))
    join_message = join_message.replace("{userping}", f"<@{target_member.id}>")
    
    # Build the welcome message using the join message
    message = discord.Embed(
        title="Welcome",
        description=join_message,
        colour=discord.Colour.green()
    )
    
    # Return the welcome message
    return message