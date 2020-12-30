import discord
from discord import channel

import utils as Utils
from keys.token import token

PREFIX = '!'


class MyClient(discord.Client):

    async def on_ready(self):
        # prints message when bot is online
        print('robotic voice speaking..... BOT ONLINE')

    async def on_message(self, message):
        global PREFIX
        # anti-recursion
        if message.author == client.user:
            return

        else:
            # replies hello
            if message.content.startswith('{}hello'.format(PREFIX)):
                await message.channel.send('hello')

            # magic 8-ball answers
            elif message.content.startswith('{}8-ball'.format(PREFIX)):
                answer = Utils.eightball_answer()
                await message.channel.send(answer)

            # polls command - either a simple yes/no or a range of choices
            elif message.content.startswith('{}poll'.format(PREFIX)):
                newmessage = message.content.split(' ')
                count = Utils.poll(newmessage)
                await message.channel.send('@here poll has been initiated \nreact to the above message to reply to the poll')

                # poll for a range of choices keyword = 'choices'
                if count != 1:
                    reaction_count = 0
                    await message.channel.send('choices are ')
                    while (count <= len(newmessage)):
                        await message.channel.send('{} for {}'.format(Utils.poll_reactions[reaction_count], newmessage[count]))
                        await message.add_reaction(emoji=Utils.poll_reactions[reaction_count])
                        count = count + 1
                        reaction_count = reaction_count + 1

                # poll for a simple yes or no
                else:
                    await message.add_reaction(emoji='👍')
                    await message.add_reaction(emoji='👎')
                    await message.add_reaction(emoji='🤔')

            # command to change the prefix for the bot commands
            elif message.content.startswith('{}change prefix to'.format(PREFIX)):
                newprefix = message.content[18:]
                PREFIX = newprefix
                await message.channel.send('prefix changed to {}'.format(newprefix))

    # sends message when a new member joins
    # async def on_member_join(self, member):
    #     print('welcome member')


client = MyClient()
client.run(token)
