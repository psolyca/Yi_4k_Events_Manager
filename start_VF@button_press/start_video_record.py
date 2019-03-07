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
