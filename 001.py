#http://www.pythonchallenge.com/pc/def/274877906944.html
#http://www.pythonchallenge.com/pc/def/map.html
#No need to decode the long text , just the "map" in the url
import string
if __name__=="__main__":
	s="g fmnc wms bgblr rpylqjyrc gr zw fylb. \
	rfyrq ufyr amknsrcpq ypc dmp. \
	bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. \
	sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
	## i hope you didnt translate it by hand. \
	## thats what computers are for. \
	## doing it in by hand is inefficient and that's why this text is so long. \
	## using string.maketrans() is recommended. now apply on the url.
	ts=""
	for ch in s:
		if ('a'<=ch and ch<='z'):
			ch=chr((ord(ch)+2-ord('a'))%26+ord('a'))
		ts+=ch
	print ts
	key="map"
	ts=""
	for ch in key:
		ch=chr((ord(ch)+2-ord('a'))%26+ord('a'))
		ts+=ch
	print ts
	#ocr

	#using string.maketrans() suggested by hint.
	cipher=string.lowercase #"abcdef...xyz"
	t=string.maketrans(cipher,cipher[2:]+cipher[:2]) #create cipher book
	text=s.translate(t)  #decoding
	print text
