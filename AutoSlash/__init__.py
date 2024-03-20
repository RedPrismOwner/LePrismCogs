from .AutoSlash import AutoSlashCommands

def setup(bot):
    bot.add_cog(AutoSlashCommands(bot))
