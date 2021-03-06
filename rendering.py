import discord
import os


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")


@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 582708984436490241:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == 'member':
            role = discord.utils.get(guild.roles, name='멤버')
        elif payload.emoji.name == 'guest':
            role = discord.utils.get(guild.roles, name='게스트')
        elif payload.emoji.name == 'elder':
            role = discord.utils.get(guild.roles, name='장로')
        elif payload.emoji.name == 'streamer':
            role = discord.utils.get(guild.roles, name='스트리머')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print("done")
            else:
                print("Member not found.")
        else:
            print("Role not found.")


@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 582708984436490241:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        if payload.emoji.name == 'member':
            role = discord.utils.get(guild.roles, name='멤버')
        elif payload.emoji.name == 'guest':
            role = discord.utils.get(guild.roles, name='게스트')
        elif payload.emoji.name == 'elder':
            role = discord.utils.get(guild.roles, name='장로')
        elif payload.emoji.name == 'streamer':
            role = discord.utils.get(guild.roles, name='스트리머')

        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
                print("done")
            else:
                print("Member not found.")
        else:
            print("Role not found.")


access_token = os.environ["BOT_TOKEN"]
client.run("access_token")
