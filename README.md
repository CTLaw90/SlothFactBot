# SlothFactsBot
The og project. u/SlothFactsBot, sloth fact extraordinaire

## Introduction
Yep. This bot exists to post random sloth facts to unsuspecting users on reddit whenever sloths are mentioned.

This began as a simple project to use the reddit Praw plugin. I've since grown pretty fond of this bot and periodically tweak it. It was originally written in 2.7 and I have since updated it for 3.7. I have also created a discord monitoring bot, so I can check on it on the go.

## The Bot
The reddit bot itself is straigtforward. It utilizes the Praw library inorder to interact with reddit. The main code monitors a comment stream and looks for my keyword 'sloth' and then will attempt to comment a random fact. My facts are kept as a txt file that is broken into a list upon the code start up. It does keep track of which users it has already posted a comment to and won't post multiple to the same author. This is just to prevent single users from spamming a thread with sloth facts. I have the code write to the terminal some information about how many comments its looked through, where its posting the comments and to which user. There are some simple error handling measures included.

The second file here, slothdiscord.py, was my attempt at giving me a way to monitor my script while not at my computer. I have this script serve as the main script I use. On start up it loads as a discord bot into a private channel I have set up. I can then send it commands such as !run which will have the script begin my main poster2.py script. It keeps track of if this script is running through monitoring a .pid file. This bot allows me to start, stop, check runtime, and read error logs directly through discord. I have been running these scripts via a local dropbox folder which further allows me to make edits to the script before remotely starting it again.

## Thoughts
Still a very basic comment posting bot. It originally served as good practice using a new library and has since given me an opportunity to learn some best practices with file monitoring, forced me to be a bit creative with how I want to remotely manage my scripts and given me some insight to updating code from one version of a language to another.
