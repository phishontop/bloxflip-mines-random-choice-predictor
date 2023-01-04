import random, discord; from discord.ext import commands as k
b = k.Bot(command_prefix='.', intents=discord.Intents.all())
@b.command()
async def geek_skid(z):
    g = [[":green_square:" for i in range(5)] for x in range(5)]
    for c in range(5): g[c][random.randint(0, 4)] = ":red_square:"
    await z.send("\n".join(["".join(l) for l in g]))
b.run(input("token: ")) # Credits to Vipqix 
