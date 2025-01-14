import json

json_string = '''
{
    "name": "John",
    "age": 30,
    "city": "New York"
} 
'''

data = json.loads(json_string) # loads is used to convert a json string to a dictionary
data['test'] = True
new_json = json.dumps(data, indent=2) # dumps is used to convert a dictionary to a json string


############## json files
with open('data.json', 'r') as file:
    data = json.load(file)