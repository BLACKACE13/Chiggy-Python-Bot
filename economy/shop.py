import discord, json
from discord.ext import commands
from discord.ext.commands import BucketType


class Shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.shop_data = json.load(open(r"./resources/shop.json"))

    @commands.group(name="shop", aliases=["market"], invoke_without_command=True)
    @commands.cooldown(1, 5, BucketType.user)
    async def market(self, ctx):
        prefix = await self.bot.get_prefix(ctx.message)

        embed = discord.Embed(
            timestamp=ctx.message.created_at,
            title="Market Categories",
            color=ctx.author.color,
        )

        for category in self.shop_data:
            embed.add_field(
                name=f"__{category.upper()}__",
                value=f'{self.shop_data[category]["description"]}',
                inline=False,
            )

        embed.set_footer(
            text=f"To see the list of items in each category {prefix[2]}shop <category>",
            icon_url=ctx.author.avatar_url,
        )

        await ctx.send(embed=embed)

    @market.command(name="food")
    @commands.cooldown(1, 5, BucketType.user)
    async def food(self, ctx, args=None):
        if args and args.lower() in self.shop_data["food"]["items"]:
            owned = 0
            title = f"__{args.title()}__"

            des = (
                self.shop_data["food"]["items"][args.lower()]["description"]
                or "This is a magistic item and the data is unknown"
            )
            cost = self.shop_data["food"]["items"][args.lower()]["cost"]
            img = self.shop_data["food"]["items"][args.lower()]["image"]

            itemembed = discord.Embed(
                timestamp=ctx.message.created_at,
                title=title,
                color=ctx.author.color,
                description=f"**Info: -** {des}\n**Cost: -** `{cost}` <:chigs:973011363041517598>\n**Owned: -** {owned}",
            )

            itemembed.set_thumbnail(url=img)
            itemembed.set_footer(
                text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url
            )

            return await ctx.channel.send(embed=itemembed)

        elif args:
            return await ctx.channel.send(
                "Well that item doesn't exist or is not in this category"
            )

        des = ""
        for items in self.shop_data["food"]["items"]:
            cost = self.shop_data["food"]["items"][items]["cost"]
            des = (
                des
                + f"**{items.upper()}** - `{cost}` <:chigs:973011363041517598>"
                + "\n"
            )

        embed = discord.Embed(
            timestamp=ctx.message.created_at,
            title="__Food__",
            color=ctx.author.color,
            description=des,
        )

        embed.set_footer(
            text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url
        )

        await ctx.send(embed=embed)

    @market.command(name="pets")
    @commands.cooldown(1, 5, BucketType.user)
    async def pets(self, ctx, args=None):
        if args and args.lower() in self.shop_data["pets"]["items"]:
            owned = 0
            title = f"__{args.title()}__"

            des = (
                self.shop_data["pets"]["items"][args.lower()]["description"]
                or "This is a magistic item and the data is unknown"
            )
            cost = self.shop_data["pets"]["items"][args.lower()]["cost"]
            img = self.shop_data["pets"]["items"][args.lower()]["image"]

            itemembed = discord.Embed(
                timestamp=ctx.message.created_at,
                title=title,
                color=ctx.author.color,
                description=f"**Info: -** {des}\n**Cost: -** `{cost}` <:chigs:973011363041517598>\n**Owned: -** {owned}",
            )

            itemembed.set_thumbnail(url=img)
            itemembed.set_footer(
                text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url
            )

            return await ctx.channel.send(embed=itemembed)

        elif args:

            return await ctx.channel.send(
                "Well that item doesn't exist or is not in this category"
            )

        des = ""

        for items in self.shop_data["pets"]["items"]:

            cost = self.shop_data["pets"]["items"][items]["cost"]
            des = (
                des
                + f"**{items.upper()}** - `{cost}` <:chigs:973011363041517598>"
                + "\n"
            )

        embed = discord.Embed(
            timestamp=ctx.message.created_at,
            title="__Pets__",
            color=ctx.author.color,
            description=des,
        )

        embed.set_footer(
            text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url
        )

        await ctx.send(embed=embed)

    @market.command(name="gadgets")
    @commands.cooldown(1, 5, BucketType.user)
    async def gadgets(self, ctx, args=None):
        if args and args.lower() in self.shop_data["gadgets"]["items"]:
            owned = 0
            title = f"__{args.title()}__"

            des = (
                self.shop_data["gadgets"]["items"][args.lower()]["description"]
                or "This is a magistic item and the data is unknown"
            )
            cost = self.shop_data["gadgets"]["items"][args.lower()]["cost"]
            img = self.shop_data["gadgets"]["items"][args.lower()]["image"]

            itemembed = discord.Embed(
                timestamp=ctx.message.created_at,
                title=title,
                color=ctx.author.color,
                description=f"**Info: -** {des}\n**Cost: -** `{cost}` <:chigs:973011363041517598>\n**Owned: -** {owned}",
            )

            itemembed.set_thumbnail(url=img)
            itemembed.set_footer(
                text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url
            )

            return await ctx.channel.send(embed=itemembed)

        elif args:
            return await ctx.channel.send(
                "Well that item doesn't exist or is not in this category"
            )

        des = ""

        for items in self.shop_data["gadgets"]["items"]:
            cost = self.shop_data["gadgets"]["items"][items]["cost"]
            des = (
                des
                + f"**{items.upper()}** - `{cost}` <:chigs:973011363041517598>"
                + "\n"
            )

        embed = discord.Embed(
            timestamp=ctx.message.created_at,
            title="__Gadgets__",
            color=ctx.author.color,
            description=des,
        )

        embed.set_footer(
            text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url
        )

        await ctx.send(embed=embed)

    @market.command(name="flowers")
    @commands.cooldown(1, 5, BucketType.user)
    async def flowers(self, ctx, args=None):
        if args and args.lower() in self.shop_data["flowers"]["items"]:
            owned = 0
            title = f"__{args.title()}__"

            des = (
                self.shop_data["flowers"]["items"][args.lower()]["description"]
                or "This is a magistic item and the data is unknown"
            )
            cost = self.shop_data["flowers"]["items"][args.lower()]["cost"]
            img = self.shop_data["flowers"]["items"][args.lower()]["image"]

            itemembed = discord.Embed(
                timestamp=ctx.message.created_at,
                title=title,
                color=ctx.author.color,
                description=f"**Info: -** {des}\n**Cost: -** `{cost}` <:chigs:973011363041517598>\n**Owned: -** {owned}",
            )

            itemembed.set_thumbnail(url=img)
            itemembed.set_footer(
                text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url
            )

            return await ctx.channel.send(embed=itemembed)

        elif args:
            return await ctx.channel.send(
                "Well that item doesn't exist or is not in this category"
            )

        des = ""

        for items in self.shop_data["flowers"]["items"]:
            cost = self.shop_data["flowers"]["items"][items]["cost"]
            des = (
                des
                + f"**{items.upper()}** - `{cost}` <:chigs:973011363041517598>"
                + "\n"
            )

        embed = discord.Embed(
            timestamp=ctx.message.created_at,
            title="__Flowers__",
            color=ctx.author.color,
            description=des,
        )

        embed.set_footer(
            text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url
        )

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Shop(bot))
