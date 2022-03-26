from discord import guild, Spotify
from discord.ext import commands
import discord
import json


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["av"])
    async def avatar(self, ctx, member: commands.MemberConverter = None):
        if str(ctx.message.channel.type) == "private":
            return
        if not member:
            member = ctx.message.author
        userAvatar = member.avatar_url

        embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
        embed.set_author(name=f"Avatar of {member.name}  Looking nice!!")
        embed.set_image(url=userAvatar)
        embed.set_footer(
            text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url
        )

        msg = await ctx.send(embed=embed)
        await msg.add_reaction("✨")

    @commands.command(aliases=["info"])
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def userinfo(self, ctx, *, user: discord.Member = None):
        if not user:
            user = ctx.author

        embed = discord.Embed(
            title=f"{user.name} [ID: {user.id}]",
            discription=f"Here's what info we retrieved about {user}",
            colour=user.colour,
            timestamp=ctx.message.created_at,
        )
        str1 = ""
        l = user.roles[::-1]
        for i in range(len(user.roles) - 1):
            str1 += " " + l[i].mention

        perms = " "
        if user.guild_permissions.administrator == True:
            perms += "Administrator" + " **|** "
        if user.guild_permissions.kick_members == True:
            perms += "Kick members" + " **|** "
        if user.guild_permissions.ban_members == True:
            perms += "Ban members" + " **|** "
        if user.guild_permissions.manage_channels == True:
            perms += "Manage channels" + " **|** "
        if user.guild_permissions.manage_messages == True:
            perms += "Manage messages" + " **|** "
        if user.guild_permissions.manage_nicknames == True:
            perms += "Manage nicknames" + " **|** "
        if user.guild_permissions.mention_everyone == True:
            perms += "Mention everyone" + " **|** "
        if user.guild_permissions.manage_roles == True:
            perms += "Manage roles" + " **|** "
        if user.guild_permissions.manage_emojis == True:
            perms += "Manage emojis" + " **|** "
        if user.guild_permissions.manage_webhooks == True:
            perms += "Manage webhooks" + " **|** "
        if user.guild_permissions.send_messages == True:
            perms += "Send messages" + " **|** "
        if perms == " ":
            perms = "None"

        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="__NICKNAME__", value=user.nick, inline=True)
        embed.add_field(
            name="__CREATED AT__",
            value=user.created_at.strftime("%a, %d %b %Y %H:%M:%S %p"),
            inline=True,
        )
        embed.add_field(
            name="__JOINED AT__",
            value=user.joined_at.strftime("%a, %d %b %Y %H:%M:%S %p"),
            inline=True,
        )
        embed.add_field(name="__STATUS__", value=user.status, inline=True)
        embed.add_field(name="__ROLES__", value=str1, inline=False)
        embed.add_field(
            name="__TOP ROLE__", value=f"<@&{user.top_role.id}>", inline=True
        )
        embed.add_field(name="__PERMISSIONS__", value=perms, inline=False)
        embed.set_footer(
            text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url
        )
        await ctx.send(embed=embed)

    @commands.bot_has_guild_permissions(send_messages=True)
    @commands.cooldown(1, 60, commands.BucketType.guild)
    @commands.command()
    async def prefix(self, ctx, *, prefix):

        with open(r"./resources/prefixes.json") as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix
        await ctx.send(f"Guild prefix set to '{prefix}' .")

        with open(r"./resources/prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)

    @commands.command(aliases=["calculate"])
    async def cal(self, ctx, *args):
        num = ""
        for i in args:
            num += i
        await ctx.send(eval(num))

    @commands.cooldown(1, 20, commands.BucketType.user)
    @commands.command(aliases=["guildinfo"])
    async def serverinfo(self, ctx):
        infoembed = discord.Embed(
            title="**SERVER INFO**",
            colour=ctx.author.colour,
            timestamp=ctx.message.created_at,
        )

        str1 = ""
        l = ctx.guild.roles[::-1]
        for i in range(len(ctx.guild.roles)):
            if (
                not l[i].is_bot_managed()
                and not l[i].is_default()
                and not l[i].is_premium_subscriber()
                and not l[i].is_integration()
            ):
                str1 += " " + l[i].mention

        infoembed.set_thumbnail(url=ctx.guild.icon_url)
        infoembed.add_field(name="__NAME__", value=ctx.guild.name, inline=True)
        infoembed.add_field(name="__ID__", value=ctx.guild.id, inline=True)
        infoembed.add_field(
            name="__CREATED AT__",
            value=ctx.guild.created_at.strftime("%a, %d %b %Y %H:%M:%S %p"),
            inline=False,
        )
        infoembed.add_field(
            name="__OWNER__",
            value=f"{ctx.guild.owner.mention}",
            inline=True,
        )
        infoembed.add_field(name="__ROLES__", value=str1, inline=False)
        infoembed.add_field(
            name="__MEMBER COUNT__", value=ctx.guild.member_count, inline=True
        )
        infoembed.set_footer(
            text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url
        )
        await ctx.send(embed=infoembed)

    @commands.command()
    async def spotify(self, ctx, user: discord.Member = None):

        user = user or ctx.author
        activity_list = []
        for activity in user.activities:
            activity_list.append(activity.name)
            if isinstance(activity, Spotify):
                seconds = activity.duration.seconds
                seconds_in_day = 60 * 60 * 24
                seconds_in_hour = 60 * 60
                seconds_in_minute = 60

                days = seconds // seconds_in_day
                hours = (seconds - (days * seconds_in_day)) // seconds_in_hour
                minutes = (
                    seconds - (days * seconds_in_day) - (hours * seconds_in_hour)
                ) // seconds_in_minute
                artist = activity.artist.replace(";", " |")
                des = f"Listening to:- **{activity.title}**\nArtist(s):- **{artist}**\nDuration:- {hours} hours {minutes} minutes {seconds- minutes*60} seconds"

                spotify_embed = discord.Embed(
                    colour=user.colour,
                    timestamp=ctx.message.created_at,
                    description=des,
                )
                spotify_embed.set_author(name=user.name, icon_url=user.avatar_url)
                spotify_embed.set_thumbnail(url=activity.album_cover_url)
                spotify_embed.set_footer(
                    text=f"Requested by {ctx.author.name}",
                    icon_url=ctx.author.avatar_url,
                )
                await ctx.send(embed=spotify_embed)
        if "Spotify" not in activity_list:
            await ctx.send(f"{user.name} is listening to actually umm nothing")


def setup(bot):
    bot.add_cog(Utility(bot))
