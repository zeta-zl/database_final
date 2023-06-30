from db import dbop

def _init(user,param="patient"):
    global _global_dict
    if param == "doctor":
        _global_dict = (dbop.findDoctor(user)[0]+(param,))
    else:
        _global_dict = (dbop.findPatient(user)[0]+(param,))
    #print(_global_dict)


def getcuruser():
    return _global_dict[1]

def getcurrentopt():
    return _global_dict[-1]