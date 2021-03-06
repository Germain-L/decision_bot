import discord
import requests
import time

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    @staticmethod
    async def on_message(message):
        # prefix used by bot to detect commands
        prefix = '?'

        # find first character in message
        prefix_message = message.content[0]

        # end function if prefixes don't match
        if prefix_message != prefix:
            return 0

        # remove prefix from commands
        message.content = message.content[1:]

        # splits arguments into an array where ' ' are found in the message
        args = [i.lower() for i in message.content.split()]

        if args[0] == 'decide':
            deciding = await message.channel.send('Deciding ...')

            request = requests.get('https://yesno.wtf/api')

            if request.status_code == 200:
                gif = request.json()["image"]

                await message.channel.send(gif)


            else:
                await message.channel.send("An error occured because the person who coded this is dumb")
            
            await deciding.delete()

        else:
            await message.channel.send("Wrong command kiddo please use ?decide")


            

client = MyClient()
client.run('your key here')
