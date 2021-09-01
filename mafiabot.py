import discord
from discord.ext import commands
import asyncio
from discord.ext.commands import check
import random

print('    Version 1.2.1 \n    Code written by Abbas Mohamadi \n    10/17/2020 \n \n \n')


#here we can use our bot with a custom prefix for example we can type .m for mute
client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Bot is ready')

# command .m mute all the members in the current voice channel that the user is connect to
@client.command()
async def m(ctx):
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.edit(mute=True)
        print('mute done')
    await ctx.send('All users are Muted')

# command .um mute all the members in the current voice channel that the user is connect to
@client.command()
async def um(ctx):
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.edit(mute=False)
        print('unmute done')
    await ctx.send('All users are UnMuted')


def in_voice_channel():  # check to make sure ctx.author.voice.channel exists
    def predicate(ctx):
        return ctx.author.voice and ctx.author.voice.channel
    return check(predicate)

# command .move <your voice chat name> move all the users into the new voice chat
@in_voice_channel()
@client.command()
async def move(ctx, *, channel: discord.VoiceChannel):
    for members in ctx.author.voice.channel.members:
        await members.move_to(channel)

# command .dm <this is your custom message> sends the custom message
# to all the users that connect to that specific voice channel in direct message
@client.command()
async def dm(ctx, *, args=None):
    if args != None:
        members = ctx.author.voice.channel.members
        for member in members:
            try:
                await member.send(args)
                print("'"+ args + "' send to : " + member.name)

            except:
                print("Could't send '" + args + "' to " + member.name)
    else:
        await ctx.channel.send(" You don't provide arguments")


# command .role give random mafia roles to random person that connect to the voice channel
@client.command()
async def role(ctx):
        role = ['civil 1', 'civil 2', 'doctor', 'armor', 'detective', 'sniper', 'press', 'god father',
            'mafia negotiator',
            'simple mafia']
        members = ctx.author.voice.channel.members
        mafia = ['god father', 'mafia negotiator', 'simple mafia']
        mafiamember = []
        mafianame = []

        for member in members:
            X = random.choice(role)

            try:

                await member.send(X)
                print("'" + X + "' send to : " + member.name)
                role.remove(X)
                print(role)

                if X in mafia:
                    mafiamember.append(member)
                    mafianame.append(str(member.name + "  --->  " + X))
            except:
                print("Could't send '" + X + "' to " + member.name)
        for member in mafiamember:
            await member.send("your team mates are : " + str(mafianame))
        print("\n \n \n \n " + str(mafianame))



#here you have to enter your discord server token number
client.run('your token number should enter here')

