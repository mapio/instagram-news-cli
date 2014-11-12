from requests import Session
import re

from .pyCookieCheat import chrome_cookies

FIND_LI = re.compile( '<li class.*?^</li>', re.S | re.M )
CLEAN_TAGS = re.compile( '<.*?>' )

def main():

	url = 'http://instagram.com/api/v1/news/'

	session = Session()
	cookies = chrome_cookies( url )
	response = session.get( url, cookies = cookies )

	print(
		'\n'.join(
			' '.join( CLEAN_TAGS.sub( '', _ ).split() )
			for _ in FIND_LI.findall( response.text )
			)
		)
