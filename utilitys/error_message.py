import discord

def error_message(description: str):
    return discord.Embed(
        title="Error!",
        description=description,
        color=discord.Color.red(),
    )
