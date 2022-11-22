import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from config import settings
from config.extensions import extensions


intents = nextcord.Intents.all()

bot = commands.Bot(
    command_prefix="$",
    intents=intents,
    help_command=None,
    #activity=nextcord.Game(name="")
)

@bot.event
async def on_application_command_error(interaction: Interaction, error):
    print(f"{error} by {interaction.user.name}#{interaction.user.discriminator} on /{interaction.application_command.name}")

@bot.event
async def on_ready():
    print(f"Connected to Discord as {bot.user.name}#{bot.user.discriminator}")


if __name__ == '__main__':
    for extension in extensions["extensions"]:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"Error | Couldn't load module - {e}")

    bot.run(settings.BOT_TOKEN)