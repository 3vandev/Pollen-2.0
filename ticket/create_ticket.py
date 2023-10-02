import discord
import os
from .close_ticket import close_ticket
from utilitys.embed_builder import embed_builder
from discord.interactions import Interaction
from discord import ui

class create(ui.Modal, title="Open a ticket"):
    reason = ui.TextInput(
        label="Whats your reason for opening a ticket?",
        style=discord.TextStyle.long,
        placeholder="Reason",
        required=True,
    )

    async def on_submit(self, interaction: Interaction):
        # create a new text channel with the name "ticket-{user's name}"
        channel = await interaction.guild.create_text_channel(f"ticket-{interaction.user.name}")
        
        # set permissions for the default role (everyone) to not be able to read, send messages, or view the channel
        await channel.set_permissions(interaction.guild.default_role, read_messages=False, send_messages=False, view_channel=False)
        
        # set permissions for the user who created the ticket to be able to read and send messages in the channel
        await channel.set_permissions(interaction.user, read_messages=True, send_messages=True)

        # send an embed message to the channel with the user's name and a message for them to be patient
        # also include the close_ticket view to allow the user to close the ticket
        embed = discord.Embed(description=f"**Reason:**\n{self.reason}\n\nModerators will be with you shortly please be patient",colour=discord.Colour.green())
        embed.set_author(name=f"Ticket: {interaction.user.name}",icon_url=interaction.user.avatar.url)
        await channel.send(embed=embed,view=close_ticket())

        await interaction.response.send_message(embed=embed_builder("Success", f"Ticket created <#{channel.id}>\n\n**Reason**\n{self.reason}"), ephemeral=True)

class create_ticket(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None
     
    @discord.ui.button(label="Create Ticket", style=discord.ButtonStyle.gray, custom_id="POLLEN-TICKET-CREATE",emoji="🎫")
    async def ticket_create(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(create())
