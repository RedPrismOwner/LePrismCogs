from redbot.core import commands
from redbot.core.bot import Red
import git
import os

class DownloadCogs(commands.Cog):
    def __init__(self, bot: Red):
        self.bot = bot

    @commands.command()
    async def download_and_load_cogs(self, ctx, repo_url: str):
        try:
            git.Repo.clone_from(repo_url, "temp_cogs")
            for filename in os.listdir("temp_cogs"):
                if filename.endswith(".py"):
                    cog_name = filename[:-3]
                    self.bot.reload_extension(f"temp_cogs.{cog_name}")
            await ctx.send("Cogs downloaded and loaded successfully!")
        except git.GitCommandError as e:
            await ctx.send(f"An error occurred: {e}")

async def setup(bot: Red):
    await bot.add_cog(DownloadCogs(bot))
