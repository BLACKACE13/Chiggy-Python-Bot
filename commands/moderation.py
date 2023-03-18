import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.bot_has_guild_permissions(send_messages=True)
    @commands.cooldown(1, 30, commands.BucketType.user)
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        name = member.nick or member.name

        await member.ban(reason=reason)
        await ctx.channel.send(f"{name} has been banned.")

    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.bot_has_guild_permissions(manage_messages=True, send_messages=True)
    @commands.command(aliases=["purge"])
    async def clear(self, ctx, amount=5):
        deleted_count = 0
        channel = ctx.message.channel

        if amount > 1000:
            raise commands.BadArgument(
                f" <:ahemahem:876323457112100914> Hey!! **|** **{ctx.author.name}** Sorry but you can't make me delete that amount of messages at once."
            )
        if amount <= 100:
            await ctx.message.delete()
            await ctx.channel.purge(limit=amount)
            deleted_count = amount
        elif amount > 100:
            await ctx.message.delete()
            while amount > 100:
                await channel.purge(limit=100)
                deleted_count = deleted_count + 100
                amount = amount - 100
            if amount <= 100:
                await channel.purge(limit=amount)
                deleted_count = deleted_count + amount
                amount = 0
        await channel.send(
            f"Successfully deleted {deleted_count} messages", delete_after=5
        )

    @commands.command(aliases=["nikal"])
    @commands.cooldown(1, 30, commands.BucketType.user)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        name = member.nick
        if member.nick == None:
            name = member.name
        await ctx.channel.send(f"{name} has been kicked.")

    @commands.bot_has_guild_permissions(send_messages=True)
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedrole = discord.utils.get(guild.roles, name="Muted")

        if not mutedrole:
            mutedrole = await guild.create_role(
                name="Muted", colour=discord.Colour.light_grey()
            )

            for channel in guild.channels:
                await channel.set_permissions(
                    mutedrole,
                    speak=False,
                    send_messages=False,
                    read_message_history=None,
                    read_messages=None,
                )

        await member.add_roles(mutedrole, reason=reason)
        if reason == None:
            await ctx.send(f"Muted {member.mention}")
        else:
            await ctx.send(f"Muted {member.mention} \nReason: {reason}")

    @commands.bot_has_guild_permissions(send_messages=True)
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.has_permissions(manage_permissions=True)
    async def unmute(self, ctx, member: discord.Member):
        mutedrole = discord.utils.get(ctx.guild.roles, name="Muted")

        await member.remove_roles(mutedrole)
        await ctx.send(f"Unmuted {member.mention}")


def setup(bot):
    bot.add_cog(Moderation(bot))
