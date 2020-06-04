import discord
import datetime
import re

from discord.ext import commands
from urllib import parse, request

from random import randint, randrange


token = ''

bot = commands.Bot(command_prefix='m>', description="Hi, im chatarra, a pleasure to serve u")


# Cpaperiommands



# this command test if the bot is connected or not
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

# this command returns the sum of two different numbers
@bot.command()
async def sum(ctx ,a: int, b: int):
    await ctx.send(a + b)

# this command shows the stats of the server
@bot.command()
async def stats(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Chatarra bot", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server was created at: ", value=f'{ctx.guild.created_at}')
    embed.add_field(name="Server id: ", value=f"{ctx.guild.id}")
    embed.set_image(url='https://i1.wp.com/codigoespagueti.com/wp-content/uploads/2014/06/GIF.gif?resize=640%2C360&quality=80&ssl=1')
    
    try:
        embed.thumbnail(url=f"{ctx.guild.id}")
    except:
        pass

    await ctx.send(embed=embed)


# this commant calls idiot to whatever is mentioned.
@bot.command()
async def idiot(ctx, naming : discord.Member):
    usuario = ctx.message.author
    nombre_bot = bot.user.id
    naming = '<@!{}>'.format(naming.id)
    print(naming)
    print('<@!{}>'.format(usuario.id))
    if(naming == '<@!{}>'.format(nombre_bot)):

        await ctx.send('no u {0.mention}'.format(usuario))
        await ctx.send('https://giphy.com/gifs/a4sJykNINf0f6')

    elif (naming == '<@!{}>'.format(usuario.id)):

        await ctx.send(f'ur telling me u r an idiot{naming}?')
        await ctx.send('https://giphy.com/gifs/frustrated-glee-angry-NvIGNFAGDEcqk')

    else:
        await  ctx.send(f'jaja they told u idiot {naming}')
        await  ctx.send('https://giphy.com/gifs/idiot-sandwich-3o85xnoIXebk3xYx4Q')

# this command gives you the link of wathever you are searching from youtube
@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    print(search_results)
    await ctx.send("https://www.youtube.com//watch?v=" + search_results[0])

# this command is for sayin Despacito in a mean way for Des >:)
@bot.command()
async def Des(ctx):
    await ctx.send('Des')
    await ctx.send('Pa')
    await ctx.send('cito')

@bot.command()
async def tell(ctx):
    await ctx.send('On construction')

# command to tell the mentioned user that they artwork is 10/10
@bot.command()
async def tenof(ctx, member: discord.Member):
    rando = randrange(5)

    switcher ={
        0: 'https://giphy.com/gifs/201516-BWySufD6KWQzC',
        1: 'https://giphy.com/gifs/mrw-someone-brady-ar4x1w44umngk',
        2: 'https://giphy.com/gifs/fWh7ETXumAQIwRLwwk',
        3: 'https://giphy.com/gifs/reaction-EBPvJ8wA04Kc0',
        4: 'https://giphy.com/gifs/sbnation-10-2ZqbXco8wMMDqsvpfJS'
    }
    await ctx.send('<@!{}>'.format(member.id))
    await ctx.send(f' {switcher[rando]}')

@bot.command()
async def F(ctx):
    member = ctx.message.author
    rando = randrange(5)
    switcher ={
    0: 'https://giphy.com/gifs/hyperxgaming-hyperx-family-gaming-hStvd5LiWCFzYNyxR4',
    1: 'https://giphy.com/gifs/press-your-luck-LXpmVImP06400',
    2: 'https://giphy.com/gifs/spongebob-squarepants-f-cFLLnExjELn7a',
    3: 'https://giphy.com/gifs/cartoonhangover-LWlw7lJJB2HCNwnKPM',
    4: 'https://giphy.com/gifs/noahcyrus-noah-cyrus-we-are-3ohjV4uRfStUFPGCty'
    }
    await ctx.send('F. <@!{}>'.format(member.id))
    await ctx.send(f' {switcher[rando]}')

@bot.command()
async def code(ctx):
    await ctx.send("""```py
            print("hola mundo")
            ```""")




# events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("i like kill... serving People"))
    print('Bot ready')



#@bot.event
#async def on_member_join(member):
#    pass
bot.run(token)
