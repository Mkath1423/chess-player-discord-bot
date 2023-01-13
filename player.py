import asyncio
import time
from chess import Board

import discord
from discord.ext import commands

BOT_TOKEN = "MTA2MzMwODI0OTk4MzYxOTE3Mg.GoXyDv.MUrAA3PzHNKzDbS53OwQM_I2uKXnfK1_BuREvg"
CHANNEL_ID = 1063309632396865576


class Session:
    def __init__(self, user, user_is_white=True):
        self.user = user

        self.board = Board()
        self.user_is_white = user_is_white








bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

current_games = {

}


def game_to_str(board: Board, white_pov=True):
    base = [[":black_large_square:" if white_pov != ((col % 2) == (row % 2)) else ":white_large_square:" for col in range(8)] for row in range(8)]

    out = "-A--B--C--D-E--F--G--H-\n"
    for i, row in enumerate(base, start=1):
        out += "".join(row)
        out += "\n"
    print(board, out, sep="\n")
    return out



@bot.command()
async def start_game(ctx, *args):
    author = ctx.message.author
    user_name = str(author).split('#')[0]
    # find if game exists with user
    if current_games.keys().__contains__(author):
        await ctx.send(f"<@{author.id}>, You already have a game! continue playing or !resign to end it")
        return


    await ctx.send(f"Alright <@{author.id}>, let's play!\n")
    await asyncio.sleep(1)
    current_games[author] = Board()
    await ctx.send(game_to_str())



@bot.event
async def on_ready():
    print("chess player is ready")

    channel = bot.get_channel(CHANNEL_ID)

    await channel.send("Ready to play?")

@bot.command()
async def hello(ctx):
    print(ctx.message.author)
    print(vars(ctx))
    await ctx.send("Hello?")

bot.run(BOT_TOKEN)