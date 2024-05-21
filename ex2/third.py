import json

f = open("data/doentes/pg53791.json")
bd = json.load(f)
f.close()

id = 3


for registo in bd:

    ttl = f':Patient{id} a :Patient ;\n   :name "{registo["nome"]}" ;\n'

    for sintoma in registo['sintomas']:
        ttl += f"   :exhibitsSymptom :{sintoma.replace('(', '_').replace(')', '_').replace(' ', '')} ;\n"
    
    ttl = ttl[:-2] + ".\n\n"
    print(ttl)

    id += 1
    
