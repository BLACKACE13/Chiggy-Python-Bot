import discord , random
from discord.ext import commands
import asyncio
from database import checks ,functions

class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=["cf"])
    async def coinflip(self, ctx, *args):
        await checks.user_check_cash(ctx.author.id)
        bet = 1
        heads = ["h","heads","head","H"]
        tails = ["t","tail","tails","T"]
        if len(args) > 2:
            return await ctx.send(f"❗Invalid arguments **{ctx.author.name}**|Please include the betting amount and the choice[optional]. ")
        if args:
            for amt in args:
                if amt.isdigit():
                    bet = int(amt)
                    break
            for choi in args:
                if choi.lower() in tails:
                    choice = "Tails"
                elif choi.lower() in heads:
                    choice = "Head"
                else:
                    choice = random.choice(['Tails','Head'])
        else:
            choice = random.choice(['Tails','Head'])

        
        win_condition = random.choice(['Tails','Head'])
        win_amount = bet*2
       
        if bet < 1: await ctx.send(f"**{ctx.author.name}** you can't bet that...")
        else:
            if await functions.check_balance(ctx.author.id) <bet:
               await ctx.send(f"**{ctx.author.name}** you don't even have that much chigs... " )
            else: 
           
                message=await ctx.send(f"**{ctx.author.name}** spent {bet} <:chigs:937640062332571699> and chose {choice}\nThe coin spins... <a:cf:939070721504706572>")
                await asyncio.sleep(2)
                if choice==win_condition:
                   await message.edit(content=f"**{ctx.author.name}** spent {bet} <:chigs:937640062332571699> and chose {choice}\nThe coin spins...and you won {win_amount} <:chigs:937640062332571699> !! ")
                   await functions.add_balance(ctx.author.id,bet)
                   await functions.cash_postsyncer([ctx.author.id])
            
                if choice!=win_condition:
                   await message.edit(content=f"**{ctx.author.name}** spent {bet} <:chigs:937640062332571699> and chose {choice}\nThe coin spins...and you lost it...")
                   await functions.remove_balance(ctx.author.id,bet)
                   await functions.cash_postsyncer([ctx.author.id])



    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=["rd"])
    async def rolldice(self, ctx,bet_amount=1):
        await checks.user_check_cash(ctx.author.id)

        choice= random.choice([2,random.randint(1,6)])
        win_condition= random.choice([2,random.randint(1,6)])

        if bet_amount < 1: await ctx.send(f"**{ctx.author.name}** you can't bet that...")
        else: 
            
            message=await ctx.send(f"**{ctx.author.name}** spent {bet_amount} <:chigs:937640062332571699> and chose {choice}\nThe die rolls... ")
            await asyncio.sleep(2)
            if choice==win_condition:
                if choice in (1,2,3):
                    win_amount= bet_amount * 2
                elif choice in (4,5):
                    win_amount= bet_amount * 3
                elif choice in (6):
                    win_amount= bet_amount * 4
        
                await message.edit(content=f"**{ctx.author.name}** spent {bet_amount} <:chigs:937640062332571699> and chose {choice}\nCongoo <a:Yeeey:876323873069596712> {win_condition} turns up...and you won {win_amount} <:chigs:937640062332571699> !! ")
                await functions.add_balance(ctx.author.id,bet_amount)
            
            if choice!=win_condition:
                await message.edit(content=f"**{ctx.author.name}** spent {bet_amount} <:chigs:937640062332571699> and chose {choice}\nUmm unfortunately you lost...better luck next time.")
                await functions.remove_balance(ctx.author.id,bet_amount)


def setup(bot):
    bot.add_cog(Gamble(bot))
