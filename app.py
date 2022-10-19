from flask import Flask, jsonify, request
import requests, os

# Create flask app
app = Flask(__name__)

# Put apilayer key in app config from env
app.config['API_KEY'] = os.environ.get('API_KEY')


@app.route('/api/rates', methods=['GET'])
def convert_currency():
    print(f'Api key - {app.config["API_KEY"]}')

    request_url = f"https://api.apilayer.com/fixer/convert"
# Get request parameters
    parameters = {'apikey': app.config['API_KEY'],
                  'from': request.args.get('from'),
                  'to': request.args.get('to'),
                  'amount': request.args.get('value')}

# Get response from fixer.io
    request_answer = requests.get(request_url, params=parameters).json()

# Response to client with the result
    return jsonify({'result': request_answer.get("info")['rate']})


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)
