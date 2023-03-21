import discord
import os
# import random
from dotenv import load_dotenv
from typing import Union
from discord import Message
from ttt import ttt

load_dotenv()
token = os.getenv('TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        self.state = "message"

    async def on_typing(self, channel, user, when):
        print(f"{user} is typing message in {channel} {when}")

    async def on_message(self, message):
        print(f'Message from {message.author} in {message.channel}: {message.content}')
        print(message.attachments)

        if message.author == client.user:
            print("ignoring bot message")
            return

        if client.user in message.mentions:
            print("bot mentioned")
            print(f"\tsending message: I WAS MENTIONED")
            await message.channel.send("I WAS MENTIONED")

        if "hello" in message.content :
        # if message.content == "hello":
            print(f"command recognized: hello")
            print(f"\tsending message: hello")
            await message.channel.send("hello")

        if "react" in message.content:
            print(f"\treacting with 👍")
            await message.add_reaction("👍")
            await message.add_reaction("👽")
        
        if message.content == "ttt":
            self.state = "ttti"
            self.player_1 = message.author
            await message.channel.send(f"player 1 is {self.player_1}")
            await message.channel.send(f"please mention player 2")
        if self.state == "ttti" and message.author == self.player_1 and len(message.mentions)==1:
            self.state = "ttt1"
            self.player_2 = message.mentions[0]
            await message.channel.send(f"player 2 is {self.player_2}")
            await message.channel.send("use the numberpad for input:\n```7 | 8 | 9\n--+---+--\n4 | 5 | 6\n--+---+--\n1 | 2 | 3 \n```")
            await message.channel.send(f"{self.player_1}'s turn")
            self.game = ttt()

        if message.content in {"1","2",'3','4','5','6','7','8','9'} and self.state in {"ttt1", "ttt2"} and message.author in {self.player_1, self.player_2}:
            status = self.game.update_board(message.content, self.state)
            if status == -1: await message.channel.send("invalid ttt position")
            elif status == 0: 
                await message.channel.send(format_board(self.game.board))
                if self.state == "ttt1": 
                    self.state = "ttt2"
                    await message.channel.send(f"{self.player_2}'s turn")
                else: 
                    self.state = "ttt1"
                    await message.channel.send(f"{self.player_1}'s turn")
            elif status == 1: 
                await message.channel.send(format_board(self.game.board))
                await message.channel.send(f"Player {self.state[3]} wins!")
                self.state = "message"
            elif status == 2: 
                await message.channel.send(format_board(self.game.board))
                await message.channel.send(f"stalemate!")
                self.state = "message"

def format_board(x):
    return f"```{x[0]} | {x[1]} | {x[2]}\n--+---+--\n{x[3]} | {x[4]} | {x[5]}\n--+---+--\n{x[6]} | {x[7]} | {x[8]} \n```"


# intents = discord.Intents.default()
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
# client = discord.Client(intents=intents)
client.run(token)