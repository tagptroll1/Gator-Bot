import discord
from discord.ext import commands
import humanify
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('cogs/gator-project-e3b46f8efea9.json', scope)
gc = gspread.authorize(credentials)

admin_ids = ['255409211385708546', '255403079669645312', '255419757895876608']


class RecruitmentSheets:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(self, ctx, user: discord.Member, info_about_new_member):
        gc.open()
        try:
            if admin_ids[0] or admin_ids[1] or admin_ids[2] in [role.id for role in ctx.message.author.roles]:
                wks = gc.open('Gator_Recruits_(was Cobras)').sheet1
                ign, th, tag, age, location = info_about_new_member.split('-')
                wks.append_row(
                    [str(humanify.datetime(user.joined_at)), ign, 'Trials',
                     '#', user.name + '#' + user.discriminator, tag, th, age,
                     location, '#', '#'])
                await ctx.send('Your Append was successful !')
            else:
                await ctx.send('You dont have permission to use this command !')
        except Exception as e:
            await ctx.send('An error ' + str(e) + 'has occured !')

    @commands.command()
    async def info(self, ctx, *, ign):
        gc.open()
        try:
            if admin_ids[0] or admin_ids[1] or admin_ids[2] in [role.id for role in ctx.message.author.roles]:
                wks = gc.open('Gator_Recruits_(was Cobras)').sheet1
                x = wks.find(ign).row
                headings = wks.row_values(1)

                row_vals = wks.row_values(x)
                for f, b in zip(headings, row_vals):
                    # msg = '***' + f + '***' + ':' + b
                    info = discord.Embed(
                        title=f'Info about {ign}',
                        description='***' + f + '***' + ':' + b,
                        color=0x7cfc00
                    )
                    # msg = '***' + f + '***' + ':' + b
                    await ctx.send(embed=info)
            else:
                await ctx.send('You dont have permission to use this command !')
        except Exception as e:
            await ctx.send('An error ' + str(e) + 'has occured !')

    """@info.error
    async def info_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.invoke(self.info, member = ctx.author)
            logging.info('sent info about the author : commads.MissingRequiredArgument')
    """


def setup(bot):
    bot.add_cog(RecruitmentSheets(bot))
