import praw
import prawcore
import time
import random
import urllib
import sys
import os
import logging
import atexit
from requests.exceptions import HTTPError

pid = str(os.getpid())
pidfile = '.\\tmp\\sloth.pid'
errorfile = '.\\tmp\\slothboterr.log'
outfile = '.\\tmp\\slothout.txt'

logging.basicConfig(filename=errorfile, level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)

def exitprocedure():
	global a, pidfile, out
	out.close()
	a.close()
	os.unlink(pidfile)

if os.path.isfile(pidfile):
	sys.exit()
	
a = open(pidfile, 'w')
a.write(pid)

raw_facts = open('slothfacts.txt')
list_of_facts = raw_facts.read()
list_of_facts = list_of_facts.split('\n')

r = praw.Reddit( client_id='' , client_secret='', password='', user_agent='', username='')

target_text = ["sloth"]

processed = []
authors = []
submissions = {}

ccount = 0

out = open(outfile, 'w')

print('SlothBot Online')
try:
	while True:
		for c in r.subreddit('all').stream.comments():
			ccount += 1
			print('COMMENTS READ: ', ccount, end='\r')
			try:
				has_trig = any(string in c.body for string in target_text)
				if has_trig and c.id not in processed and (c.author.name != 'SlothFactsBot') and c.author.name not in authors:
					c.reply("Did someone mention sloths?\n Here's a random fact!\n\n" + random.choice(list_of_facts))
					processed.append(c.id)
					authors.append(c.author.name)
					print("posted a fact to: " + c.author.name + " in " + c.subreddit.display_name + " on " + time.asctime())
					out.write("posted a fact to: " + c.author.name + " in " + c.subreddit.display_name + " on " + time.asctime())
									
			except praw.exceptions.APIException as e:
				print('API Error: ', e.message)
				logger.error(e)
				
			except praw.exceptions.ClientException as e:
				print('Client Error: ', e)
				logger.error(e)
				
			except praw.exceptions.PRAWException as e:
				print('PRAW Error: ', e)
				logger.error(e)
				
			except prawcore.exceptions.Forbidden:
				print('403 Banned from Subreddit: ', c.subreddit.display_name)
				continue
			
			except AttributeError:
				print('Attribute Error')
				logger.error('Attribute Error')
				continue
				
			except urllib.error.HTTPError as e:
				if e.code in [429, 500, 502, 503, 504]:
					print("Reddit is down (error %s), sleeping..." % e.code)
					logger.error(e)
					time.sleep(60)
					pass
				else:
					raise
					
finally:
	exitprocedure()
			
atexit.register(exitprocedure)