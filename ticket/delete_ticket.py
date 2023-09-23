import discord
import os
from utilitys.embed_builder import embed_builder

class delete_ticket(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None
     
    # Define a button with label "Delete", red color, custom ID "POLLEN-TICKET-DELETE", and trash can emoji
    @discord.ui.button(label="Delete", style=discord.ButtonStyle.red, custom_id="POLLEN-TICKET-DELETE", emoji="🗑️")
    async def ticket_create(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Send a message to the channel where the interaction occurred with an embed that says the ticket has been deleted
        await interaction.channel.send(embed=embed_builder("Ticket", "This ticket has been deleted in 5 seconds"))
        # Delete the channel where the interaction occurred after 5 seconds
        await interaction.channel.delete()

