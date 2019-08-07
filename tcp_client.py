'''
@Author: 华豪
@Date: 2019-08-06 14:26:14
@E-Mail: hh751317151@163.com
@LastEditors: 华豪
@LastEditTime: 2019-08-06 20:58:38
'''

import socket
import time

st = time.time()

sock = socket.socket()
sock.connect(("127.0.0.1", 9999))

# while True:
file_info = sock.recv(247).decode()
# print(file_info)
file_info1 = file_info.split(" ")
file_name = file_info1[0]

lenth = len(file_name)
file_size = file_info[lenth:].strip()
file_size = int(file_size.split(" ")[0])

copy_size = 0
copy_press_old = 0
copy_press_new = 0

print("%s 开始传输..."%file_name)
try:
    with open("E:\\FTP\\"+file_name, "wb") as f:
        while True:
            data = sock.recv(1024)
            if data:            
                f.write(data)
                eet = time.time()
                copy_size += len(data)
                speed = int(copy_size / ((eet-st) *1000))

                t = (file_size - copy_size) / (speed *1000)

                copy_press_new = int(copy_size * 100/ file_size)

                if copy_press_new != copy_press_old:
                    copy_press_old = copy_press_new
                    print("...{a}%...速度为{s}KB/s，预计还剩{t1:.2f}秒...".format(a=copy_press_new,s=speed,t1=t),end='\r')
            else:
                break
    et = time.time()
    print("\n{s} 传输完成，用时{t2:.2f}秒".format(s=file_name,t2=et-st))
except Exception as e:
    print(e)
    # break
sock.close()
