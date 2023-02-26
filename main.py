import base64
import random

import nextcord
from nextcord.ext import commands
from craiyon import Craiyon
from PIL import Image
from io import BytesIO
import time

bot = commands.Bot(command_prefix="!",intents=nextcord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is up and ready !")

@bot.command()
async def generate(ctx: commands.Context, * ,prompt: str ):
    quotes = [
        "We don't make mistakes, just happy little accidents. - Bob Ross",
        "There's nothing wrong with having a tree as a friend. - Bob Ross",
        "Talent is a pursued interest. - Bob Ross",
        "Let's make some happy little clouds in our world. - Bob Ross",
        "In painting, you have unlimited power. You have the ability to move mountains. - Bob Ross",
        "You can do anything here - the only prerequisite is that it makes you happy. - Bob Ross",
        "Believe that you can do it cause you can do it. - Bob Ross",
        "The secret to doing anything is believing that you can do it. Anything that you believe you can do strong enough, you can do. Anything. - Bob Ross"
    ]

    print(random.choice(quotes))
    ETA = int(time.time()+60)
    msg = await ctx.send(f"{random.choice(quotes)} <t:{ETA}:R>")
    generator=Craiyon()
    result = generator.generate(prompt)
    images = result.images
    for i in images:
        image = BytesIO(base64.decodebytes(i.encode("utf-8")))
        return await msg.edit(content="Content generated by **craiyon.com**",file=nextcord.File(image,"image.png"))

bot.run("TOKEN")
