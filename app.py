from flask import Flask, request
import json
obj= Flask(__name__)
@obj.route('/')
def home():
    return "Welcome to my home page"
@obj.route('/calculate',methods= ['GET'])
def calculate():
    number1= int(request.json["number1"])
    number2= int(request.json["number2"])
    operator= request.json["operator"]
    if operator== 'add':
        result= number1+number2
    elif operator== 'multiply':
        result= number1*number2
    elif operator== 'divide':
        result= number1/number2
    else:
        result=number1-number2
    return "the operation is {} and the result is {}".format(operator,result)
if __name__== '__main__':   
    obj.run(debug=True)