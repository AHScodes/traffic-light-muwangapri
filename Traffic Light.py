import pyfirmata

import time

board = pyfirmata.Arduino("/dev/cu.usbmodem14201")

it = pyfirmata.util.Iterator(board)

it.start()

motion = board.get_pin('a:2:p')

# RL= red light, GL = green light, OL = orange light,

RL = board.digital[1]
GL = board.digital[2]
OL = board.digital[3]


RL2 = board.digital[5]
GL2 = board.digital[6]
OL2 = board.digital[7]



while True:
    work = motion.read()
    #Make it green all the time, busy street always green quit street == red.
   # 0 or 1 and timer
    print(work)
#If motions is sensed busy street turns red
    if work:
        time.sleep(10)
        GL.write(0)
        OL.write(1)
        time.sleep(5)
        OL.write(0)
        RL.write(1)

        GL2.write(1)

    else:

        GL.write(1)