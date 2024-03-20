from .AutoSlashCommands import AutoSlashCommands

async def setup(bot):
    await bot.add_cog(AutoSlashCommands(bot))
