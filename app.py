from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    a = request.form['a']
    b = request.form['b']
    operator = request.form['operator']

    if operator == '+':
        result = int(a) + int(b)
    elif operator == '-':
        result = int(a) - int(b)
    elif operator == '*':
        result = int(a) * int(b)
    elif operator == '/':
        result = int(a) / int(b)
    else:
        return jsonify({'error': 'Invalid operator'})

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
