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
agent='Your reddit agent string. Make it unique' + str(datetime.datetime.now()) //and ofcourse adding time to make it more unique
r = praw.Reddit(user_agent=agent)

#Lets define our variables
postids=[]                                       #Bot will not search through posts it's already found results in
toaddr = 'youremail@address.com'                # Change this
fromaddr = 'sender@email.com'                   # Change this
subname = 'SUBREDDIT NAME'
searchfor = 'YOUR SEARCH TERM'

while True:
    
    print("[+] Searching again \n \n \n")
    results = r.search(searchfor, subreddit=subname, limit=0, sort='new')
    
    
    for post in results:
    
        if post.id in postids:  #If we have already looked at this post, ignore it
            break
        else:
            print(post.title)
            print(post.url)
            postids.append(post.id)
            title = post.title
            url = post.url

            #lest create the message
            msg = MIMEText('Post title: ' + title + '\n Post URL: ' + url)
            msg['To'] = email.utils.formataddr(('Recipient', toaddr))
            msg['From'] = email.utils.formataddr(('RedditBot', fromaddr))
            msg['Subject'] = title



            server = smtplib.SMTP('YOUR SMTP SERVER')                           #Change this
            server.set_debuglevel(True) # show communication with the server. Change it to disable smtp debug log.
            try:
                server.sendmail(fromaddr, [toaddr], msg.as_string())
            finally:
                server.quit()



    time.sleep(1800)              #Sleep for 1800 seconds or 30 minutes and search again
