from discord.ext import commands
import utils.messageprocessor as messageprocessor
from database import checks


class Messages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if str(message.channel.type) == "private" or message.author.bot:
            return
        await messageprocessor.react(self.bot, message)
        await checks.user_check_cash(message.author.id)
        if "chiggy-ai" in message.channel.name:
            await messageprocessor.react(self.bot, message)


def setup(bot):
    bot.add_cog(Messages(bot))
