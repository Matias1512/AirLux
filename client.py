import requests
import random
import time

SERVER_URL = "http://server:5000"  # Remplacez "server" par le nom du conteneur du serveur

def send_random_number():
    random_number = random.randint(1, 100)
    data = {"number": random_number}

    try:
        response = requests.post(f"{SERVER_URL}/receive", json=data)
        if response.status_code == 200:
            print(f"Nombre aléatoire {random_number} envoyé avec succès.")
        else:
            print(f"Erreur lors de l'envoi du nombre aléatoire. Code d'erreur {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erreur de connexion au serveur : {e}")

if __name__ == "__main__":
    while True:
        send_random_number()
        time.sleep(5)  # Envoie un nombre aléatoire toutes les 5 secondes
