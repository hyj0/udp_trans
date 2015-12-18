# -*- coding: utf-8 -*-

import socket
import common
import util
import thread
import threadQue

if __name__ == '__main__':
    address = ('127.0.0.1', 31500)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(address)

    thread.start_new_thread(threadQue.work, (None,))
    #gp = common.Grouppackage()
    while True:
        data, addr = s.recvfrom(2048)
        if not data:
            print "client has exist"
            break
        print "received:", data, "from", addr
        #gp.parsepackage(data)
        threadQue.q.put(data)

    s.close()
