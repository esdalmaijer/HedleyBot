# This thing started with this tweet, if you're looking for someone to blame:
# https://twitter.com/jlsinc/status/798142993651867648


import time

from markovbot import MarkovBot
from secret import cons_key, cons_secret, access_token, access_token_secret

# Initialise a MarkovBot instance.
print(u"\nInitialising a new MarkovBot.")
tweetbot = MarkovBot()

# Generate a dict for all possible responses.
respdict = {u'Kendrick Lamar':( \
	u'HEDLEY! https://www.youtube.com/watch?v=8vjEnkQdaHM',
	u'HEDLEY! http://jpg.party/http://i.imgur.com/lzLPfT3.gif',
	u'HEDLEY! http://jpg.party/http://i.imgur.com/nAV7ueU.gif',
	u'HEDLEY! http://jpg.party/http://i.imgur.com/3yt4gex.jpg',
	u'HEDLEY! http://jpg.party/http://i.imgur.com/6COCqT1.jpg',
	u'HEDLEY! http://jpg.party/http://i.imgur.com/C9pcsJI.jpg'
	)}

# Add the respdict to the bot's database.
tweetbot.set_simple_responses(respdict)

# Log in to Twitter.
print(u"\nBot is logging in to Twitter.")
tweetbot.twitter_login(cons_key, cons_secret, \
	access_token, access_token_secret)

# Start auto-responding to tweets.
print(u"\nBot is starting the auto-replying Thread.")
tweetbot.twitter_autoreply_start(u'Kendrick Lamar', database=u'simpleresponse',
	keywords=None, prefix=None, suffix=u'#HeldeyLamar', maxconvdepth=None)

# Run for 10 seconds.
time.sleep(60)
tweetbot.twitter_autoreply_stop()
## Run indefinitively
#while True:
#	# Sleep for a minute, to avoid wasting resources.
#	time.sleep(60)
	