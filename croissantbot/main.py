import os  # ← これを一番上の行（import discord の近く）に追加
import discord
from discord import app_commands
from discord.ext import commands

# 準備・設定
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

MAP_CODE = "3225-0366-8885"

@bot.event
async def on_ready():
    print(f"✅ ログイン成功: {bot.user.name}")
    try:
        # スラッシュコマンドをDiscordに同期
        synced = await bot.tree.sync()
        print(f"✅ {len(synced)} 個のコマンドを同期しました")
    except Exception as e:
        print(f"❌ 同期エラー: {e}")

# /map コマンド
@bot.tree.command(name="map", description="Steal the Brainrotの島コードを表示します")
async def map_command(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🧠 STEAL THE BRAINROT",
        description=f"**島コード**: `{MAP_CODE}`\n[Epic Gamesで開く](https://www.fortnite.com/@ferins/{MAP_CODE})",
        color=discord.Color.purple()
    )
    embed.set_footer(text="マップ製作者: ferins")
    await interaction.response.send_message(embed=embed)

# /code コマンド（/codesから変更）
@bot.tree.command(name="code", description="最新の特典コード状態を表示します")
async def code_command(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🎁 最新特典コード一覧",
        description="今STEAL THE BRAINROTで使用できるコードはありません。",
        color=discord.Color.red()
    )
    await interaction.response.send_message(embed=embed)

# /link コマンド（新規追加）
@bot.tree.command(name="link", description="公式Discordサーバーのリンクを表示します")
async def link_command(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🔗 STEAL THE BRAINROTの公式サーバー",
        description="以下のリンクから公式Discordサーバーに参加できます：\nhttps://discord.gg/brainrotfn",
        color=discord.Color.blue()
    )
    await interaction.response.send_message(embed=embed)

# ここに取得したトークンを貼り付けます
token = os.getenv("DISCORD_TOKEN")
bot.run(token)