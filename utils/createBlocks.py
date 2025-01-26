import json

# Créer des blocs dans la config juste en entrant des valeurs dans le Terminal ( simplifier le travail )
name = str(input("Entrez le nom du bloc : "))
texture = str(input("Entrez la texture du bloc : "))
price = int(input("Entrez le prix du bloc : "))

bloc = {name: {
    "name": name,
    "texture": texture,
    "price": price
}}

with open('configs/blocs.json', "r") as f:
    data = json.load(f)


with open('configs/blocs.json', "w") as f:
    
    if data != {}:
        for i, j in data.items():
            bloc[i] = j
    
    json.dump(bloc, f)

