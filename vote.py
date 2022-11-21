import discord
from discord.ext import commands

import textFormat

groups = [
    "new"
]

cmds = [
    [
        "vote"
    ]
]

class VOTE:
    def __init__(self,id,tag) -> None:
        self.__id = id
        self.__tag = tag
        self.__count = 0
    def PLUS(self) -> bool:
        self.__count += 1
        return True
    def DOWN(self) -> bool:
        if self.__count > 0:
            self.__count -= 1
            return True
        return False
    def get_id(self):
        return self.__id
    def get_tag(self):
        return self.__tag

class Vote(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        self.bot = bot
        self.__votes = []
    @commands.Cog.listener()
    async def on_ready(self):
        print("OnReady Vote System")
    @commands.group(invoke_without_command=True,name=groups[0])
    async def new(self,ctx):
        """
        新規の項目を追加するオプションです

        `Vote cogのコンポーネントです、関連するコマンドは !new で閲覧することができます`
        `#このインスタンスはCommands.Groupでデコレートされています`
        """
        await ctx.send(embed=textFormat.help_format(self.new,commands=cmds[0]))
    @new.command(name=cmds[0][0],usage="vote <`name`> <`tag`>")
    async def create_vote(self,ctx,name,tag):
        pass
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.UserInputError):
            embed = textFormat.create_usage_help(ctx.command,color=(237, 50, 90))
            embed.description = f"__`{ctx.command.name}`**コマンドを実行できません、再度ヘルプを確認してください.**__"
            await ctx.send(embed=embed)
    

        
def setup(bot:commands.Bot):
    bot.add_cog(Vote(bot))