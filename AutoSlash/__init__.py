from .AutoSlashCommands import AutoSlashCommands

async def setup(bot):
    bot.add_cog(AutoSlashCommands(bot))
