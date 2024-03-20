from .AutoSlashCommands import AutoSlash

def setup(bot):
    bot.add_cog(AutoSlashCommands(bot))
