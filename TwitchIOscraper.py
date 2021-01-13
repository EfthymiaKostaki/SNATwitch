from twitchio.ext import commands

bot = commands.Bot(
    irc_token='oauth:677hgdmf1jw8pdktptf2txxann84wr',
    api_token='test',
    nick='effieko',
    prefix='!',
    initial_channels=['MacieJay']
)

# Register an event with the bot
@bot.event
async def event_ready():
    print(f'Ready | {bot.nick}')

@bot.event
async def event_message(message):
    print(message.content)

    # If you override event_message you will need to handle_commands for commands to work.
    await bot.handle_commands(message)

# Register a command with the bot
@bot.command(name='test', aliases=['t'])
async def test_command(ctx):
    await ctx.send(f'Hello {ctx.author.name}')
bot.run()
