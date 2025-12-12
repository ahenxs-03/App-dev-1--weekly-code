import json
my_json='{"name" : "Soham Roy", "score" : 99, "stock" : ["NMP","RC","MPL","D11"] }'
#  json.load(my_json)=:parse
use=json.loads(my_json)
print(use)
print(type(use))
print(type(my_json))
#json.dumps:=dict to json
di={
    "name":"Rohan",
    'class':9,
    'pass':True
}
print(json.dumps(di))
print(type(json.dumps(di)))
'''output==:
{'name': 'Soham Roy', 'score': 99, 'stock': ['NMP', 'RC', 'MPL', 'D11']}
<class 'dict'>
<class 'str'>
{"name": "Rohan", "class": 9, "pass": true}#observe True is not supported
<class 'str'>'''
#in python json variable is more likely str