from redbot.core import commands
from redbot.core.bot import Red
import git

class DownloadCogs(commands.Cog):
    def __init__(self, bot: Red):
        self.bot = bot

    @commands.command()
    async def downloadcogs(self, ctx, repo_url: str):
        try:
            git.Repo.clone_from(repo_url, "/home/ubuntu/RedPrism/cogs")
            for cog_file in os.listdir("/home/ubuntu/RedPrism/cogs"):
                if cog_file.endswith(".py"):
                    cog_name = cog_file[:-3]
                    if f"cogs.{cog_name}" in self.bot.extensions:
                        self.bot.reload_extension(f"cogs.{cog_name}")
                    else:
                        self.bot.load_extension(f"cogs.{cog_name}")
            await ctx.send("Cogs downloaded and loaded successfully!")
        except git.GitCommandError as e:
            await ctx.send(f"An error occurred: {e}")

def setup(bot: Red):
    bot.add_cog(DownloadCogs(bot))
