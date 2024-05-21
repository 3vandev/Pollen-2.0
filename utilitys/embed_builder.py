import discord

class field:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

def embed_builder(title, description, fields = None, color = discord.Color.light_embed()):
    embed = discord.Embed(
        title=title,
        description=description,
        color=color,
    )
    if fields:
        for field in fields:
            embed.add_field(name=field.name, value=field.description)
    embed.set_footer(text=f"Premier Boxing Association",icon_url="https://cdn.discordapp.com/icons/1225123710768513116/3d9904e34f51e265507e33af9b03830b.webp?size=96")

    return embed
