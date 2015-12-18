# -*- coding: utf-8 -*-

import socket
import sys
import common
import util

if __name__ == '__main__':
    address = ('127.0.0.1', 31500)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    bufstr = util.readfile(sys.argv[2])
    frags = common.fragmentstr(bufstr, sys.argv[1])
    for packet in frags:
        msg = str(packet)
        if not msg:
            break
        s.sendto(msg, address)

    print frags.reverse()
    for packet in frags:
        msg = str(packet)
        if not msg:
            break
        s.sendto(msg, address)

    s.close()
    print 'send ok'
