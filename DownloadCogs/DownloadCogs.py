from redbot.core import commands
import git

class DownloadCogs(commands.Cog):
    """Cog for downloading cogs from a GitHub repository."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def download_cogs(self, ctx, repo_url: str):
        """
        Download cogs from a GitHub repository.
        
        Arguments:
        repo_url -- The URL of the GitHub repository to download cogs from.
        """
        try:
            git.Repo.clone_from(repo_url, "cogs")
            await ctx.send("Cogs downloaded successfully!")
        except git.GitCommandError as e:
            await ctx.send(f"An error occurred: {e}")

    @download_cogs.error
    async def download_cogs_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please provide the URL of the GitHub repository.")
        elif isinstance(error, git.GitCommandError):
            await ctx.send("An error occurred while downloading cogs.")

def setup(bot):
    bot.add_cog(DownloadCogs(bot))
