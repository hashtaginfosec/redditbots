import praw
import sys
import random

user_agent_name = 'myReditbot/1.0 by qasimchadhar' + str(random.randint(1, 20000000))
print(user_agent_name)

r = praw.Reddit(user_agent=user_agent_name)

# subreddit = r.get_subreddit("learnpython")
# print("Printing top 10 submissions in /learnpython")
# for submission in subreddit.get_hot(limit=10):
#         # Test if it contains a PRAW-related question
#     print(submission)

# username = 'qasimchadhar'

username = sys.argv[1:]
for each_user in username:
    print("\n Comments found for " + each_user)
    u = r.get_redditor(each_user)
    for comment in u.get_comments(limit=10):
        print(comment.body)

