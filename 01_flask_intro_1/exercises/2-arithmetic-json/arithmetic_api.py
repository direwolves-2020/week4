from flask import Flask, jsonify, request

app = Flask(__name__)
# test this route with localhost:5000/add?num1=5&num2=6

@app.route('/')
def index():
    return "Welcome to calculator"

@app.route('/add')
def add():
    num1 = request.args.get('num1') 
    num2 = request.args.get('num2') 
    expression = num1 + ' + ' + num2
    result = int(num1) + int(num2)
    
    return jsonify(
        expression = expression,
        result = result
    )


@app.route('/subtract')
def substract():
    num1 = request.args.get('num1') 
    num2 = request.args.get('num2') 
    expression = num1 + ' - ' + num2
    result = int(num1) - int(num2)
    
    return jsonify(
        expression = expression,
        result = result
    )


@app.route('/multiply')
def multiply():
    num1 = request.args.get('num1') 
    num2 = request.args.get('num2') 
    expression = num1 + ' * ' + num2
    result = int(num1) * int(num2)
    
    return jsonify(
        expression = expression,
        result = result
    )


@app.route('/divide')
def divide():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    expression = num1 + ' / ' + num2
    result = int(num1) / int(num2)

    return jsonify(
        expression = expression,
        result = result
    )


if __name__ == "__main__":
    app.run(debug=True)
