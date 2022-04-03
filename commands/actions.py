import discord ,random
from discord.ext import commands
import json


class Actions(commands.Cog):
    def __init__(self, bot):
        with open(r"./resources/gifs.json") as f:
            gif_data = json.load(f)
        self.bot = bot
        self.gif_data = gif_data


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.bot_has_guild_permissions(send_messages=True)
    async def hug(self, ctx, target: commands.MemberConverter = None):
        hug_list = self.gif_data.get("hug")
        img = random.choice(hug_list)

        embed = discord.Embed(title="Hug <:cute_hug:868020279375462431>  ", colour=discord.Colour.random())
        embed.set_image(url=img)
        
        await ctx.reply(embed=embed)



def setup(bot):
    bot.add_cog(Actions(bot))
