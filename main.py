import discord
from discord import channel

import utils as Utils
from keys import token

PREFIX = '!'


class MyClient(discord.Client):

    async def on_ready(self):
        # prints message when bot is online
        print('robotic voice speaking..... BOT ONLINE')
        await client.change_presence(activity=discord.Game(name='type {}help'.format(PREFIX)))

    async def on_message(self, message):
        global PREFIX
        # anti-recursion
        if message.author == client.user:
            return

        else:
            # replies hello
            if message.content.lower().startswith('{}hello'.format(PREFIX)):
                await message.channel.send('hello')

            # magic 8-ball answers
            elif message.content.lower().startswith('{}8-ball'.format(PREFIX)):
                messageList = message.content.split(' ')
                
                if(Utils.check_commandlength(messageList)):
                    answer = Utils.eightball_answer()
                    await message.channel.send(answer)
                else:
                    await message.channel.send('Incomplete Command!!!')

            # polls command - either a simple yes/no or a range of choices
            elif message.content.lower().startswith('{}poll'.format(PREFIX)):
                newmessage = message.content.split(' ')
                count = Utils.poll_option(newmessage)
                print(count)
                if count == 1:
                    await message.channel.send('please enter a statement for your poll')

                # poll for a range of choices keyword = 'choices'
                elif count != 1 and count<=len(newmessage)-1:
                    reaction_count = 0
                    await message.channel.send('@here poll has been initiated \nreact to the above message to reply to the poll')
                    await message.channel.send('choices are ')
                    while (count < len(newmessage)):
                        await message.channel.send('{} for {}'.format(Utils.poll_reactions[reaction_count], newmessage[count]))
                        await message.add_reaction(emoji=Utils.poll_reactions[reaction_count])
                        count = count + 1
                        reaction_count = reaction_count + 1

                # poll for a simple yes or no
                else:
                    await message.channel.send('@here poll has been initiated \nreact to the above message to reply to the poll')
                    await message.add_reaction(emoji='👍')
                    await message.add_reaction(emoji='👎')
                    await message.add_reaction(emoji='🤔')

            # command to change the prefix for the bot commands
            elif message.content.lower().startswith('{}prefix'.format(PREFIX)):
                newprefix = message.content[8:]
                if(len(newprefix)<2):
                    print(len(newprefix))
                    print(newprefix)
                    PREFIX = newprefix
                    await message.channel.send('prefix changed to {}'.format(newprefix))
                else:
                    await message.channel.send('Prefix must be a single character!!')

            # command to display the help Embed
            elif message.content.lower().startswith('{}help'.format(PREFIX)):
                embed_message = discord.Embed(title = 'help',discription ='bot commands')
                embed_message.set_author(name=client.user)
                embed_message.add_field(name = 'commands',value='{}poll \n{}prefix \n{}8-ball'.format(PREFIX,PREFIX,PREFIX))
                await message.channel.send(embed = embed_message)

client = MyClient()
client.run(token)
