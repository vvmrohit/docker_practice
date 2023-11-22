from flask import Flask, request, jsonify
import random

app = Flask(__name__, static_url_path='/static')

secret_number = random.randint(1,100)  # The secret number to guess

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/guess', methods=['POST'])
def check_guess():
    guessed_number = int(request.json['guess'])
    
    if guessed_number > secret_number:
        result = 'Too high! Try a smaller number.'
    elif guessed_number < secret_number:
        result = 'Too low! Try a larger number.'
    else:
        result = 'Congratulations! You guessed the number!'
    
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
