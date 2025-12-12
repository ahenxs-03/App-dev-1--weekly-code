# set up 
# build flask based app and integrate api
from flask import Flask 
app=Flask(__name__)
emp_data=[{"id":101,"name":"Sohan Sen","salary":2000000},
          {"id":102,"name":"Ran Son","salary":800000},
          {"id":103,"name":"Sophe Skn","salary":300000},
          {"id":104,"name":"Doe","salary":1000000},
          {"id":105,"name":"Alpha","salary":800000}
          ]
@app.route('/')
def home():
    return "hello"

@app.route('/employee')
def get_employees():
    return emp_data
@app.route('/employee/<int:id>')
def search(id):
    for e in emp_data:
        if e["id"]==id:
            return e
    return {"message":"sorry, %d not found"%(id)},404
app.run(debug=True)