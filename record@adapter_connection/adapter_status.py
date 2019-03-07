def cmd(obj, _res):
    arg= {}
    if _res['param'] == "1":
        arg['setRecordMode']= 0
        arg['startRecording']= True
    else:
        arg['stopRecording']= True
    obj.execute(arg, _sCB= True)
