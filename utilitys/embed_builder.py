import discord

class field:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

def error(description: str):
    return discord.Embed(
        title="An Error Occurred",
        description=description,
        color=discord.Color.red(),
    )

def embed_builder(title, description, fields = None, color = discord.Color.yellow()):
    embed = discord.Embed(
        title=title,
        description=description,
        color=color,
    )
    if fields:
        for field in fields:
            embed.add_field(name=field.name, value=field.description)
    return embed
