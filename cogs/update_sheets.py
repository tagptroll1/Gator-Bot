from discord.ext import commands
import humanify
import datetime
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
    async def ustatus(self, ctx, *, info):

        gc.login()
        if admin_ids[0] or admin_ids[1] or admin_ids[2] in [role.id for role in ctx.message.author.roles]:
            wks = gc.open('Gator_Recruits_(was Cobras)').sheet1
            ign, new_status = info.split('-')
            x = wks.find(ign).row
            val = wks.cell(x, 3).value
            wks.update_cell(x, 3, str(new_status))
            await ctx.send("Status has been updated from " + val + " to " + new_status)
        else:
            await ctx.send("You do not have permission to use this command !")

    @commands.command()
    async def udd(self, ctx, info):
        gc.login()
        if admin_ids[0] or admin_ids[1] or admin_ids[2] in [role.id for role in ctx.message.author.roles]:
            ign, d = info.split('-')
            wks = gc.open('Gator_Recruits_(was Cobras)').sheet1
            x = wks.find(ign).row
            if d[1] == 'n' or 'N':
                current_time = datetime.datetime.now()
                wks.update_cell(x, 4, str(humanify.datetime(current_time)))
            else:
                wks.update_cell(x, 4, str(d))
        else:
            await ctx.send("You do not have permission to use this command !")

    @commands.command()
    async def uw1(self, ctx, info):
        gc.login()
        if admin_ids[0] or admin_ids[1] or admin_ids[2] in [role.id for role in ctx.message.author.roles]:
            ign, w1 = info.split('-')
            wks = gc.open('Gator_Recruits_(was Cobras)').sheet1
            x = wks.find(ign).row
            wks.update_cell(x, 10, str(w1))
        else:
            await ctx.send("You do not have permission to use this command !")

    @commands.command()
    async def uw2(self, ctx, info):
        gc.login()
        if admin_ids[0] or admin_ids[1] or admin_ids[2] in [role.id for role in ctx.message.author.roles]:
            ign, w2 = info.split('-')
            wks = gc.open('Gator_Recruits_(was Cobras)').sheet1
            x = wks.find(ign).row
            wks.update_cell(x, 11, str(w2))
        else:
            await ctx.send("You do not have permission to use this command !")


def setup(bot):
    bot.add_cog(RecruitmentSheets(bot))
