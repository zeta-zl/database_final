import os
import dbClass

def init():

    db = dbClass.dbClass()
    global global_db
    global_db = {'dbObj':db}

def getValue(s):
    return global_db[s]

init()