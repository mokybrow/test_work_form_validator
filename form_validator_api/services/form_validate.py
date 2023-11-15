import json
from tinydb import TinyDB, Query
import re
from datetime import datetime, date


async def form_validate_op(form: dict) -> dict:
    db = TinyDB('db.json')
    pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
    phone_pattern = r'^(7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$'

    for key, value in form.items():
        if re.match(pattern, value) is not None:
            form[f'{key}'] = 'email'
        date_format1 = '%Y-%m-%d'
        date_format3 = '%Y.%m.%d'
        date_format2 = '%d-%m-%Y'
        date_format4 = '%d.%m.%Y'
        try:
            dateObject = datetime.strptime(value, date_format1)
            form[f'{key}'] = 'date'
        except:
            pass
        try:
            dateObject = datetime.strptime(value, date_format2)
            form[f'{key}'] = 'date'
        except:
            pass
        try:
            dateObject = datetime.strptime(value, date_format3)
            form[f'{key}'] = 'date'
        except:
            pass
        try:
            dateObject = datetime.strptime(value, date_format4)
            form[f'{key}'] = 'date'
        except:
            pass
        if re.match(phone_pattern, value) is not None:
            form[f'{key}'] = 'phone'

        if (form[key] != 'email') & (form[key] !=  'date' ) & (form[key] !=  'phone'):
            form[key] = 'str'
    all_rows = db.all()
    money_counter = {}    
    for j in all_rows:
        count = 0 
        for key, value in j.items():
            if key in form:
                if form[key]==value:
                    count +=1
        money_counter[j['name']] = count

    # max_key = max(money_counter, key=money_counter.get)
    # print(max_key)
    inverse = [(value, key) for key, value in money_counter.items()]
    max_key = max(inverse)
    if max_key[0] == 0:
        return(form)
    return max_key[1]

    
