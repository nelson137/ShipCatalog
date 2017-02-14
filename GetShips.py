import requests, re
from myplatform import MyPlatform
from collections import OrderedDict

def getShips(srcLoc, srcType='text'):
    '''Returns OrderedDict of ships from source'''

    def checkNull(stat, isNum=False):
        '''Removes leading '"' if stat not "null"'''
        if isNum:
            return 0 if stat == 'null' else int(stat[1:-1])
        else:
            return 'null' if stat == 'null' else stat[1:-1]

    if srcType == 'html':
        # get raw source code from website
        source = requests.get(srcLoc).content.decode()

        newlinePat = '\n'
        htmlPat = '<!DOCTYPE.+App\.app = new |}\);.+<\/html>'
        inbetweenPat = '\[{"id":"\d+","slug"(.+?}){86}'
        source = re.sub(newlinePat, '', source)
        source = re.sub(htmlPat, '', source)
        source = re.sub(inbetweenPat, '', source)
    else:
        path = MyPlatform().path

        # get raw source code from file
        with open('{}/{}'.format(path, srcLoc), 'r') as f:
            source = f.read()

    # get ships stats from source code
    allStatsPat = r'{"id":"\d+","production_status":"[^{]+{[^[]+'
    #allStatsPat = r'{"id":"\d+","production_status":"[^{]+{([^,]+,){3}'
    allStats = re.findall(allStatsPat, source)

    ships = OrderedDict()

    # patterns for each stat
    modelPat =    r'name":(null|"[^"]+"),"focus'
    mfrPat =      r'name":(null|"[^"]+"),"known_for'
    focusPat =    r'focus":(null|"[^"]+")'
    prodstatPat = r'production_status":(null|"[^"]+")'
    descPat =     r'description":(null|".+"),"tagline' # r'description":(null|"[^"]+"),"tagline'
    cargocapPat = r'cargocapacity":(null|"[^"]+")'
    maxcrewPat =  r'maxcrew":(null|"[^"]+")'

    for index in range(len(allStats)):
        allStats[index] = re.sub(r'\\', '', allStats[index])

        # get stat from source code of each ship
        model =    checkNull(re.search(modelPat, allStats[index]).group(1))
        mfr =      checkNull(re.search(mfrPat, allStats[index]).group(1))
        focus =    checkNull(re.search(focusPat, allStats[index]).group(1))
        prodstat = checkNull(re.search(prodstatPat, allStats[index]).group(1))
        desc =     checkNull(re.search(descPat, allStats[index]).group(1))
        cargocap = checkNull(re.search(cargocapPat, allStats[index]).group(1), True)
        maxcrew =  checkNull(re.search(maxcrewPat, allStats[index]).group(1), True)

        # put stats into OrderedDict
        ships[model] = OrderedDict([('model', model), ('manufacturer', mfr), ('focus', focus), ('production status', prodstat), ('description', desc), ('cargo capacity', cargocap), ('max crew', maxcrew)])

    return ships
