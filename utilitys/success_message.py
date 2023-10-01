import discord

def success_message(description: str):
    return discord.Embed(
        title="Success!",
        description=description,
        color=discord.Color.green(),
    )
