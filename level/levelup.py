import discord
from discord.ext import commands
from utilitys import embed_builder
from database import database
from PIL import Image, ImageDraw, ImageChops,ImageFont
from io import BytesIO
import os

def circle(pfp,size = (215,215)):
    
    pfp = pfp.resize(size).convert("RGBA")
    
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask) 
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

db = database.db
class levelup(commands.Cog):
    def __init__(self, client: commands.bot):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.bot:
            return
        
        #"userid"	INTEGER,
        #"guildid"	INTEGER,
        #"level"	INTEGER,
        #"xp"	INTEGER,
        #"warnings"	INTEGER,

        # Get the directory where the script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the full path to 'level.png' in the same directory as the script
        image_path = os.path.join(script_dir,"levelup.png")

        image = Image.open(image_path)

        asset = message.author.avatar
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((289,289))
        pfp = circle(pfp)
        draw = ImageDraw.Draw(pfp)

        text = 'https://devnote.in'
        
        draw.text((312,153))
        image.paste(pfp, (25,25))
        
        image.save("profile.png")

        await message.channel.send(file=discord.File("profile.png"))
        db.add_member(message.author.id, message.guild.id)
        user_data = db.get_user_data(message.author.id, message.guild.id)
        db.update_level(message.author.id, message.guild.id, user_data[2] + 1)
        await message.reply(f"Your level is now {user_data[2] + 1}")
        
        
async def setup(client: commands.Bot) -> None:
    await client.add_cog(levelup(client))