import util

BUFLEN  = 1000

def fragmentstr(inputstr, type):
    retlst = []
    strmd5 = util.md5str(inputstr)

    bufLst = []
    strIndex = 0
    while True:
        onebuf = inputstr[strIndex:strIndex+BUFLEN]
        if len(onebuf) == 0:
            break
        bufLst.append(onebuf)
        strIndex += BUFLEN

    blockId = 0
    for onebuf in bufLst:
        oneMap = {'type':type, 'md5':strmd5, 'blockId':blockId, 'totalBlock':len(bufLst), 'buf':onebuf}
        retlst.append(oneMap)
        blockId = blockId + 1
    return retlst

class Grouppackage():
	#{'md5':{'type':t 'totalBlock':N 'bufLst':{0:'buf0', 1:'buf1', ...}}}
    dataMap = {}

    def parsepackage(self, instr):
        oneMap = eval(instr)
        #print(oneMap)
        if not self.dataMap.has_key(oneMap['md5']):
			self.dataMap[oneMap['md5']] = {'type':oneMap['type'], 'totalBlock':oneMap['totalBlock'], 'bufLst':{oneMap['blockId']:oneMap['buf']}}
        else:
			self.dataMap[oneMap['md5']]['bufLst'][oneMap['blockId']] = oneMap['buf']
        print 'size:', len(self.dataMap[oneMap['md5']]['bufLst'])
        self.checkfinish(oneMap['md5'])

    def checkfinish(self, md5str):
        totalBlock = self.dataMap[md5str]['totalBlock']
        bufLst = self.dataMap[md5str]['bufLst']
        bufstr = ''
        for i in range(0, totalBlock):
            if not bufLst.has_key(i):
                return
            bufstr += bufLst[i]

        print md5str, 'finish:', bufstr
        self.callfun(type, bufstr, md5str)

    def callfun(self, type, bufstr, md5str):
        util.writefile(md5str, bufstr)

    def getpackage(self):
        return self.dataMap

if __name__ == '__main__':
    frags = (fragmentstr("1234567890abcdefg", 1))
    print(frags)

    gp = Grouppackage()
    for packet in frags:
        gp.parsepackage(str(packet))
    print gp.getpackage()
