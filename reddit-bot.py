#pip install praw
import praw
import config
import time
import os


def bot_login():
    print "Loggin in..."
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "test-a-bot-dave testing!")
    print "Logged in"

    return r


def run_bot(r):
	print "Obtaining 25 comments..."
    for comment in r.subreddit('test').comments(limit=25) and comment.id not in comments_replied_to and comment.author != r.user.name():
		if "dog" in comment.body:
			print "String with \"dog\" found in comment " + comment.id
			comment.reply("I also love dogs! [Here](http://i.imgur.com/LLgRKeq.jpg) is an image of one!")
			print "Replied to comment " + comment.id

            comments_replied_to.append(comment.id)

            with open("comments_replied_to.txt","a"):
               f.write(comment.id + "\n")

	print "Sleeping for 10 seconds..."
	#Sleep for 10 seconds...
	time.sleep(10)

def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt","r") as f:
        comments_replied_to = f.read()
        comments_replied_to = comments_replied_to.split("\n")

    return comments_replied_to

r = bot_login()
comments_replied_to = []

while True:
	run_bot(r,comments_replied_to)