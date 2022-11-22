import nextcord
import requests
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
from config import settings

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=[settings.GUILD_ID], description="Получени исходника аватарки")
    async def avatar(self, interaction: Interaction, member: nextcord.Member=SlashOption(description="Укажите участника", required = False)):
        if not member:
            member = interaction.user
        result = nextcord.Embed(
            description=f"Аватарка {member.mention}",
            color=0x2f3136
        )
        result.set_image(url=member.display_avatar.url)
        await interaction.response.send_message(embed=result)

def setup(bot):
    bot.add_cog(Avatar(bot))
    print("Module Avata successfully loaded")