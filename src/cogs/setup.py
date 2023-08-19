import nextcord
from nextcord.ext import commands
import database.database as database
import sqlite3

class SetupCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @nextcord.slash_command(name="setup_channel", description="Setup Channel ID")
    async def add_channel(self, interaction: nextcord.Interaction, channel: nextcord.TextChannel):
        guild_id = interaction.guild.id
        if channel.id or guild_id in database.fetch_channel_ids():
            await interaction.response.send_message(f"You have already setup a cross-chat channel, use command /check_cross_chat_channel", ephemeral=True)
        else:
            database.add_channel_id(channel.id, guild_id)
            await interaction.response.send_message(f"You have added <#{channel.id}> as your advertising channel", ephemeral=True)
    
    @nextcord.slash_command(name="remove_channel", description="Remove Channel ID")
    async def remove_channel(self, interaction: nextcord.Interaction, channel: nextcord.TextChannel):
        await interaction.response.send_message(f"You have removed <#{channel.id}> as your advertising channel", ephemeral=True)
        database.remove_channel_id(channel.id)
        
    @nextcord.slash_command(name="check_cross_chat_channel", description="Check cross-chat channel")
    async def check_channel(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(f"Your cross-chat channel is <#{database.fetch_channel_ids()}>", ephemeral=True)

def setup(bot):
    bot.add_cog(SetupCog(bot))