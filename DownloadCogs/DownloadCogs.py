from redbot.core import commands
from redbot.core.bot import Red
import git
import os

class DownloadCogs(commands.Cog):
    """Cog for downloading and loading cogs from a GitHub repository."""

    def __init__(self, bot: Red):
        self.bot = bot
        self.cogs_directory = '/home/ubuntu/RedPrism/cogs/'

    @commands.command()
    async def downloadcogs(self, ctx, repo_url: str):
        """
        Download and load cogs from a GitHub repository.

        Arguments:
        repo_url -- The URL of the GitHub repository to download and load cogs from.
        """
        try:
            git.Repo.clone_from(repo_url, self.cogs_directory)
            for filename in os.listdir(self.cogs_directory):
                if filename.endswith(".py"):
                    cog_name = filename[:-3]
                    self.bot.reload_extension(f"cogs.{cog_name}")
            await ctx.send("Cogs downloaded and loaded successfully!")
        except git.GitCommandError as e:
            await ctx.send(f"An error occurred: {e}")

    @downloadcogs.error
    async def downloaderror(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please provide the URL of the GitHub repository.")
        elif isinstance(error, git.GitCommandError):
            await ctx.send("An error occurred while downloading and loading cogs.")

def setup(bot: Red):
    bot.add_cog(DownloadCogs(bot))
