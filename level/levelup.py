import discord
from discord import app_commands
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

        db.add_member(message.author.id, message.guild.id)
        user_data = db.get_user_data(message.author.id, message.guild.id)
        db.update_xp(message.author.id, message.guild.id, user_data[3] + 100)
        if user_data[3] >= 1000:
            db.update_xp(message.author.id, message.guild.id, 0)
            db.update_level(message.author.id, message.guild.id, user_data[2] + 1)

            # Get the directory where the script is located
            script_dir = os.path.dirname(os.path.abspath(__file__))

            # Construct the full path to 'level.png' in the same directory as the script
            image_path = os.path.join(script_dir,"levelup.png")

            image = Image.open(image_path).convert("RGBA")

            asset = message.author.avatar
            data = BytesIO(await asset.read())
            pfp = Image.open(data)
            pfp = pfp.resize((98,98))
            pfp = circle(pfp)
            
            # Create a new image with a white background
            text_image = Image.new('RGBA', image.size, (255, 255, 255, 0))
            draw = ImageDraw.Draw(text_image)

            text = f'Level {user_data[2] + 1}'
            
            font = ImageFont.truetype("font.ttf", 45)

            draw.text((10,10), text, (255,255,255), font=font)
            
            # Paste the text image onto the original image using the alpha channel of the original image as a mask
            image.alpha_composite(text_image, (250,60))
            image.alpha_composite(pfp, (2,2))
            
            image.save("profile.png")

            await message.channel.send(f"Well done <@{message.author.id}> you leveled up",file=discord.File("profile.png"))
        
async def setup(client: commands.Bot) -> None:
    await client.add_cog(levelup(client))