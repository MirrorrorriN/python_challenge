#http://www.pythonchallenge.com/pc/def/274877906944.html
#http://www.pythonchallenge.com/pc/def/map.html
#No need to decode the long text , just the "map" in the url
if __name__=="__main__":
	s="g fmnc wms bgblr rpylqjyrc gr zw fylb. \
	rfyrq ufyr amknsrcpq ypc dmp. \
	bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. \
	sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
	for ch in s:
		ch+=2
	print s
	key="map"
	for ch in key:
		ch+=2
	print key