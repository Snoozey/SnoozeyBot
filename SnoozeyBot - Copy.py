#This bot is Discord Bot Created by Snoozey.
#Version 1.1
#Date 2/16/2018


import discord
from discord.ext import commands
import random
import urllib.request
import requests
import json
import aiohttp
import asyncio
import async_timeout

description = '''An example bot to showcase the discord.ext.commands extension module.'''
bot = commands.Bot(command_prefix='?', description=description)

#Enter Channel Name you want
channelName = 123
commandList = "fnstat, listcommands, poeitem, poehelp, sotchests, sotskulls "
gameList = "Fortnite, Path of Exile, Sea of Thieves"

@bot.event
async def on_ready():
    print('Logged in as: ' + bot.user.name)
    print('The bot User ID is: ' + str(bot.user.id))
    print('Bot is currently sitting in the channel: ' + str(bot.get_channel(channelName)))
    # print ('The bot is currently using the following API key for fortnite: ' + fortniteTrackerAPI)
    bot.get_channel(channelName)
    print('------')

# @bot.event
# async def on_command_error(ctx,error):
#     if isinstance(error, commands.CommandNotFound):
#         await ctx.channel.send("That command is not known.")
#         await ctx.channel.send("Here is the list of known commands: " + commandList)

@bot.command()
async def fnstat(ctx,fortniteUserName):
    # Enter your fortnite key below
    fortniteTrackerAPI = "key here"
    fortniteURL = "https://api.fortnitetracker.com/v1/profile/pc/" + (fortniteUserName)
    headers = {'TRN-Api-Key': fortniteTrackerAPI}
    #async with aiohttp.get(fortniteURL,headers=headers) as stats:
    async with aiohttp.ClientSession() as sess:
        async with sess.get(fortniteURL,headers=headers) as stats:
            #print (stats.status)
            #print (fortniteURL)
            fnstat = await stats.json()
        soloWins = "0"
        soloKD = "0"
        duoWins = "0"
        duoKD = "0"
        squadWins = "0"
        squadKD = "0"
        try:
            soloWins = fnstat['stats']['p2']['top1']['value']
        except Exception:
            pass
        try:
            soloKD = fnstat['stats']['p2']['kd']['value']
        except Exception:
            pass
        try:
            duoWins = fnstat['stats']['p10']['top1']['value']
        except Exception:
            pass
        try:
            duoKD = fnstat['stats']['p10']['kd']['value']
        except Exception:
            pass
        try:
            squadWins = fnstat['stats']['p9']['top1']['value']
        except Exception:
            pass
        try:
            squadKD = fnstat['stats']['p9']['kd']['value']
        except Exception:
            pass
        fortniteStatResults = (fortniteUserName + ": (SOLO wins: " + soloWins + " & kd: " + soloKD + ")   (DUO wins: " + duoWins
	    + " & kd: " + duoKD + ")   (SQUAD wins: " + squadWins + " & kd: " + squadKD + ")")
        await ctx.channel.send(fortniteStatResults)

@bot.command()
async def listcommands(message):
    await message.channel.send("Hello the list of commands are: " + commandList)

@bot.command()
async def poeitem(ctx, *, item):
    poeWikiURL = ('https://pathofexile.gamepedia.com/' + item)
    await ctx.channel.send(item +": <" + poeWikiURL.replace(" ","_") + ">")
    # async with aiohttp.ClientSession() as sess:
    #     async with sess.get(poeWikiURL) as itemPoe:
    #         print (itemPoe)
    #         #wiki = await itemPoe.json()

@bot.command()
async def sotchests(ctx):
    await ctx.channel.send("Castaway\'s chest is worth 100 gold.")
    await ctx.channel.send("Seafarer\'s chest is worth 200 gold.")
    await ctx.channel.send("Marauder\'s chest is worth 400 gold.")
    await ctx.channel.send("Captain\'s chest is worth 1000 gold.")
    await ctx.channel.send("Chest of a Thousand Grogs\'s chest is worth 1200 gold.")
    await ctx.channel.send("Chest of Sorrow chest is worth 1500 gold.")
    await ctx.channel.send("Stronghold chest is worth 2000 gold.")

@bot.command()
async def sotskulls(ctx):
    await ctx.channel.send("Foul skull is worth 100 gold.")
    await ctx.channel.send("Disgraced skull is worth 250 gold.")
    await ctx.channel.send("Hateful skull is worth 500 gold.")
    await ctx.channel.send("Villainous skull is worth 800-1700 gold.")
    await ctx.channel.send("Stronghold skull is worth 2000-4000 gold.")

@bot.command()
async def games(ctx):
    await ctx.channel.send("I support the following games: " + gameList)

@bot.command()
async def poehelp(ctx):
    poetradeURL = ('http://poe.trade/')
    poeappURL = ('https://poeapp.com/')
    poeLabURL = ('http://www.poelab.com/')
    poeWikiURL = ('https://pathofexile.gamepedia.com/')
    await ctx.channel.send("Path of Exile Trading: <" + poetradeURL + ">" + "or " + "<" + poeappURL + ">")
    await ctx.channel.send("Path of Exile Lab Help: <" + poeLabURL + ">")
    await ctx.channel.send("Path of Exile Lab Help: <" + poeWikiURL + ">")

#Enter your discord code below.
bot.run('discordcode')
