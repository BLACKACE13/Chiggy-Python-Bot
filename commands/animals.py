import discord
from discord.ext import commands
import animalapi as a


class Animals(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.bot_has_guild_permissions(send_messages=True)
    @commands.command()
    async def bird(self, ctx):
        if str(ctx.message.channel.type) == "private":
            return

        response = a.animal_data("bird")
        fact = response.get("fact")
        if "image" in ctx.message.content:
            embed = discord.Embed(title="🕊️ Chirrup 🕊️", colour=discord.Colour.random())
            embed.set_image(url=response.get("image"))
        elif "fact" in ctx.message.content:
            embed = discord.Embed(
                title="🕊️ Chirrup 🕊️",
                description=f"**Fact** - {fact}",
                colour=discord.Colour.random(),
            )
        else:
            embed = discord.Embed(
                title="🕊️ Chirrup 🕊️",
                description=f"**Fact** - {fact}",
                colour=discord.Colour.random(),
            )
            embed.set_image(url=response.get("image"))

        await ctx.channel.send(embed=embed)

    @commands.bot_has_guild_permissions(send_messages=True)
    @commands.command()
    async def cat(self, ctx):
        if str(ctx.message.channel.type) == "private":
            return

        response = a.animal_data("cat")
        fact = response.get("fact")
        if "image" in ctx.message.content:
            embed = discord.Embed(title="🐈 Meow 🐈", colour=discord.Colour.random())
            embed.set_image(url=response.get("image"))

        elif "fact" in ctx.message.content:
            embed = discord.Embed(
                title="🐈 Meow 🐈",
                description=f"**Fact** - {fact}",
                colour=discord.Colour.random(),
            )

        else:
            embed = discord.Embed(
                title="🐈 Meow 🐈",
                description=f"**Fact** - {fact}",
                colour=discord.Colour.random(),
            )
            embed.set_image(url=response.get("image"))
        await ctx.channel.send(embed=embed)

    @commands.bot_has_guild_permissions(send_messages=True)
    @commands.command()
    async def dog(self, ctx):
        if str(ctx.message.channel.type) == "private":
            return

        response = a.animal_data("dog")
        fact = response.get("fact")
        if "image" in ctx.message.content:
            embed = discord.Embed(title="🐩 Ruff 🐩", colour=discord.Colour.random())
            embed.set_image(url=response.get("image"))

        elif "fact" in ctx.message.content:
            embed = discord.Embed(
                title="🐩 Ruff 🐩",
                description=f"**Fact** - {fact}",
                colour=discord.Colour.random(),
            )

        else:
            embed = discord.Embed(
                title="🐩 Ruff 🐩",
                description=f"**Fact** - {fact}",
                colour=discord.Colour.random(),
            )
            embed.set_image(url=response.get("image"))
        await ctx.channel.send(embed=embed)

    @commands.bot_has_guild_permissions(send_messages=True)
    @commands.command()
    async def fox(self, ctx):
        if str(ctx.message.channel.type) == "private":
            return

        response = a.animal_data("fox")
        fact = response.get("fact")
        if "image" in ctx.message.content:
            embed = discord.Embed(title="🦊 Waoool 🦊", colour=discord.Colour.random())
            embed.set_image(url=response.get("image"))

        elif "fact" in ctx.message.content:
            embed = discord.Embed(
                title="🦊 Waoool 🦊",
                description=f"**Fact** - {fact}",
                colour=discord.Colour.random(),
            )

        else:
            embed = discord.Embed(
                title="🦊 Waoool 🦊",
                description=f"**Fact** - {fact}",
                colour=discord.Colour.random(),
            )
            embed.set_image(url=response.get("image"))
        await ctx.channel.send(embed=embed)

    @commands.bot_has_guild_permissions(send_messages=True)
    @commands.command()
    async def kangaroo(self, ctx):
        if str(ctx.message.channel.type) == "private":
            return

        response = a.animal_data("kangaroo")
        fact = response.get("fact")
        if "image" in ctx.message.content:
            embed = discord.Embed(title="🦘 Hopp 🦘", colour=discord.Colour.random())
            embed.set_image(url=response.get("image"))
        elif "fact" in ctx.message.content:
            embed = discord.Embed(
                title="🦘 Hopp 🦘",
                description=f"**Fact** - {fact}",
                colour=discord.Colour.random(),
            )
        else:
            embed = discord.Embed(
                title="🦘 Hopp 🦘",
                description=f"**Fact** - {fact}",
                colour=discord.Colour.random(),
            )
            embed.set_image(url=response.get("image"))

        await ctx.channel.send(embed=embed)

    @commands.bot_has_guild_permissions(send_messages=True)
    @commands.command()
    async def koala(self, ctx):
        if str(ctx.message.channel.type) == "private":
            return

        response = a.animal_data("koala")
        fact = response.get("fact")
        if "image" in ctx.message.content:
            embed = discord.Embed(title="🐨 Hurr 🐨", colour=discord.Colour.random())
            embed.set_image(url=response.get("image"))
        elif "fact" in ctx.message.content:
            embed = discord.Embed(
                title="🐨 Hurr 🐨",
                description=f"**Fact** - {fact}",
                colour=discord.Colour.random(),
            )
        else:
            embed = discord.Embed(
                title="🐨 Hurr 🐨",
                description=f"**Fact** - {fact}",
                colour=discord.Colour.random(),
            )
            embed.set_image(url=response.get("image"))
        await ctx.channel.send(embed=embed)

    @commands.bot_has_guild_permissions(send_messages=True)
    @commands.command()
    async def panda(self, ctx):
        if str(ctx.message.channel.type) == "private":
            return

        response = a.animal_data("panda")
        fact = response.get("fact")
        if "image" in ctx.message.content:
            embed = discord.Embed(title="🐼 Huff 🐼", colour=discord.Colour.random())
            embed.set_image(url=response.get("image"))
        elif "fact" in ctx.message.content:
            embed = discord.Embed(
                title="🐼 Huff 🐼",
                description=f"**Fact** - {fact}",
                colour=discord.Colour.random(),
            )
        else:
            embed = discord.Embed(
                title="🐼 Huff 🐼",
                description=f"**Fact** - {fact}",
                colour=discord.Colour.random(),
            )
            embed.set_image(url=response.get("image"))
        await ctx.channel.send(embed=embed)

    @commands.bot_has_guild_permissions(send_messages=True)
    @commands.command()
    async def raccoon(self, ctx):
        if str(ctx.message.channel.type) == "private":
            return

        response = a.animal_data("raccoon")
        fact = response.get("fact")
        if "image" in ctx.message.content:
            embed = discord.Embed(title="🦝 Burrr 🦝", colour=discord.Colour.random())
            embed.set_image(url=response.get("image"))
        elif "fact" in ctx.message.content:
            embed = discord.Embed(
                title="🦝 Burrr 🦝",
                description=f"**Fact** - {fact}",
                colour=discord.Colour.random(),
            )
        else:
            embed = discord.Embed(
                title="🦝 Burrr 🦝",
                description=f"**Fact** - {fact}",
                colour=discord.Colour.random(),
            )
            embed.set_image(url=response.get("image"))

        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Animals(bot))
