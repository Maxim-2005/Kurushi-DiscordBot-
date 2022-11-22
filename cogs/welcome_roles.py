import nextcord
from nextcord.ext import commands


class WelcomeRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: nextcord.Member):
        WELCOME_ROLES_IDS = [732500295669645343, 996179038689312769, 996180216328224788]
        for role_id in WELCOME_ROLES_IDS:
            role = member.guild.get_role(role_id)
            await member.add_roles(role)


def setup(bot):
    bot.add_cog(WelcomeRoles(bot))
    print('Module WelcomeRoles successfully loaded')