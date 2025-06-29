from discord.ext import commands
from dotenv import load_dotenv
import discord
import os

load_dotenv()
TOKEN = os.getenv(key='TOKEN')

intents = discord.Intents.default()
intent.message_content = True

bot = commands.Bot(intents=intents, command_prefix='!')

@bot.event
async def on_ready():
    print(f'Бот {bot.user} запущен и готов к работе!')
    
@bot.command(name = 'hello')
async def greet(ctx):
    await ctx.send(f'Привет, {ctx.author.name}! Чем я могу помочь!')
    
    
if __name__ == '__main__':
    bot.run(token=TOKEN)