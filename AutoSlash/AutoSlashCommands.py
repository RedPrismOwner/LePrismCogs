from discord.ext import commands

class AutoSlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def create_slash_commands(self):
        for cog in self.bot.cogs.values():
            for command_name, command_object in cog.get_commands().items():
                command_description = command_object.help or "No description provided"
                slash_command = commands.Command(name=command_name, description=command_description)

                @slash_command.slash(name=command_name, description=command_description)
                async def command_wrapper(ctx, *args):
                    await command_object.callback(cog, ctx, *args)

    def setup_auto_slash_commands(self):
        self.create_slash_commands()

def setup(bot):
    auto_slash_cog = AutoSlashCog(bot)
    auto_slash_cog.setup_auto_slash_commands()
    bot.add_cog(auto_slash_cog)
