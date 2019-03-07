import os
import logging

def cmd(obj, _res):
    arg= {}
    file = _res['param'][:-4]
    logging.debug('_res : %s.MP4, %s.SEC' % (file, file))
    if os.path.isfile('/tmp/vfstarted'):
        logging.debug('stopViewFinder')
        os.remove('/tmp/vfstarted')
        arg['stopViewFinder']= True
    else:
        logging.debug('startViewFinder')
        open('/tmp/vfstarted', 'w')
        arg['startViewFinder']= True
    os.remove('%s.MP4' % file)
    os.remove('%s.SEC' % file)
    obj.execute(arg, _sCB= True)
