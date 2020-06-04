person = {}

person['Cantones']=[]

b={
    "id":"123",
    "nombre":"juan"
}

# for i in range(100):
#     add={
#         "id":i+1,
#         "codigo":"",
#         "canton":"",
#         "coordenadas":"",
#         "provincias_id":""
#     }
#     person['Cantones'].append(add)

for i in range(20):
    add={
        "id":i+1,
        "codigo":str(101+i),
        "canton":"",
        "coordenadas":"",
        "provincia_id":1
    }
    person['Cantones'].append(add)

for i in range(15):
    asdf={
        "id":i+21,
        "codigo":str(201+i),
        "canton":"",
        "coordenadas":"",
        "provincia_id":2
    }
    person['Cantones'].append(asdf)

for i in range(8):
    add={
        "id":i+36,
        "codigo":str(301+i),
        "canton":"",
        "coordenadas":"",
        "provincia_id":3
    }
    person['Cantones'].append(add)

for i in range(10):
    add={
        "id":i+44,
        "codigo":str(401+i),
        "canton":"",
        "coordenadas":"",
        "provincia_id":4
    }
    person['Cantones'].append(add)

for i in range(11):
    add={
        "id":i+54,
        "codigo":str(501+i),
        "canton":"",
        "coordenadas":"",
        "provincia_id":5
    }
    person['Cantones'].append(add)

for i in range(11):
    add={
        "id":i+65,
        "codigo":str(601+i),
        "canton":"",
        "coordenadas":"",
        "provincia_id":6
    }
    person['Cantones'].append(add)

for i in range(6):
    add={
        "id":i+76,
        "codigo":str(701+i),
        "canton":"",
        "coordenadas":"",
        "provincia_id":7
    }
    person['Cantones'].append(add)
import json

s= json.dumps(person)

# print(s)

#Esta es la dirección de donde uno quiere que aparezca el archivo json
with open("/Users/ravehunter05/Desktop/json_paises/cantones.json","w") as f:
    f.write(s)
