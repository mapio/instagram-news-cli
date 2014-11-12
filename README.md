Instagram News CLI
==================

This is a quick and dirty hack to read your Instagram news feed from the
command line.

This script gets the data from the undocumented API endpoint [http://instagram.com/api/v1/news/](http://instagram.com/api/v1/news/); since such endpoint does not support OAuth, the script uses [pyCookieCheat.py](https://gist.github.com/n8henrie/8715089) to access the Chrome cookies to simulate an authenticated access; so in order to use this script you first need to login to [http://instagram.com/](http://instagram.com/) using the Chrome browser.

This is a Python3 script (just because `pyCookieCheat.py` is, and I'm too lazy
to backport it to Python2 also);  Installing this script, using `pip`, is as
simple as running

	pip install -r requirements.txt
	python setup.py install

Once insatlled, you can get your Instagram news feed invoking

	instagram-news

that will output something simliar to

	gordongram liked oonamasterchef's photo. 2 hours ago
	gordongram started following oonamasterchef. 2 hours ago
	merujewels liked 8 of bartolo_meru's photos. 5 hours ago
	wireditalia started following mm_cco. 13 hours ago

Since this script is just an hack and does not actually parse the response
text (it just cleans it up a bit), it is possible that if the API will change
the output format the script will break.
