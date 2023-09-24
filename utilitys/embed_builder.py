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
    embed.set_footer(text=f"Pollen - Lightweight Discordbot",icon_url="https://cdn.discordapp.com/app-icons/1145021802083528735/56c74d987e6d5240adc7549e6a1fc86c.png?size=256&quot")
    return embed
