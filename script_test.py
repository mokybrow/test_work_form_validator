import httpx

params = [{'fname': 'Mikhail', 'birthdate': '08-03-1992', 'email': 'mokybrow@gmail.com'}, 
          {'fname': 'Mikhail', 'birthdate': '08-03-2002', 'phone': '+79622647929'}, 
          {"aboba": "mckenzi", "phone": "666"}, {},
          {'surname': "Ivanov", 'education': 'college', "birthdate": "12.03.2013"}]
for i in params:
    r = httpx.post('http://127.0.0.1:8000/get_form', params=i)

    print(r.content)