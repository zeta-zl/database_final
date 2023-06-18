"""
primary_key_dict:字典，key是table名，value是其主键名
dataClass：数据类，通过构造其子类创建记录，相dbop中的函数传入类以对数据库操作
"""

primary_key_dict = \
    {
        'doctor': ["doctor_id"],
        'department': ["department_managerid"],
        'patient': ["patient_id"],
        'admission_form': ["doctor_id", "patient_id"],
        'pharmacy': ["pharmacy_id"],
        'medicine': ["pharmacy_id", "medicine_id"],
        'medical_orders': ["medical_ordersid"],
        'registration_form': ["Registration_id"]
    }


class dataClass:
    def __init__(self):
        pass

    def to_dic(self):
        return self.__dict__


class doctor_data(dataClass):
    def __init__(self,
                 doctor_id,
                 doctor_name=None,
                 doctor_gender=None,
                 doctor_age=None,
                 doctor_title=None,
                 doctor_fee=None,
                 doctor_dept=None
                 ):
        super().__init__()

        self.doctor_id = doctor_id
        self.doctor_name = doctor_name
        self.doctor_gender = doctor_gender
        self.doctor_age = doctor_age
        self.doctor_title = doctor_title
        self.doctor_fee = doctor_fee
        self.doctor_dept = doctor_dept


class department_data(dataClass):
    def __init__(self,
                 department_name,
                 department_telephone=None,
                 department_managerid=None
                 ):
        super().__init__()

        self.department_name = department_name
        self.department_telephone = department_telephone
        self.department_managerid = department_managerid


class patient_data(dataClass):
    def __init__(
            self,
            patient_id,
            patient_name=None,
            patient_idnumber=None,
            patient_telephone=None,
            patient_money=500
    ):
        super().__init__()

        self.patient_id = patient_id
        self.patient_name = patient_name
        self.patient_idnumber = patient_idnumber
        self.patient_telephone = patient_telephone
        self.patient_money = patient_money


class admission_form_data(dataClass):
    def __init__(
            self,
            doctor_id,
            patient_id,
            admission_date=None,
            admission_department=None
    ):
        super().__init__()

        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.admission_date = admission_date
        self.admission_department = admission_department


class pharmacy_data(dataClass):
    def __init__(
            self,
            pharmacy_id,
            pharmacy_name=None):
        super().__init__()

        self.pharmacy_id = pharmacy_id
        self.pharmacy_name = pharmacy_name


class medicine_data(dataClass):
    def __init__(
            self,
            pharmacy_id,
            medicine_id,
            medicine_category=None,
            medicine_name=None,
            medicine_price=None,
            medicine_stock=None
    ):
        super().__init__()

        self.pharmacy_id = pharmacy_id
        self.medicine_id = medicine_id
        self.medicine_category = medicine_category
        self.medicine_name = medicine_name
        self.medicine_price = medicine_price
        self.medicine_stock = medicine_stock


class medical_orders_data(dataClass):
    def __init__(
            self,
            medical_ordersid,
            medicine_id,
            patient_id,
            num,
            doctor_id,
            text=None
    ):
        super().__init__()

        self.medical_ordersid = medical_ordersid
        self.medicine_id = medicine_id
        self.patient_id = patient_id
        self.num = num
        self.text = text
        self.doctor_id = doctor_id
        self.order_date = None


class registration_form_data(dataClass):
    def __init__(self,
                 registration_id,
                 patient_id=None,
                 registration_date=None):
        super().__init__()

        self.registration_id = registration_id
        self.patient_id = patient_id
        self.registration_date = registration_date


if __name__ == '__main__':
    doc = doctor_data(1, 2, 3, 4)
    ls = [(k, v) for k, v in doc.to_dic().items()]
    print(ls)
