from dataClass import *
from dbClass import dbClass
import dbop

if __name__ == '__main__':
    db = dbClass()
    db.connectdb()
    data = patient_data(6, "71", 5)
    dbop.insert_into_table("patient", data, True)
    # data = doctor_data()
    # dbop.delete_from_table("doctor", ["doctor_id=1"],True)
    # print(ls)
