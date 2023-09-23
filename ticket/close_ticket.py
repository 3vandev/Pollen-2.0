import discord
import os
from .delete_ticket import delete_ticket
from utilitys.embed_builder import embed_builder

class close_ticket(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None
     
    # This button closes the ticket and archives it
    @discord.ui.button(label="Close", style=discord.ButtonStyle.red, custom_id="POLLEN-TICKET-CLOSE", emoji="⛔")
    async def ticket_create(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Remove user's permissions to read, send messages, and view the channel
        await interaction.channel.set_permissions(interaction.user, read_messages=False, send_messages=False, view_channel=False)
        # Edit the channel name to indicate it's been closed and archived
        await interaction.channel.edit(name=f"closed-{interaction.channel.name}-PLN-ARCHIVE")
        # Delete the message that triggered the interaction
        await interaction.message.delete()
        # Send a message indicating the ticket has been closed and archived, with a delete button
        await interaction.channel.send(embed=embed_builder("Ticket", f"This ticket was closed by {interaction.user.name} and has now been archived"), view=delete_ticket())
