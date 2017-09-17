#http://www.pythonchallenge.com/pc/def/ocr.html
import urllib
import re
def get_challenge(s):
    return urllib.urlopen('http://www.pythonchallenge.com/pc/' + s).read()
    
if __name__=="__main__":
    src = get_challenge('def/ocr.html')
    text = re.compile('<!--((?:[^-]+|-[^-]|--[^>])*)-->', re.S).findall(src)[-1]   #Why this RegEx? Exclude the first annoatation part 
    counts = {}
    for c in text: counts[c] = counts.get(c, 0) + 1
    print counts
    print ''.join(re.findall('[a-z]', text))
