from discord.ext import commands
import random

# import libs here


class FunStuff:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def flip(self, ctx):
        x = random.choice(['Heads', 'Tails'])
        await ctx.send(x)

    @commands.command()
    async def magic8ball(self, ctx):
        my_response = [
            ":8ball: It is certain ",
            ":8ball: It is decidedly so ",
            ":8ball: Without a doubt ",
            ":8ball: Yes, definitely ",
            ":8ball: You may rely on it ",
            ":8ball: As I see it, yes ",
            ":8ball: Most likely ",
            ":8ball: Outlook good ",
            ":8ball: Yes ",
            ":8ball: Signs point to yes ",
            ":8ball: Reply hazy try again ",
            ":8ball: Ask again later ",
            ":8ball: Better not tell you now ",
            ":8ball: Cannot predict now ",
            ":8ball: Concentrate and ask again ",
            ":8ball: Don't count on it ",
            ":8ball: My reply is no",
            ":8ball: My sources say no ",
            ":8ball: Outlook not so good ",
            ":8ball: Very doubtful :"
        ]
        x = random.choice(my_response)
        await ctx.send(x)

    @commands.command()
    async def rps(self, ctx, c):
        try:
            ans = random.choice(['Rock', 'Paper', 'Scissor'])
            # rock
            if c in ['rock', 'r', 'Rock', 'R'] and ans == 'Rock':
                await ctx.send('Bot says Rock, Its a tie ')
            elif c in ['Paper', 'paper', 'p', 'P'] and ans == 'Rock':
                await ctx.send('Bot says Rock, You win :) ')
            elif c in ['Scissor', 'scissor', 's', 'S'] and ans == 'Rock':
                await ctx.send('Bot says Rock, You loose :( ')
            # paper
            elif c in ['rock', 'r', 'Rock', 'R'] and ans == 'Paper':
                await ctx.send('Bot says Paper, You lose :( ')
            elif c in ['Paper', 'paper', 'p', 'P'] and ans == 'Paper':
                await ctx.send('Bot says Paper, Its a tie ')
            elif c in ['Scissor', 'scissor', 's', 'S'] and ans == 'Paper':
                await ctx.send('Bot says Paper, You win :) ')
            # scissor
            elif c in ['rock', 'r', 'Rock', 'R'] and ans == 'Scissor':
                await ctx.send('Bot says Scissor, You win :) ')
            elif c in ['Paper', 'paper', 'p', 'P'] and ans == 'Scissor':
                await ctx.send('Bot says Scissor, You lose :( ')
            elif c in ['Scissor', 'scissor', 's', 'S'] and ans == 'Scissor':
                await ctx.send('Bot says Scissor, Its a tie ')
        except:
            await ctx.send('Please enter your answer')


def setup(bot):
    bot.add_cog(FunStuff(bot))
    # add this cog in main.py as well in the cogs list as the file name
