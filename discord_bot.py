import discord
import random

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))

        if message.content.startswith('!puppy'):
            await message.channel.send("Here's your puppy!")
            dog_file = discord.File("C:\\Python Files\\Puppies\\puppy-" + str(random.randint(0,36)) + ".jpg", filename="puppy.jpg")
            await message.channel.send(file = dog_file)

        if message.content.startswith('!stop_it'):
            await message.channel.send("Nice to meet you!")
            simp_file = discord.File('C:\\Python Files\\Puppies\\sameer_fedora.png')
            await message.channel.send(file = simp_file)

client = MyClient()
client.run('insert token here')
