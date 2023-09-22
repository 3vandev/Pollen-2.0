import discord
import os
from .delete_ticket import delete_ticket
from utilitys.embed_builder import embed_builder


class close_ticket(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=70000)
        self.value = None
     
    @discord.ui.button(label="Close", style=discord.ButtonStyle.red)
    async def ticket_create(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.channel.set_permissions(interaction.user, read_messages=False, send_messages=False, view_channel=False)
        await interaction.channel.send(embed=embed_builder("Ticket", f"This ticket was closed by {interaction.user.name} and has now been archived"), view=delete_ticket())
