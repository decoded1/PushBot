import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('!sendmessage'):
        await message.channel.send('This is a custom message!')

async def send_timed_message():
    await client.wait_until_ready()
    channel = client.get_channel(1068876041898184786)
    while True:
        await channel.send('This is a timed message!')
        await asyncio.sleep(60)

client.loop.create_task(send_timed_message())

client.run('MTA3OTA3MDc1Mjg2MDU0MDk0OA.G-OgPs.eJepOfXoOsQi2sQqC-Gd_5oGBgyLqZHHSxornk')
