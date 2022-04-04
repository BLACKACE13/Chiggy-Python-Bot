import discord , random
from discord.ext import commands
from database import checks ,functions
import os.path, json


class Bot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.bot_has_guild_permissions(send_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=['bal','balance'])
    async def cash(self, ctx ,user: discord.Member = None):
        if str(ctx.message.channel.type) == "private":
            return

        user = user or ctx.author
        uid = user.id

        await checks.user_check_cash(uid)
        cash = await functions.check_balance(str(uid))

        await ctx.reply(f"<:chigs:937640062332571699> **{user.name}** currently has **{cash:,}** chigs.")

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(name='give',aliases=['send'])
    async def sendchigs(self,ctx,cash,user:discord.Member= None):
        
        if cash.isdigit():
           cash = int(cash) 
           if cash is None or user is None : await ctx.send(f"❗Invalid arguments **{ctx.author.name}** |Please include cash and the user. ") 
           elif cash < 0: await ctx.send(f"**{ctx.author.name}** Well are you basically trying to rob **{user.name}** _tch tch_...")

           else:

            await checks.user_check_cash(ctx.author.id)
            if await functions.check_balance(ctx.author.id) < cash:
                 await ctx.send(f"**{ctx.author.name}** you cannot send that much chigs... " )

            else:
                await checks.user_check_cash(user.id)
                
                await functions.add_balance(user.id,cash)
                await functions.remove_balance(ctx.author.id,cash)
                 
                await ctx.send(f"**{ctx.author.name}** sent {cash} chigs <:chigs:937640062332571699> to **{user.name}**!")
                await functions.cash_postsyncer([user.id,ctx.author.id])
        else: 
            await ctx.send(f"❗Invalid arguments **{ctx.author.name}** |Please include cash and the user. ")


    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.command(name='beg')
    async def beg(self,ctx):

        await checks.user_check_cash(ctx.author.id)
        prob=random.choice(['yes', 'no','maybe'])

        if prob == 'yes':
            beg_amount=random.randint(50,350)
            phrases=[
            f'Oh poor! I have only {beg_amount} <:chigs:937640062332571699> to give.',
            f'You got {beg_amount} <:chigs:937640062332571699> from the strangers passing by.',
            f'What a pity! Here {beg_amount} <:chigs:937640062332571699> ...Hope it would help you a bit.',
            f'Here **{ctx.author.name}**, take {beg_amount} <:chigs:937640062332571699> ...have a great day! UwU'
            ]

            await ctx.reply(random.choice(phrases))
            await functions.add_balance(ctx.author.id,beg_amount)

        if prob != 'yes':
            phrases=[
            'Can you please stop begging everytime!',
            'You may just ask your friend to give you some chigs instead of begging.',
            'Ask me later, not in the mood now xD .'
            ]
            
            await ctx.reply(random.choice(phrases))
        await functions.cash_postsyncer([ctx.author.id])

    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.command(name='buy')
    async def buy(self,ctx,item,amount=1):
        await checks.user_check_inventory(ctx.author.id)
 
        await checks.user_check_cash(ctx.author.id)


        item_cost = json.load(open(r"./resources/itemcost.json"))
        
        if item.lower() in item_cost:
            cost= item_cost[item.lower()]
        
        price= amount*cost

        if await functions.check_balance(ctx.author.id) < price:
   
            await ctx.send(f"**{ctx.author.name}** you don't even have that much chigs... " )
        
        else:
            await functions.remove_balance(ctx.author.id,price)
            await functions.cash_postsyncer([ctx.author.id])         
            await functions.add_item(ctx.author.id,item,amount)
            await functions.inventory_postsyncer([str(ctx.author.id)])
   
            await ctx.send(f"**{ctx.author.name}** || purchased {amount} {item} for {price} <:chigs:937640062332571699>!" )

    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.command()
    async def inv(self, ctx):
        prefetcher_file = os.path.join(os.path.dirname(__file__), "../database/prefetch_data/inventory_cache.json")
        with open(prefetcher_file) as f:
            inventory_data = json.load(f)
        user_data = inventory_data[str(ctx.author.id)]
        inv = ""
        for item in user_data:
            if user_data[item] > 0:
                inv =  inv + item.title() +  ' - ' + str(user_data[item]) + "\n"

        embed = discord.Embed(
                title=f"{ctx.author.name}'s Inventory",
                description=f"{inv}",
                colour=ctx.author.colour,
            )

        await ctx.channel.send(embed = embed)


def setup(bot):
    bot.add_cog(Bot(bot))
