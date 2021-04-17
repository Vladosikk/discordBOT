# from discord_webhook import DiscordWebhook, DiscordEmbed
# import conf
# #Генерируется веб-хук
# webhook = DiscordWebhook(url=conf.webhook_URL)
# #Заполняем веб-хук
# webhook.set_content(
#     "Privet, timofey"
# )
# #Генерируем вкладыш веб-хука 1
# embed0 = DiscordEmbed()
# embed0.set_author(
#     name = "Vladislav",
#     icon_url = "https://w7.pngwing.com/pngs/244/308/png-transparent-vladimir-putin-accession-of-crimea-to-the-russian-federation-united-states-putin-s-russia-vladimir-putin.png",
#     url = "https://github.com/Vladosikk"
# )
# embed0.set_title("Titul'nik ot Vlada")
# embed0.set_color("657041")
# embed0.set_description("One year ago")
# #Генерируем вкладыш веб-хука 1
# embed_1 = DiscordEmbed()
# embed_1.set_video(
#     url = "https://www.youtube.com/watch?v=ipAnwilMncI",
#     height = "200",
#     width = "200"
# )
# #Добавляем вкладыши
# webhook.add_embed(embed0)
# webhook.add_embed(embed_1)
# #Отправляем веб-хук
# webhook.execute()
import conf
import discord
from discord.ext import commands
import img_handler as imhl
import os
# Настраиваем расширенный доступ Intents
intense = discord.Intents.default()
intense.members = True
# Создаем подключение бота
#client = discord.Client(intents=intense)

# @client.event
# async def on_message(message):
#     # <Message 
#     # id=825338943959597086 
#     # channel=<TextChannel id=822806350886207542 name='флудильня' position=0 nsfw=False news=False category_id=822806350886207539> 
#     # type=<MessageType.default: 0> 
#     # author=<Member id=486903409115398144 name='❤†ᵰ†ᵰ℟ìη❤' discriminator='2082' bot=False nick=None guild=<Guild id=822806350886207538 name='Bots' shard_id=None chunked=False member_count=29>>
#     # flags=<MessageFlags value=0>>

#     #Проверка на дурака 1 - Отправлятор является самим ботом
#     if message.author == client.user:
#         return
#     #Проверка на дурака 2 - Отправлятор является самим ботом    
#     if message.author.bot:
#         return

#     #Задаем канал для бота [Vladislav]
#     if message.channel.id == 825309137751244801:
#         #Ответ пользователю в формате "Hello, {user.name} - your message {user.content}"
#         msg = None
#         #Отправляем сообщение в канал channel используя метод send
#         # 1. /hello - просто сообщения
#         bot = commands.Bot(command_prefix = "!", intents=intents)
#         # args - tuple
#         @bot.command(name = "hello")
#         async def command_hello(ctx, *args):
#         #Переводим список в строку разделенными пробелами
#             message = " ".join(args)
#             if ctx.channel.id == 825309137751244801:
#                 msg = f'Salam! Dont cry {message}'
#                 await ctx.channel.send(msg)
#         # 2. /about_me - сообщение пользователя по его параметрам id/name (если есть ник то добавить "твой ник nick")
#         @bot.command(name = "about_me")
#             msg = f'Your id is {message.author.id}'
#             if message.author.nick:
#                 msg = f'and your nick is {message.author.nick}'
#         # 3. /repeat [] - повторить за пользователя
#         @bot.command()
#         async def repeat(ctx):
#         if ctx.message.content == "#repeat":
#             await ctx.send(f'Nothing')
#         else:
#             await ctx.send(f'{ctx.message.content[7:]}')
#         # 4. /get_member {id/name} - берём инфу по пользователю по типу about_me {если пусто != обрабатываем ошибку}
#         elif ctx[0] == "/get_member":
#             name = ctx[1]
#             for idx, member in list(enumerate(message.author.guild.members)):
#                 if name == member.name or name == member.id:
#                     msg = f'His username is {member.name} {f"and his nick is {member.nick}" if member.nick else ""} and his id is {member.id}' 
#             if name == "":
#                 msg = f'There is no one who has that id or name'
#         # 5. /get_members  - список всех пользователй по "1. name {nick} id" *(через webhook)
#         elif message.content == "/get_members":
#             if message.author.guild.name == "Bots":
#                 msg = ""
#                 for idx, member in list(enumerate(message.author.guild.members)):
#                     msg += f'{idx+1}. {member.name} { f"[{member.nick}]"  if member.nick else "" } - {member.id}\n'
#         # 6. /get_сhannels  - список всех каналов категории Ботсы по "1. name id" *(через webhook)
#         elif message.content == "/get_channels":
#             msg = ""
#             if message.author.guild.name == "Bots":
#                 for idx, channel in list(enumerate(message.author.guild.channels)):
#                     msg += f'{idx+1}. {channel.name} - {channel.id}\n'
#         # 7. /goto {id/name} - подключение бота в определенный канал (по умолчанию бот подключен в свой канал)
#         elif ctx[0] == "/goto":
#             namechannel = ctx[1]
#             for idx, channel in list(enumerate(message.author.guild.channels)):
#                 if namechannel == channel.name or int(namechannel) == channel.id:
#                     message.channel.id = namechannel
#                     msg = f"Channel is changed"
#                     break
#                 else: 
#                     msg = f"channel doesn't found"
#         #Отправляем сообщение если оно есть
#         if msg != None:
#             await message.channel.send(msg)





# client.run(conf.bot_token)




bot = commands.Bot(command_prefix = "!", intents=intents)

# args - tuple
@bot.command(name = "hello")
async def command_hello(ctx, *args):
    #Переводим список в строку разделенными пробелами
    message = " ".join(args)
    if ctx.channel.id == 825309137751244801:
        msg = f'Salam! Dont cry {message}'
        await ctx.channel.send(msg)
@bot.command(name = "about_me")
async def command_hello(ctx, *args):
    #Переводим список в строку разделенными пробелами
    message = " ".join(args)
    if ctx.channel.id == 825309137751244801:
        msg = f'Salam! {ctx.author.id}'
        if ctx.author.nick:
            msg = f'and your nick is {ctx.author.nick}'
    await ctx.channel.send(msg)

@bot.command(name= "repeat")
async def command_repeat(ctx, *args):
    if ctx.channel.id == 825309137751244801:
        msg = f'{" ".join(args)}'
    await ctx.channel.send(msg)

@bot.command(name = "get_member")
async def get_member(ctx, member:discord.Member = None):
    msg = None
    global channel
    if ctx.channel.id == channel:

        if member:
            msg = f'Member {member.name}{"({member.nick})" if member.nick else " "} - {member.id}'

        if msg == None:
            msg = "error"


        await ctx.channel.send(msg)

@bot.command(name= "mk")
async def command_mk(ctx, f1: discord.Member=None, f2: discord.Member=bot.user):
    global channel
    if ctx.channel.id == channel:
        if f1 and f2:
            await imhl.vs_create(f1.avatar_url,f2.avatar_url)

            await ctx.channel.send(file=discord.File(os.path.join("./img/result.img")))




bot.run(conf.bot_token)
