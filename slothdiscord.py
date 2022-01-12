#PYTHON 3.7
#DISCORD SLOTH BOT MONITOR

import discord
import asyncio
import subprocess
import os
import sys
import time

client = discord.Client()
pidfile = '.\\tmp\\sloth.pid'
errorfile = '.\\tmp\\slothboterr.log'
botfile = 'poster2.py'
outfile = '.\\tmp\\slothout.txt'

proc = False

starttime = time.time()

def readlog():
	global errorfile
	logfile = open(errorfile)
	log = logfile.read()
	log = log.split('\n')
	logfile.close()
	return log

def readout():
	global outfile
	b = open(outfile)
	out = b.read()
	out = out.split('\n')
	b.close()
	return out
	
def readoutlast():
	global outfile
	b = open(outfile)
	out = b.read()
	out = out.split('\n')
	b.close()
	return (out[len(out)-2])

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('-----')
	
@client.event
async def on_message(message):
	global starttime, proc
	if message.content.startswith('!status'):
		if os.path.isfile(pidfile):
			tmp = await client.send_message(message.channel, '%s is currently running' %botfile)
			tmp = await client.send_message(message.channel, time.strftime('uptime - %H:%M:%S', time.gmtime(time.time() - starttime)))
		else:
			tmp = await client.send_message(message.channel, '%s is not running' %botfile)
		
	elif message.content.startswith('!quit'):
		tmp = await client.send_message(message.channel, 'closing %s and exiting' %botfile)
		proc.terminate()
		os.remove(pidfile)
		sys.exit()

	elif message.content.startswith('!kill'):
		if os.path.isfile(pidfile):
			tmp = await client.send_message(message.channel, 'killing %s' %botfile)
			if proc:
				proc.terminate()
			os.remove(pidfile)
		else:
			tmp = await client.send_message(message.channel, '%s is not running. Cannot kill process' %s)
		
	elif message.content.startswith('!run'):
		if os.path.isfile(pidfile):
			tmp = await client.send_message(message.channel, '%s is already running' %botfile)
		else:
			tmp = await client.send_message(message.channel, 'starting %s' %botfile)
			starttime = time.time()
			proc = subprocess.Popen(['py', botfile], creationflags=subprocess.CREATE_NEW_CONSOLE)

	elif message.content.startswith('!error'):
		tmp = await client.send_message(message.channel, 'printing errorfile: %s' %errorfile)
		print(readlog())
		
	elif message.content.startswith('!output'):
		tmp = await client.send_message(message.channel, 'printing outfile: %s' %outfile)
		print(readout())
	
	elif message.content.startswith('!lastout'):
		tmp = await client.send_message(message.channel, 'printing last output from outfile: %s' %outfile)
		print(readoutlast())
		
	elif message.content.startswith('!clearerror'):
		tmp = await client.send_message(message.channel, 'clearing errorfile: %s' %errorfile)	
		os.remove(errorfile)
		
	elif message.content.startswith('!help'):
		tmp = await client.send_message(message.channel, 'options: \n!status - check if script is running \n!run - execute script \n!kill - close the script \n!error - print the error log \n!clearerror - wipe the error log \n!output - print the output file \n!lastout - print the last line of the output file \n!quit - close the script and exit discord')
		
client.run('insert bot id here')