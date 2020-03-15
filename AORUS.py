import asyncio
import discord
from discord.ext import commands
from discord.utils import get


app = commands.Bot(command_prefix='어로스 봇')

token = "Njg4NDQyMjIwNzg1MDQxNDQ1.Xm5gVg.2V28L3fxFqkPDrZd54fyZrw2hK8"
calcResult = 0

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")
    game = discord.Game("어로스 봇 실행중")
    await app.change_presence(status=discord.Status.online, activity=game)

@app.command(name="추방", pass_context=True)
async def _kick(ctx, *, user_name: discord.Member, reason=None):
    await user_name.kick(reason=reason)
    await ctx.send(str(user_name)+"을(를) 추방하였습니다.")

@app.command(name="밴", pass_context=True)
async def _ban(ctx, *, user_name: discord.Member):
    await user_name.ban()
    await ctx.send(str(user_name)+"을(를) 밴 시켰습니다.")

@app.command(name="역할추가", pass_context=True)
async def _HumanRole(ctx, member: discord.Member=None):
    member = member or ctx.message.author
    await member.add_roles(get(ctx.guild.roles, name="AORUS 시민"))
    await ctx.channel.send("인증이 정상적으로 처리되었습니다.")



@app.event
async def on_message(message):
    await app.process_commands(message)
    if message.author.bot:
        return None
    if message.content == "어로스 봇 출력":
        await message.channel.send("어로스 봇 에 의해 출력됨.")
    if message.content.startswith("어로스 봇 1부터10"):
        for x in range(10):
            await message.channel.send(x+1)
    if message.content.startswith("어로스 봇 계산"):
        global calcResult
        param = message.content.split()
        try:
            if param[1].startswith("더하기"):
                calcResult = int(param[2]) + int(param[3])
                await message.channel.send("Result : " + str(calcResult))
            if param[1].startswith("빼기"):
                calcResult = int(param[2]) - int(param[3])
                await message.channel.send("Result : " + str(calcResult))
            if param[1].startswith("곱하기"):
                calcResult = int(param[2]) * int(param[3])
                await message.channel.send("Result : " + str(calcResult))
            if param[1].startswith("나누기"):
                calcResult = int(param[2]) / int(param[3])
                await message.channel.send("Result : " + str(calcResult))
        except IndexError:
            await message.channel.send("무슨 숫자를 계산할지 알려주세요.")
        except ValueError:
            await message.channel.send("숫자로 넣어주세요.")
        except ZeroDivisionError:
            await message.channel.send("You can't divide with 0.")


app.run(token)