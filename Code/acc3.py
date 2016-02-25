import lsm_ada
from time import sleep
import scrollphat
import sys
import time

lsm = lsm_ada.Adafruit_LSM303()
counter =0
while True:
   acc = lsm.read()
   a_x = acc[0][0]
   a_y = acc[0][1]
   a_z = acc[0][2]
   m_x = acc[1][0]
   m_y = acc[1][1]
   m_z = acc[1][2]
   
   if a_x > -900:
     counter +=1
   print(acc)
   sleep(0.1)
   scrollphat.write_string(str(counter))


   scrollphat.scroll()
   time.sleep(0.1)
