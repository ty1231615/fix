import discord

#original
import setting

def usege(base):
    pass

def create_usage_help(base,color=(55, 126, 219)):
    embed = discord.Embed(title=":large_orange_diamond:   **ヘルプコマンド**   :large_orange_diamond:",color=discord.Colour.from_rgb(color[0],color[1],color[2]))
    embed.add_field(
        name="使い方 :white_small_square: usege",
        value=f"{base.usage}",
        inline=False,
    )
    return embed

def help_format(base,commands=[],color=(83,237,1)):
    embed = discord.Embed(color=discord.Colour.from_rgb(color[0], color[1], color[2]))
    embed.add_field(
        name="グルー プ",
        value=base.help,
        inline=False
    )
    if commands:
        embed.add_field(
            name="コマンド一覧",
            value=view_commands(commands),
            inline=False
        )
    embed.add_field(
        name="依存関係",
        value=view_parents(base),
        inline=False
    )
    return embed

def view_parents(base):
    text = f"・{setting.icon_emoji}"
    for i in reversed(base.parents):
        text += f"   -   `{i}`"
    text += f"   |   __`{base.name}`__"
    return text

def view_commands(cmds:list):
    text = ""
    for i in cmds:
        text += f":small_blue_diamond: __`{i}`__\n"
    return text