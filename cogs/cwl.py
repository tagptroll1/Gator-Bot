from discord.ext import commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('cogs/gator-project-2-7460b2795c66.json', scope)
gc = gspread.authorize(credentials)


class CwlRegistration:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cwl(self, ctx, *, info_for_cwl):

        await ctx.send(f"{ctx.author} Registration for cwl is closed ! Come back for the next cwl !")
        """
        gc.login()
        # print(info_for_cwl)
        try:
            wks_cwl = gc.open('cwl_roster').sheet1
            ign, th, yon, notes = info_for_cwl.split('-')
            wks_cwl.append_row([ign, th, yon, notes])
            await ctx.send('Your append was successful !')
        except Exception as e:
            await ctx.send('An error ' + str(e) + 'has occured !')
        """
    @commands.command()
    async def cwlinfo(self, ctx, *, ign):
        gc.login()
        try:

            wks_cwl = gc.open('cwl_roster').sheet1
            x = wks_cwl.find(str(ign)).row
            headings = wks_cwl.row_values(1)

            row_vals = wks_cwl.row_values(x)
            for f, b in zip(headings, row_vals):
                msg = '***' + f + '***' + ':' + b
                await ctx.send(msg)
        except:
            await ctx.send(ign + ' was not found !')

    @commands.commad()
    async def ret(self, ctx, *, ign):
        # a command to retain a player in the cwl sheets if he wants to participate in the next cwl also
        gc.login()
        try:
            pass
        except Exception as e:
            pass


def setup(bot):
    bot.add_cog(CwlRegistration(bot))
