from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['DEBUG'] = True

received_numbers = []

@app.route('/receive', methods=['POST'])
def receive_number():
    data = request.get_json()
    received_number = data.get("number")

    received_numbers.append(received_number)

    print(received_numbers)
    print(f"Nombre reçu : {received_number}")
    return jsonify({"message": "Nombre reçu avec succès"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
