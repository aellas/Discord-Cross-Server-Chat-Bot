import nextcord
from nextcord.ext import commands
import database.database as database

NextcordComponents = nextcord.components

class AdvertisingCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.user_warnings = {}  

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        if message.author.id in self.user_warnings and self.user_warnings[message.author.id] >= 5:
            return
        
        channel_ids = database.fetch_channel_ids()
        if message.channel.id in channel_ids:
            print("Message received: " + str(message.content))

            swear_words = ["swear_word1", "swear_word2"]
            mentioned_roles = ["@everyone", "@here"]

            if any(word in message.content.lower() for word in swear_words) or any(role in message.content for role in mentioned_roles):
                await message.channel.send("Warning: Detected swearing or role mention")
                self.user_warnings[message.author.id] = self.user_warnings.get(message.author.id, 0) + 1
                if self.user_warnings[message.author.id] >= 5:
                    await message.user.send("You have been warned 5 times. You will be kicked from the server.")
            else:
                embed = nextcord.Embed(description=f"📨 Sent to **{len(channel_ids)}** servers", color=0xffffff)
                await message.channel.send(embed=embed)
                for channel_id in channel_ids:
                    if channel_id != message.channel.id:
                        channel = self.bot.get_channel(channel_id)
                        if channel:
                            await channel.send(f"`📩` {message.content}")
                            embed = nextcord.Embed(description=f"Sent by **{message.author.name}** from **{message.guild.name}** ", color=0xffffff)
                            await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(AdvertisingCog(bot))
