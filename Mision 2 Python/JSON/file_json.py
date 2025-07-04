import json
with open('archivo.json', 'r') as file:
    data = json.load(file)
print(data)

my_data = [{'nombre': 'Juan', 'edad': 30, 'valor': 890},
           {'nombre': 'Leo', 'edad': 50, 'valor': 600}]


with open('otro_archivo.json','w') as file:
    json.dump(my_data, file, indent=4)
