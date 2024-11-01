import discord
import random
import os
import json
from save_data import champions
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()  # 기본 인텐트를 가져옵니다.
intents.members = True  # 멤버 인텐트 활성화 (서버 멤버에 접근할 수 있도록)
intents.presences = True  # 사용자 상태 인텐트 활성화

client = commands.Bot(command_prefix='!', intents=intents)  # 인텐트를 봇에 추가합니다.

# 봇 초기화
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# 랜덤 라인과 챔피언 리스트
lanes = ['Top', 'Jungle', 'Mid', 'ADC', 'Support']


# 봇이 준비되었을 때
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')


# 랜덤 팀 배정
@client.event
async def on_message(message):
    if message.content.startswith('!start'):
        # 유저 리스트 가져오기
        members = [
            member for member in message.guild.members if not member.bot
        ]
        # if len(members) <= 10:
        #     await message.channel.send("10명의 플레이어가 필요합니다!")
        #     return

        random.shuffle(members)  # 유저 섞기
        team1 = members[:5]
        team2 = members[5:]

        # 팀 1과 팀 2에 각각 고유한 라인 할당
        random.shuffle(lanes)  # 라인 배열 섞기
        team1_lanes = lanes.copy()  # 팀 1용 라인 목록
        team2_lanes = lanes.copy()  # 팀 2용 라인 목록

        # 팀 1 출력
        await message.channel.send("**Team 1:**")
        for member in team1:
            lane = team1_lanes.pop()  # 고유한 라인 할당 후 목록에서 제거
            await message.channel.send(f'{member.mention} - {lane}')

        # 팀 2 출력
        await message.channel.send("**Team 2:**")
        for member in team2:
            lane = team2_lanes.pop()  # 고유한 라인 할당 후 목록에서 제거
            await message.channel.send(f'{member.mention} - {lane}')

    if message.content.startswith('!gogo'):
        # 유저 리스트 가져오기
        members = [
            member for member in message.guild.members if not member.bot
        ]
        if len(members) <= 10:
            await message.channel.send("10명의 플레이어가 필요합니다!")
            return

        random.shuffle(members)  # 유저 섞기
        team1 = members[:5]
        team2 = members[5:]

        # 팀 1과 팀 2에 각각 고유한 라인 할당
        random.shuffle(lanes)  # 라인 배열 섞기
        team1_lanes = lanes.copy()  # 팀 1용 라인 목록
        team2_lanes = lanes.copy()  # 팀 2용 라인 목록

        # champion = random.choice(champions[lane])
        # 팀 1 출력
        await message.channel.send("**Team 1:**")
        for member in team1:
            lane = team1_lanes.pop()  # 고유한 라인 할당 후 목록에서 제거
            random.shuffle(champions[lane])
            champions1 = champions[lane][0]
            await message.channel.send(
                f'{member.mention} - {lane} - {champions1}')

        # 팀 2 출력
        await message.channel.send("**Team 2:**")
        for member in team2:
            lane = team2_lanes.pop()  # 고유한 라인 할당 후 목록에서 제거
            random.shuffle(champions[lane])
            champions1 = champions[lane][0]
            await message.channel.send(
                f'{member.mention} - {lane} - {champions1}')

    if message.content.startswith('!gigi'):
        members = ['1팀', '2팀']
        random.shuffle(members)

        await message.channel.send(f"{members[0]}이 이겼습니다.")


# 봇 실행
# start the bot
client.run(TOKEN)
