import os
from dotenv import load_dotenv
import twitchio
from twitchio.ext import commands

# Load environment variables
load_dotenv()

class TwitchFunBot(commands.Bot):
    def __init__(self):
        super().__init__(
            token=os.getenv('TWITCH_TOKEN'),
            client_id=os.getenv('TWITCH_CLIENT_ID', ''),
            nick=os.getenv('BOT_NICKNAME', 'FunBot'),
            prefix='!',
            initial_channels=[os.getenv('TWITCH_CHANNEL')]
        )
        
    async def event_ready(self):
        print(f'Bot {self.nick} is online!')
        
    async def event_message(self, message):
        if message.echo:
            return
        print(f'{message.author.name}: {message.content}')
        await self.handle_commands(message)
        
    @commands.command()
    async def hello(self, ctx):
        """Say hello to the bot"""
        await ctx.send(f'Hello {ctx.author.name}! 👋')
        
    @commands.command()
    async def coinflip(self, ctx):
        """Flip a coin"""
        import random
        result = random.choice(['Heads', 'Tails'])
        await ctx.send(f'{ctx.author.name} flipped a coin and got: {result}!')
        
    @commands.command()
    async def dice(self, ctx, sides: int = 6):
        """Roll a dice"""
        import random
        if sides < 1:
            await ctx.send('Dice must have at least 1 side!')
            return
        result = random.randint(1, sides)
        await ctx.send(f'{ctx.author.name} rolled a d{sides} and got: {result}!')


if __name__ == '__main__':
    bot = TwitchFunBot()
    bot.run()
