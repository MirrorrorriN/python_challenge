import pickle
import re
import urllib
def get_challenge(s):
    return urllib.urlopen('http://www.pythonchallenge.com/pc/' + s).read()

if __name__=="__main__":
	p=get_challenge('def/banner.p')
	print p
	data=pickle.loads(p)
	print data[:100]
	print '\n'.join([''.join([p[0] * p[1] for p in row]) for row in data])
