#required-->Flask restful
#orm model-->sqlalchemy
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, fields, marshal_with

app=Flask(__name__)#Flask instance
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///employeedb.sqlite3'# db name 
#through flask instance app is created 
#through app.config data base is created
db=SQLAlchemy(app)
#db orm model created
api=Api(app)
#instance of api
#create model
app.app_context().push()

class Employee(db.Model):# parameter
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Integer,primary_key=False)
    salary=db.Column(db.Float,primary_key=False)
#create Api resources
#result json
result_json={
    "id": fields.Integer,
    "name":fields.String,
    "salary":fields.Float
}
class EmployeeAPI(Resource):
    #request method
    @marshal_with(result_json)
    def get(self,id):
        e=db.session.query(Employee).filter(Employee.id==id).first()
        if e:
            return e
        else:
            return {"message":"%s not found"%(id)},404
    def post(self):
        #take json data as input
        name=request.json["name"]
        salary=request.json["salary"]
        e=Employee(name=name,salary=salary)
        db.session.add(e)
        db.session.commit()
        return e
    def put(self,id):
        pass
    def delete(self,id):
        pass
#api routes
api.add_resource(EmployeeAPI,'/api/emp/<int:id>','/api/emp/create')

if __name__=="__main__":
    app.run(debug=True)