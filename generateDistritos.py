person = {}

person['Distritos']=[]

valor = 0
# for i in range(11):
#     add={
#         "id":i+1,
#         "codigo":str(101*100+i),
#         "distrito":"",
#         "coordenadas":"",
#         "provincia_id":"101",
#         "canton_id":"1"
#     }
#     person['Cantones'].append(add)

def generar_distritos(rango, provincia, canton,cCanton):
    for i in range(rango):
        global valor
        add={
            "id":valor + 1,
            "codigo":str(cCanton*100+i+1),
            "distrito":"",
            "coordenadas":"",
            "provincia_id":provincia,
            "canton_id":canton
        }
        person['Distritos'].append(add)
        valor+=1

# San José
generar_distritos(11,1,1,101)
generar_distritos(3,1,2,102)
generar_distritos(13,1,3,103)
generar_distritos(9,1,4,104)
generar_distritos(3,1,5,105)
generar_distritos(7,1,6,106)
generar_distritos(5,1,7,107)
generar_distritos(7,1,8,108)
generar_distritos(6,1,9,109)
generar_distritos(5,1,10,110)
generar_distritos(5,1,11,111)
generar_distritos(5,1,12,112)
generar_distritos(5,1,13,113)
generar_distritos(3,1,14,114)
generar_distritos(4,1,15,115)
generar_distritos(5,1,16,116)
generar_distritos(3,1,17,117)
generar_distritos(4,1,18,118)
generar_distritos(11,1,19,119)
generar_distritos(6,1,20,120)

# Alajuela
generar_distritos(14,2,21,201)
generar_distritos(13,2,22,202)
generar_distritos(8,2,23,203)
generar_distritos(3,2,24,204)
generar_distritos(8,2,25,205)
generar_distritos(7,2,26,206)
generar_distritos(7,2,27,207)
generar_distritos(5,2,28,208)
generar_distritos(5,2,29,209)
generar_distritos(13,2,30,210)
generar_distritos(7,2,31,211)
generar_distritos(5,2,32,212)
generar_distritos(7,2,33,213)
generar_distritos(4,2,34,214)
generar_distritos(3,2,35,215)

# Cartago
generar_distritos(11,3,36,301)
generar_distritos(5,3,37,302)
generar_distritos(8,3,38,303)
generar_distritos(3,3,39,304)
generar_distritos(12,3,40,305)
generar_distritos(3,3,41,306)
generar_distritos(5,3,42,307)
generar_distritos(4,3,43,308)

#Heredia
generar_distritos(5,4,44,401)
generar_distritos(6,4,45,402)
generar_distritos(8,4,46,403)
generar_distritos(6,4,47,404)
generar_distritos(5,4,48,405)
generar_distritos(4,4,49,406)
generar_distritos(3,4,50,407)
generar_distritos(3,4,51,408)
generar_distritos(1,4,52,409)
generar_distritos(5,4,53,410)

# Guanacaste
generar_distritos(5,5,54,501)
generar_distritos(7,5,55,502)
generar_distritos(9,5,56,503)
generar_distritos(4,5,57,504)
generar_distritos(4,5,58,505)
generar_distritos(5,5,59,506)
generar_distritos(4,5,60,507)
generar_distritos(7,5,61,508)
generar_distritos(6,5,62,509)
generar_distritos(4,5,63,510)
generar_distritos(4,5,64,511)

# Puntarenas
generar_distritos(16,6,65,601)
generar_distritos(5,6,66,602)
generar_distritos(9,6,67,603)
generar_distritos(3,6,68,604)
generar_distritos(5,6,69,605)
generar_distritos(3,6,70,606)
generar_distritos(4,6,71,607)
generar_distritos(5,6,72,608)
generar_distritos(1,6,73,609)
generar_distritos(4,6,74,610)
generar_distritos(2,6,75,611)

# Limon
generar_distritos(4,7,76,701)
generar_distritos(6,7,77,702)
generar_distritos(6,7,78,703)
generar_distritos(4,7,79,704)
generar_distritos(3,7,80,705)
generar_distritos(5,7,81,706)





import json

s= json.dumps(person)

# print(s)

#Esta es la ruta donde debería aparecer el archivo json
with open("/Users/ravehunter05/Desktop/json_paises/distritos.json","w") as f:
    f.write(s)
