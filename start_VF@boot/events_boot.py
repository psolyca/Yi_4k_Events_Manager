'''
This script start the stream of the Yi at boot.
Thus, a media viewer can connect to the RTSP server
of the Yi with rtsp://YiIPAddress/live.
This is better to use sta mode for wifi.
'''
class init():
    def __init__(self, obj):
        arg= {}
        arg['startViewFinder']= True
        obj.execute(arg, _sCB= True)
