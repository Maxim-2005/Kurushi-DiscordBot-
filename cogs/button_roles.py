import nextcord
from nextcord.ext import commands


class RoleView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    async def role_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        role_id = int(button.custom_id.split(":")[-1])
        role = interaction.guild.get_role(role_id)
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            return await interaction.response.send_message(f"Роль `{role.name}` удалена", ephemeral=True, delete_after=3)

        await interaction.user.add_roles(role)
        await interaction.response.send_message(f"Роль `{role.name}` добавлена", ephemeral=True, delete_after=3)


class TestRoleView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(
        label="Brawlhalla",
        style=nextcord.ButtonStyle.secondary,
        custom_id="TestRoleView:901419971450634270",
    )
    async def brawlhalla_role_button(self, button, interaction):
        await RoleView.role_button(self, button, interaction)
    
    @nextcord.ui.button(
        label="Counter Strike 1.6",
        style=nextcord.ButtonStyle.secondary,
        custom_id="TestRoleView:1009081700539707452",
    )
    async def cs16_role_button(self, button, interaction):
        await RoleView.role_button(self, button, interaction)

    @nextcord.ui.button(
        label="Crystal clash",
        style=nextcord.ButtonStyle.secondary,
        custom_id="TestRoleView:932245965530882138",
    )
    async def crystalclash_role_button(self, button, interaction):
        await RoleView.role_button(self, button, interaction)
        
    @nextcord.ui.button(
        label="Dead by Daylight",
        style=nextcord.ButtonStyle.secondary,
        custom_id="TestRoleView:917830343757791242",
    )
    async def dbd_role_button(self, button, interaction):
        await RoleView.role_button(self, button, interaction)

    @nextcord.ui.button(
        label="Deceit",
        style=nextcord.ButtonStyle.secondary,
        custom_id="TestRoleView:1000844155800539166",
    )
    async def deceit_role_button(self, button, interaction):
        await RoleView.role_button(self, button, interaction)

    @nextcord.ui.button(
        label="Dota 2",
        style=nextcord.ButtonStyle.secondary,
        custom_id="TestRoleView:965121364098945064",
    )
    async def dota2_role_button(self, button, interaction):
        await RoleView.role_button(self, button, interaction)
    
    @nextcord.ui.button(
        label="Garry's mod",
        style=nextcord.ButtonStyle.secondary,
        custom_id="TestRoleView:932246223237296148",
    )
    async def gmod_role_button(self, button, interaction):
        await RoleView.role_button(self, button, interaction)

    @nextcord.ui.button(
        label="Gratic phone",
        style=nextcord.ButtonStyle.secondary,
        custom_id="TestRoleView:994924128094130216",
    )
    async def gratic_role_button(self, button, interaction):
        await RoleView.role_button(self, button, interaction)

    @nextcord.ui.button(
        label="Ghost Exile",
        style=nextcord.ButtonStyle.secondary,
        custom_id="TestRoleView:1006104191388897380",
    )
    async def ghostexile_role_button(self, button, interaction):
        await RoleView.role_button(self, button, interaction)

    @nextcord.ui.button(
        label="GPO",
        style=nextcord.ButtonStyle.secondary,
        custom_id="TestRoleView:980060987522682931",
    )
    async def gpo_role_button(self, button, interaction):
        await RoleView.role_button(self, button, interaction)

    @nextcord.ui.button(
        label="Gunfire Reborn",
        style=nextcord.ButtonStyle.secondary,
        custom_id="TestRoleView:980060916148232212",
    )
    async def gunfirereborn_role_button(self, button, interaction):
        await RoleView.role_button(self, button, interaction)

    @nextcord.ui.button(
        label="Haunt Chaser",
        style=nextcord.ButtonStyle.secondary,
        custom_id="TestRoleView:1009414672069439538",
    )
    async def hauntchaser_role_button(self, button, interaction):
        await RoleView.role_button(self, button, interaction)

    @nextcord.ui.button(
        label="League of Legends",
        style=nextcord.ButtonStyle.secondary,
        custom_id="TestRoleView:846346417407787028",
    )
    async def lol_role_button(self, button, interaction):
        await RoleView.role_button(self, button, interaction)

    @nextcord.ui.button(
        label="Minecraft",
        style=nextcord.ButtonStyle.secondary,
        custom_id="TestRoleView:864207926431186985",
    )
    async def minecraft_role_button(self, button, interaction):
        await RoleView.role_button(self, button, interaction)
    
    @nextcord.ui.button(
        label="Touhou",
        style=nextcord.ButtonStyle.secondary,
        custom_id="TestRoleView:1010498748104851518",
    )
    async def touhou_role_button(self, button, interaction):
        await RoleView.role_button(self, button, interaction)

    @nextcord.ui.button(
        label="osu!",
        style=nextcord.ButtonStyle.secondary,
        custom_id="TestRoleView:876786696140750918",
    )
    async def osu_role_button(self, button, interaction):
        await RoleView.role_button(self, button, interaction)

    @nextcord.ui.button(
        label="Overwatch",
        style=nextcord.ButtonStyle.secondary,
        custom_id="TestRoleView:979307612980015144",
    )
    async def overwatch_role_button(self, button, interaction):
        await RoleView.role_button(self, button, interaction)

    @nextcord.ui.button(
        label="Phasmophobia",
        style=nextcord.ButtonStyle.secondary,
        custom_id="TestRoleView:910442537905442828",
    )
    async def phasmophobia_role_button(self, button, interaction):
        await RoleView.role_button(self, button, interaction)

    @nextcord.ui.button(
        label="Risk of Rain 2",
        style=nextcord.ButtonStyle.secondary,
        custom_id="TestRoleView:995607024358412288",
    )
    async def ror2_role_button(self, button, interaction):
        await RoleView.role_button(self, button, interaction)

    @nextcord.ui.button(
        label="Robocraft",
        style=nextcord.ButtonStyle.secondary,
        custom_id="TestRoleView:937596693845778453",
    )
    async def robocraft_role_button(self, button, interaction):
        await RoleView.role_button(self, button, interaction)

    @nextcord.ui.button(
        label="Roblox",
        style=nextcord.ButtonStyle.secondary,
        custom_id="TestRoleView:910442523443470347",
    )
    async def roblox_role_button(self, button, interaction):
        await RoleView.role_button(self, button, interaction)

    @nextcord.ui.button(
        label="Sea of Thieves",
        style=nextcord.ButtonStyle.secondary,
        custom_id="TestRoleView:937596830601056266",
    )
    async def seaofthieves_role_button(self, button, interaction):
        await RoleView.role_button(self, button, interaction)

    @nextcord.ui.button(
        label="Star Craft 2",
        style=nextcord.ButtonStyle.secondary,
        custom_id="TestRoleView:871696568091279381",
    )
    async def sc2_role_button(self, button, interaction):
        await RoleView.role_button(self, button, interaction)

    @nextcord.ui.button(
        label="Terraria",
        style=nextcord.ButtonStyle.secondary,
        custom_id="TestRoleView:863329792660078622",
    )
    async def terraria_role_button(self, button, interaction):
        await RoleView.role_button(self, button, interaction)

    @nextcord.ui.button(
        label="Warframe",
        style=nextcord.ButtonStyle.secondary,
        custom_id="TestRoleView:950724852493459476",
    )
    async def warframe_role_button(self, button, interaction):
        await RoleView.role_button(self, button, interaction)


class ButtonRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(TestRoleView())

    @commands.command()
    @commands.guild_only()
    @commands.is_owner()
    async def buttonroletest(self, ctx: commands.Context):
        result = nextcord.Embed(description="Нажми здесь чтобы получить роль", color=0x2f3136)
        result.set_author(name="Сhoose your games")
        await ctx.send(embed=result, view=TestRoleView())
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(ButtonRoles(bot))
    print('Module ButtonRoles successfully loaded')