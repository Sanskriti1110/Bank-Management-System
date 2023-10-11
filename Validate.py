import re
from datetime import datetime

def validate_bname(bname):
    valid_bname = ['HDFC','AXIS','SBI','KOTAK']
    if bname in valid_bname:
        return True
    else:
        return False

def validate_IFSC(ifsc_code):
    ifsc_pattern = r"^[A-Z]{4}0\d{6}$"
    if re.match(ifsc_pattern,ifsc_code):
        return True
    else:
        return False
        
def validate_AccNum(acc_num):
    acc_pattern = r'^\d{8,14}$'
    if re.match(acc_pattern,acc_num):
        return True
    else:
        return False

def validate_name(name):
    parts = name.split()
    if len(parts)<2:
        return False
    for i in parts:
        return i.isalpha()

def validate_gender(gender):
    valid_genders = ['Male','Female','Other']
    if gender in valid_genders:
        return True
    else:
        return False

def validate_accType(acc_type):
    valid_acc_types = ['Savings','Salary','Joint']
    if acc_type in valid_acc_types:
        return True
    else:
        return False
       
def validate_pancard(pancard):
    pancard_pattern = r"^[A-Z]{5}\d{4}[A-Z]$"
    if re.match(pancard_pattern,pancard):
        return True
    else:
        return False
        
def validate_aadhaar(aadhaar):
    aadhaar_pattern = r"^\d{12}$"
    if re.match(aadhaar_pattern,aadhaar):
        return True
    else:
        return False
 
def validate_date(date,date_format='%d-%m-%Y'):
    try:
        datetime.strptime(date, date_format)
        return True
    except ValueError:
        return False
