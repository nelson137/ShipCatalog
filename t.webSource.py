import requests, re, codecs
# allStatsPat = '{"id":"\d+","production_status":"[^{]+{([^,]+,){3}'

source = requests.get('https://robertsspaceindustries.com/ship-specs').content.decode()

newlinePat = '\n'
htmlPat = '<!DOCTYPE.+App.app = new |}\);.+<\/html>'
inbetweenPat = '\[{"id":"\d+","slug"(.+?}){86}'
source = re.sub(newlinePat, '', source)
source = re.sub(htmlPat, '', source)
source = re.sub(inbetweenPat, '', source)

allStatsPat = '{"id":"\d+","production_status":"[^{]+{([^,]+,){3}'
allStats = re.findall(allStatsPat, source)

print(len(allStats))

# with codecs.open('/Users/Nelson/Projects/Git/ship-catalog/sources/full-web-source.txt', 'w', 'utf-8') as f:
	# f.write(source)