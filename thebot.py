#!/usr/bin/python

"""
This bot searches a subreddit for specified term and sends an email notificaiton to defined address.
Use at your own risk. No warranty ^_^
Got suggessions? Have it your way :)
"""

import praw
import time
import datetime
import os
import smtplib
import email.utils
from email.mime.text import MIMEText


#Lets define the agent
agent='Your unique bot agent' + str(datetime.datetime.now()) #and of course adding time to make it more unique
r = praw.Reddit(user_agent=agent)

#Lets define our variables
postids=[]                                       #Bot will not search through posts it's already found results in
toaddr = 'email@something.com'                # Change this
fromaddr = 'email@something.com'                   # Change this
subname = 'subreddit name'                      #without /r/
searchfor = 'your keyword'

while True:

    print("[+] Searching again \n \n \n")
    results = r.search(searchfor, subreddit=subname, limit=0, sort='new')


    for post in results:
        if post.id in open("postids.txt",'r').read():
       #if post.id in postids:  #If we have already looked at this post, ignore it
            print "Post previously found."
            break
        else:
            print(post.title)
            print(post.url)
            postids.append(post.id)
            with open("postids.txt","a") as botfile:
                botfile.write(post.id)
                botfile.close()

            title = post.title
            url = post.url

            #lest create the message
            msg = MIMEText('Post title: ' + title + '\n Post URL: ' + url)
            msg['To'] = email.utils.formataddr(('Recipient', toaddr))
            msg['From'] = email.utils.formataddr(('RedditBot', fromaddr))
            msg['Subject'] = title



            server = smtplib.SMTP('localhost')                           #Change this
            server.set_debuglevel(False) # show communication with the server. Change it to disable smtp debug log.
            try:
                server.sendmail(fromaddr, [toaddr], msg.as_string())
                print "Email sent"
            finally:
                server.quit()

    time.sleep(1800)              #Sleep for 1800 seconds or 30 minutes and search again
