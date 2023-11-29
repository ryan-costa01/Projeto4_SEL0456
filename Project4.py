from flask import Flask, request
from FunctionsAPI import *

app = Flask(__name__)

@app.route("/")
def index():
    
    # Define Variable
    language = "Python"
    company = "Ryan Costa"
    Itemid = 11953369
    micro = 04.4
    

    di = {
        "language": language,
        "company": company,
        "Itemid": Itemid,
        "micro": micro
    }
	
    
    # Return JSON Object
    return di

@app.route("/myapi", methods=['POST'])
def myapi():
    
    di = request.get_json()

    errorAnalise(di)

    for func, value in di.items():
        if func == 'fact':
            di[func] = fact(value)
        elif func == 'fib':
            di[func] = fib(value)
    
    
    # Return JSON Object
    return di

if __name__ == '__main__':
    app.debug = True
    app.run()


#curl -X POST http://127.0.0.1:5000/myapi -H 'Content-Type: application/json' -d '{"fact":Value1,"fib":Value2}'