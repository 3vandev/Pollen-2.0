import discord
import os
from .close_ticket import close_ticket
from utilitys.embed_builder import embed_builder
from importlib.machinery import SourceFileLoader

class create_ticket(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None
     
    @discord.ui.button(label="Create Ticket", style=discord.ButtonStyle.gray, custom_id="POLLEN-TICKET-CREATE",emoji="🎫")
    async def ticket_create(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = await interaction.guild.create_text_channel(f"ticket-{interaction.user.name}")
        await channel.set_permissions(interaction.guild.default_role, read_messages=False, send_messages=False, view_channel=False)
        await channel.set_permissions(interaction.user, read_messages=True, send_messages=True)

        await channel.send(embed=embed_builder(f"{interaction.user.name}'s Ticket", "Moderators will be with you shortly please be patient"), view=close_ticket())
