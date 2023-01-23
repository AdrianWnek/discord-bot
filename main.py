# pip install discord

import discord

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('Bot Is Online {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Hi'): # Start conversation with Bot by typing "Hi"
        await message.channel.send('Hello!') # Bot will reply with "Hello!"

    if message.content.startswith('How are you?'): # You can ask the Bot a question
        await message.channel.send("I'm Great, thanks for asking!") # Bot will reply again

@client.event
async def on_member_join(member):
    channel = client.get_channel(1060348886222385202)
    embed=discord.Embed(title="Wlecome!",description=f"{member.mention} Just Joined")
    await channel.send(embed=embed)

# Paste your token here \/
client.run('YOUR PRIVATE TOKEN')
#To obtain the token make sure to go to Discord Developers
######### Never give your token to anyone, it might ruin your discord server! #########
######### https://discord.com/login?redirect_to=%2Fdevelopers #########
