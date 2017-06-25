import urllib
import re
# def get_challenge(num):
# 	#print ('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % num)
#     return urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % num).read()
# num = 63579
# text = re.compile('and the next nothing is ([0-9]+)')
# page = get_challenge(num)
# while (text.match(page)):
# 	num = text.match(page).group(1)
# 	print num
# 	page = get_challenge(num)
# print num
def get_challenge(num):
    return urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+num).read()

num = '63579'
text = re.compile('and the next nothing is ([0-9]+)')
page = get_challenge(num)
while (text.match(page)):
	num = text.findall(page)[0]
	print num
	page = get_challenge(num)
print page
print num