# Put your app in here.
from flask import Flask
from flask import request

app = Flask(__name__)

#initialize dictionary with math operations
from operations import add, sub, mult, div

maths = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

#routing
@app.route('/math/<operation>')
def do_math(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(maths[operation](a,b))
