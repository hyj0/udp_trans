import util

BUFLEN  = 3

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
    #md5
    dataMap = {}
    def parsepackage(self, instr):
        oneMap = eval(instr)
        print(oneMap)
        if not self.dataMap.has_key(oneMap['md5']):
            pass
        pass
    pass

if __name__ == '__main__':
    frags = (fragmentstr("1234567890abcdefg", 1))
    print(frags)

    gp = Grouppackage()
    for packet in frags:
        gp.parsepackage(str(packet))
