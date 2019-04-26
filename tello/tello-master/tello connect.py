import tello
import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(threadName)s %(message)s')
log=logging.getLogger('Drone app')
log.info('Starting')
#netstat -a get IP and port
t= tello.Tello('0.0.0.0',135)
#t.takeoff()
#time.sleep(.4)
#t.land()



#move_forward(5)
