import os
import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

# Botクラスを拡張して安全にコマンド同期を行う
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        # 起動の準備段階でスラッシュコマンドを確実に同期
        try:
            synced = await self.tree.sync()
            print(f"✅ 【起動完了】{len(synced)} 個のスラッシュコマンドを同期しました！")
        except Exception as e:
            print(f"❌ 同期エラー: {e}")

bot = MyBot()

MAP_CODE = "3225-0366-8885"

@bot.event
async def on_ready():
    print(f"✅ ログイン成功: {bot.user.name}")

# /map コマンド
@bot.tree.command(name="map", description="Steal the Brainrotの島コードを表示します")
async def map_command(interaction: discord.Interaction):
    await interaction.response.defer()
    embed = discord.Embed(
        title="🧠 STEAL THE BRAINROT",
        description=f"**島コード**: `{MAP_CODE}`\n[Epic Gamesで開く](https://www.fortnite.com/@ferins/{MAP_CODE})",
        color=discord.Color.purple()
    )
    embed.set_footer(text="マップ製作者: ferins")
    await interaction.followup.send(embed=embed)

# /code コマンド
@bot.tree.command(name="code", description="最新の特典コード状態を表示します")
async def code_command(interaction: discord.Interaction):
    await interaction.response.defer()
    embed = discord.Embed(
        title="🎁 最新特典コード一覧",
        description="今STEAL THE BRAINROTで使用できるコードはありません。",
        color=discord.Color.red()
    )
    await interaction.followup.send(embed=embed)

# /link コマンド
@bot.tree.command(name="link", description="公式Discordサーバーのリンクを表示します")
async def link_command(interaction: discord.Interaction):
    await interaction.response.defer()
    embed = discord.Embed(
        title="🔗 STEAL THE BRAINROTの公式サーバー",
        description="以下のリンクから公式Discordサーバーに参加できます：\nhttps://discord.gg/brainrotfn",
        color=discord.Color.blue()
    )
    await interaction.followup.send(embed=embed)

# /machineevent コマンド
@bot.tree.command(name="machineevent", description="アドミンマシンの属性の確率表を表示します")
async def machineevent_command(interaction: discord.Interaction):
    await interaction.response.defer()
    text = (
        "アドミンマシンの属性の確率表です。\n"
        "· Heaven 11%\n"
        "· Void 11%\n"
        "· Rave 13%\n"
        "· Aqua 11%\n"
        "· Neon 12%\n"
        "· Gothic 10%\n"
        "· Summer 11%\n"
        "· Magical 11%\n"
        "· Jungle 10%"
    )
    await interaction.followup.send(text)

token = os.getenv("DISCORD_TOKEN")
bot.run(token)
