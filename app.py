from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    a = request.json['a']
    b = request.json['b']
    #operator = request.json['operator']

    #if operator == '+':
    result = a + b
    #elif operator == '-':
        #result = a - b
    #elif operator == '*':
        #result = a * b
    #elif operator == '/':
        #result = a / b
    #else:
        #return jsonify({'error': 'Invalid operator'})

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
