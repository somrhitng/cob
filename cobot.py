from discord.ext import commands
import discord, datetime

bot = commands.Bot(command_prefix="f!")


@bot.command()
async def ping(ctx):
    ': Check your connection '
    t1 = ctx.message.created_at
    m = await ctx.send('**Pong!**')
    time = (m.created_at - t1).total_seconds() * 1000
    await m.edit(content='**Pong! Took: {}ms**'.format(int(time)))


@bot.command()
async def kick(ctx, member: discord.Member, *, reason):
    ': Kick the member if you have authority '
    if ctx.author.permissions_in(ctx.channel).kick_members:
        if reason is None:
            await member.send(
                f'''You have been kicked by {ctx.author.name} from {ctx.guild.name} due to __No reason given__ ''')
            em = discord.Embed(title='Kicked', colour=discord.Colour.dark_red(),
                               description=f'''{member} has been kicked''', timestamp=datetime.datetime.utcnow())
            em.set_thumbnail(url=member.avatar_url)
            em.add_field(name='Moderator', value=f'''{ctx.author.name}''', inline=False)
            em.add_field(name='Culpret', value=f'''{member}''', inline=False)
            em.add_field(name='Reason for kicking', value=f'''_No reason provided_''', inline=False)
            await ctx.send(embed=em)
            await member.kick()
        else:
            await member.send(f'''You have been kicked by {ctx.author.name} from {ctx.guild.name} due to {reason} ''')
            em = discord.Embed(title='Kicked', colour=discord.Colour.dark_red(),
                               description=f'''{member} has been kicked''', timestamp=datetime.datetime.utcnow())
            em.set_thumbnail(url=member.avatar_url)
            em.add_field(name='Moderator', value=f'''{ctx.author.name}''', inline=False)
            em.add_field(name='Culprit', value=f'''{member}''', inline=False)
            em.add_field(name='Reason for kicking', value=f'''{reason}''', inline=False)
            await ctx.send(embed=em)
            await member.kick(reason=reason)
    else:
        message = await ctx.send(f'''{ctx.author.mention} you are not eligible for this''', delete_after=3)
        await message.add_reaction('\u2623')


@bot.command()
async def perms(ctx, user: discord.Member = None):
    ': Find what you can do on this server'
    user = ctx.message.author if user is None else user
    if not user:
        user = ctx.author
    mess = []
    for i in user.guild_permissions:
        if i[1]:
            mess.append("\u2705 {}".format(i[0]))
        else:
            mess.append("\u274C {}".format(i[0]))
    embed = discord.Embed(title=f'''{user.name} 's permissions in the server are: ''', description="\n".join(mess),
                          color=discord.Colour.dark_purple())
    await ctx.send(embed=embed)


@commands.command()
async def warn(ctx, member: discord.Member , *, reason = None):
    ''': SoftWarn a person'''
    if ctx.author.permissions_in(ctx.channel).kick_members or ctx.author.permissions_in(ctx.channel).manage_messages:
        if reason is None:
            await ctx.send(f'''{ctx.author.mention} \n ```A reason needed to warn``` ''')
        else:
            embed = discord.Embed(title='Warning', colour=discord.Colour.gold(),
                                  description=f'''You have been warned by {ctx.author.name} for {reason}''',
                                  timestamp=datetime.datetime.utcnow())
            await member.send(embed=embed)
            em = discord.Embed(title='Warned', colour=discord.Colour.gold(),
                               description=f'''{member} has been warned''', timestamp=datetime.datetime.utcnow())
            em.set_thumbnail(url=member.avatar_url)
            em.add_field(name='Moderator', value=f'''{ctx.author.name}''', inline=False)
            em.add_field(name='Culprit', value=f'''{member}''', inline=False)
            em.add_field(name='Reason for warning', value=f'''{reason}''', inline=False)
            await ctx.send(embed=em)
    else:
        await ctx.send(f'''{ctx.author.mention} you aren't eligible for this''', delete_after=3)


@bot.command()
async def swarn(ctx, member: discord.Member , *, reason = None):
    ': Warn a person seriously'
    if ctx.author.permissions_in(ctx.channel).kick_members or ctx.author.permissions_in(ctx.channel).manage_messages:
        if reason is None:
            await ctx.send(f'''{ctx.author.mention} \n ```A serious reason needed to warn``` ''')
        else:
            embed = discord.Embed(title='Warning', colour=discord.Colour.red(),
                                  description=f'''You have been warned by {ctx.author.name} for {reason}''',
                                  timestamp=datetime.datetime.utcnow())
            await member.send(embed=embed)
            em = discord.Embed(title='Seriously Warned', colour=discord.Colour.red(),
                               description=f'''{member} has been warned''', timestamp=datetime.datetime.utcnow())
            em.set_thumbnail(url=member.avatar_url)
            em.add_field(name='Moderator', value=f'''{ctx.author.name}''', inline=False)
            em.add_field(name='Culprit', value=f'''{member}''', inline=False)
            em.add_field(name='Reason for warning', value=f'''{reason}''', inline=False)
            await ctx.send(embed=em)
    else:
        await ctx.send(f'''{ctx.author.mention} you aren't eligible for this''', delete_after=3)

@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    ': Warn a person seriously'
    if ctx.author.permissions_in(ctx.channel).ban_members:
        if reason is None:
            await ctx.send(f'''{ctx.author.mention} \n ```A serious reason needed to ban``` ''')
        else:
            embed = discord.Embed(title='Warning', colour=discord.Colour.red(),
                                  description=f'''You have been banned by {ctx.author.name} for {reason}''',
                                  timestamp=datetime.datetime.utcnow())
            await member.send(embed=embed)
            await member.ban(reason=reason)
            em = discord.Embed(title='Seriously Warned', colour=discord.Colour.red(),
                               description=f'''{member} has been warned''', timestamp=datetime.datetime.utcnow())
            em.set_thumbnail(url=member.avatar_url)
            em.add_field(name='Moderator', value=f'''{ctx.author.name}''', inline=False)
            em.add_field(name='Culprit', value=f'''{member}''', inline=False)
            em.add_field(name='Reason for warning', value=f'''{reason}''', inline=False)
            await ctx.send(embed=em)
    else:
        await ctx.send(f'''{ctx.author.mention} you aren't eligible for this''', delete_after=3)

    await bot.run("NDc5NjEyNTYyODk2NDUzNjMy.Dlbxog.xCyAGpII5X3nxiF0sheBSZlNm8k")