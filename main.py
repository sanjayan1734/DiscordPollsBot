import discord
from discord import channel
import utils as Utils 
from keys.token import token

prefix = '!'         # prefix for the bot commands

class MyClient(discord.Client):

    async def on_ready(self):
        print('robotic voice speaking..... BOT ONLINE') # prints message when bot is online

    async def on_message(self, message):
        global prefix        
        #checks if the message is from the user and not the bot
        if message.author == client.user:     
            return
        
        else:
            #replies hello
            if message.content.startswith('{}hello'.format(prefix)):     
                await message.channel.send('hello')
            
            #magic 8-ball answers
            elif message.content.startswith('{}8-ball'.format(prefix)):       
                answer = Utils.eightball_answer()
                await message.channel.send(answer)
            
            #polls command - either a simple yes/no or a range of choices
            elif message.content.startswith('{}poll'.format(prefix)):              
                newmessage= message.content.split(' ')
                count = Utils.poll(newmessage) 
                await message.channel.send('@here poll has bee initiated \n react to the above message to reply to the poll')
                
                #poll for a range of choices keyword = 'choices'
                if count != 1:
                    reaction_count = 0
                    await message.channel.send('choices are ')
                    while (count<=len(newmessage)):
                        await message.channel.send('{} for {}'.format(Utils.poll_reactions[reaction_count],newmessage[count]))
                        await message.add_reaction(emoji=Utils.poll_reactions[reaction_count])
                        count = count + 1
                        reaction_count = reaction_count + 1

                #poll for a simple yes or no 
                else :
                    await message.add_reaction( emoji='👍')
                    await message.add_reaction(emoji='👎')
                    await message.add_reaction(emoji='🤔')

            #command to change the prefix for the bot commands
            elif message.content.startswith('{}change prefix to'.format(prefix)):
                newprefix = message.content[18:]
                prefix = newprefix
                await message.channel.send('prefix changed to {}'.format(newprefix)) 

    #(not working yet)sends message when a new member joins
    async def on_member_join(member):
        print('welcome member')
        await channel.send('welcome {} '.format(member))


client = MyClient()
#bot token(needs to be moved to a seperate file)
client.run(token)