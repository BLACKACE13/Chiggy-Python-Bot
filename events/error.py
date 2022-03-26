from discord.ext import commands
import discord


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        channel = self.bot.get_channel(920782396507439137)
        if isinstance(error, commands.BotMissingPermissions):
            k = "\n".join(error.missing_perms)
            if "send_messages" in k:
                try:
                    await channel.author.send(
                        embed=discord.Embed(
                            title="<a:error:920690594697867294> Error Occurered",
                            description=f"I do not have the permissions to execute that command.\n__Missing Perms__\n{k}",
                            color=discord.Color.red(),
                        ),
                        delete_after=45,
                    )
                except:
                    return

            if "send_messages" not in k:
                try:
                    await ctx.channel.send(
                        embed=discord.Embed(
                            title="<a:error:920690594697867294> Error Occurered",
                            description=f"I do not have the permissions to execute that command.\n__Missing Perms__\n{k}",
                            color=discord.Color.red(),
                        ),
                        delete_after=45,
                    )
                except:
                    return

        if isinstance(error, commands.MissingPermissions):
            k = "\n".join(error.missing_perms)
            try:
                await ctx.channel.send(
                    embed=discord.Embed(
                        title="<a:error:920690594697867294> Error Occurered",
                        description=f"You do not have the permissions to execute that command.\n__Missing Perms__\n{k}",
                        color=discord.Color.red(),
                    ),
                    delete_after=45,
                )
            except:
                return

        if isinstance(error, commands.MissingRequiredArgument):
            try:
                await ctx.send(
                    embed=discord.Embed(
                        title="<a:error:920690594697867294> Error Occurered",
                        description=error,
                        color=discord.Color.red(),
                    ),
                    delete_after=10,
                )
            except:
                return
        if isinstance(error, commands.CommandInvokeError):
            if "missing permissions" in str(error).lower():
                try:
                    await ctx.author.send(
                        embed=discord.Embed(
                            title="<a:error:920690594697867294> Error Occurered",
                            description=f"**Missing Access**\nin Guild:- `{ctx.guild.name}`",
                            color=discord.Color.red(),
                        )
                    )
                except:
                    return
            else:
                try:
                    link = await ctx.channel.create_invite(max_age=300)
                except:
                    link = None
                embed = discord.Embed(
                    title="<a:error:920690594697867294> Error Occurered",
                    description=f"> **{error}**\n\n **__Guild Details__**\nName:- `{ctx.guild.name}`\nGuild Id:- `{ctx.guild.id}`\nOwner Name:- `{ctx.guild.owner.name}#{ctx.guild.owner.discriminator}`\nOwner Id:- `{ctx.guild.owner.id}`\n**[Server Link]({link})**",
                    color=discord.Color.red(),
                    timestamp=ctx.message.created_at,
                )
                embed.set_footer(
                    text=f"Command was executed by {ctx.author.name}",
                    icon_url=ctx.author.avatar_url,
                )
                await channel.send(embed=embed)

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(
                f"⏱️ **|** Hold up **{ctx.author.name}**.Please try after **{error.retry_after:.2f}s**",
                delete_after=error.retry_after,
            )
        if isinstance(error, commands.BadArgument):
            await ctx.send(
                embed=discord.Embed(
                    title="<a:error:920690594697867294> Error Occurered",
                    description=error,
                    color=discord.Color.red(),
                ),
                delete_after=10,
            )
       


def setup(bot):
    bot.add_cog(Events(bot))
