from .DownloadCogs import DownloadCogs

async def setup(bot):
    await bot.add_cog(DownloadCogs(bot))
