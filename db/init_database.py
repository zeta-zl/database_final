import dbClass


def _init_database():
    sql_ls = [
        '''use `hospital`;''',
        '''create table `doctor`(
        `doctor_id` VARCHAR(20) primary key,
        `doctor_name` VARCHAR(20),
        `doctor_gender` varchar(1),
        `doctor_age` INT,
        `doctor_title` varchar(20),
        `doctor_fee` INT,
        `doctor_dept` varchar(20)
    );
        ''', '''
create table `department`(
    `department_name` varchar(20) primary key, 
    `department_telephone` varchar(20), 
    `department_managerid` varchar(20),
    foreign key(`department_managerid`) references `doctor`(`doctor_id`) on delete set null
);
    ''', '''
create table `patient`(
	`patient_id` VARCHAR(20) primary key,
    `patient_name` varchar(20),
    # `patient_gender` varchar(20),
    `patient_idnumber` varchar(20),
    `patient_telephone` varchar(20),
    `patient_money` INT default 500
);
    ''', '''
create table `admission_form`(
	`doctor_id` varchar(20),
    `patient_id` varchar(20),
    `admission_date` date,
    `admission_department` varchar(20),
    foreign key(`admission_department`) references `department`(`department_name`) on delete CASCADE,
    primary key(`doctor_id`,`patient_id`)
);
    ''', '''
create table `pharmacy`(
	`pharmacy_id` varchar(20) primary key,
    `pharmacy_name` varchar(20)
);
    ''', '''
create table `medicine`(
	`pharmacy_id` varchar(20),
    `medicine_id` varchar(20),
    `medicine_category` varchar(20),
    `medicine_name` varchar(20),
    `medicine_price` varchar(20),
    `medicine_stock` int,
    primary key(`pharmacy_id`,`medicine_id`),
    foreign key(`pharmacy_id`) references `pharmacy`(`pharmacy_id`) on delete cascade
);
    ''', '''
CREATE TABLE `medical_orders` (
  `medical_ordersid` INT PRIMARY KEY,
  `medicine_id` varchar(20),
  `patient_id` varchar(20),
  `num` int not null,
  `text` TEXT,
  `doctor_id` varchar(20) NOT NULL,
  `order_date` timestamp default current_timestamp
);
    ''', '''
create table `registration_form`(
	`Registration_id` varchar(20) primary key,
    `patient_id` varchar(20),
    `Registration_date` timestamp default current_timestamp
);
    ''', '''
    CREATE TABLE doctor_accounts (
    doctor_id VARCHAR(20) PRIMARY KEY,
  password VARCHAR(70) NOT NULL
);''', '''
    CREATE TABLE patient_accounts (
  patient_id VARCHAR(20) PRIMARY KEY,
  password VARCHAR(70) NOT NULL
);'''
    ]

    db = dbClass.dbClass()
    for sql in sql_ls:
        db.execute(sql, commit=True)
    db.commit()


def init_database():
    db = dbClass.dbClass()
    db.init_db()
    result = db.connectdb()
    if result:
        sql = 'select TABLE_NAME from information_schema.tables where table_schema="hospital"'
        result = db.query(sql)
        print(result)
        if len(result) == 10:  # 已经创建好数据库
            return
        else:
            _init_database()
    else:
        print("数据库连接失败")


if __name__ == '__main__':
    init_database()
