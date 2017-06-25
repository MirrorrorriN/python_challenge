import urllib
import re
src = 'http://www.pythonchallenge.com/pc/def/equality.html'
page = urllib.urlopen(src).read()
text = re.compile('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')
ans = text.findall(page)
print ''.join(ans)