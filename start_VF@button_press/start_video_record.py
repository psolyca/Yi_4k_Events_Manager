'''
These scripts start the stream of the Yi when the button is pushed.
Thus, a media viewer can connect to the RTSP server
of the Yi with rtsp://YiIPAddress/live.
This is better to use sta mode for wifi.
'''
import os
import logging
import time
import subprocess

def cmd(obj, _res):
    arg= {}
    if os.path.isfile('/tmp/vfstarted'):
        logging.debug('Button pushed to stop VF.')
    else:
        logging.debug('Button pushed to start VF.')
    time.sleep(2) 
    logging.debug('SendToRTOS record')
    subprocess.call(['/usr/bin/SendToRTOS', 'record'])
    obj.execute(arg, _sCB= True)
