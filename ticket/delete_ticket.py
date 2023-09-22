import discord
import os
from utilitys.embed_builder import embed_builder

class delete_ticket(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=70000)
        self.value = None
     
    @discord.ui.button(label="Delete", style=discord.ButtonStyle.red)
    async def ticket_create(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.channel.send(embed=embed_builder("Ticket", "This ticket has been deleted in 5 seconds"))
        await interaction.channel.delete()
