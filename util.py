import md5

def readfile(file):
    f = open(file, 'r')
    src = f.read()
    f.close()
    return src

def writefile(file, src):
    f = open(file, 'w')
    f.write(src)
    f.close()

def md5file(localfile):
    f = open(localfile, 'r')
    src = f.read()
    f.close()
    m1 = md5.new()
    m1.update(src)
    return m1.hexdigest().upper()

def md5str(instr):
    m1 = md5.new()
    m1.update(instr)
    return m1.hexdigest().upper()

if __name__ == '__main__':
    print(md5str(''))
    print(readfile('README.md'))
    print(md5file('README.md'))

    writefile('testW.txt', readfile('README.md'))
