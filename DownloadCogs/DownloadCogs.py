from redbot.core import commands
from redbot.core.bot import Red
import git
import os
import random
import string
from datetime import datetime

class DownloadCogs(commands.Cog):
    """Cog for downloading and loading cogs from a GitHub repository."""

    def __init__(self, bot: Red):
        self.bot = bot

    @commands.command()
    async def downloadcogs(self, ctx, repo_url: str):
        """
        Download and load cogs from a GitHub repository.

        Arguments:
        repo_url -- The URL of the GitHub repository to download and load cogs from.
        """
        try:
            repo_name = repo_url.split("/")[-1].replace(".git", "")
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            random_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            unique_folder_name = f"{repo_name}_{timestamp}_{random_suffix}"
            clone_path = os.path.join("/home/ubuntu/RedPrism/cogs", unique_folder_name)
            git.Repo.clone_from(repo_url, clone_path)
            
            for folder_name in os.listdir(clone_path):
                cog_path = os.path.join(clone_path, folder_name)
                if os.path.isdir(cog_path):
                    for filename in os.listdir(cog_path):
                        if filename.endswith(".py"):
                            cog_name = filename[:-3]
                            await self.bot.reload_extension(f"cogs.{unique_folder_name}.{folder_name}.{cog_name}")
            
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
