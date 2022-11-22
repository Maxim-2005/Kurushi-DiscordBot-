import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
from config import settings

class ExampleSlash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=[settings.GUILD_ID], description="Чистка текущего канала от сообщений")
    async def clear(self, interaction: Interaction, amount: int=SlashOption(description="Количество сообщений для удаления", required=True)):
        await interaction.response.send_message(f"Ваш запрос выполняется. Пожалуйста, подождите...", ephemeral=True)
        messages = await interaction.channel.purge(limit=amount)
        await interaction.edit_original_message(content=f"Удалено **{len(messages)}** сообщений в этом канале")

def setup(bot):
    bot.add_cog(ExampleSlash(bot))
    print("Module ExampleSlash successfully loaded")