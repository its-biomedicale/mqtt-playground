import paho.mqtt.client as mqtt
import random
import time
import json

# Funzione per simulare i dati del drone
def get_drone_data():
    return {
        "drone_id": CLIENT_ID,
        "temperature": round(random.uniform(20.0, 35.0), 2),  # Simula una temperatura tra 20°C e 35°C
        "humidity": random.randint(30, 80),  # Simula umidità tra 30% e 80%
    }

# Callback quando si riceve un messaggio MQTT
def on_message(client, userdata, msg):
    print(f"Dati ricevuti: {msg.payload}")

# Configurazione MQTT
BROKER = "localhost"  # Si assume che il broker sia in esecuzione sulla macchina locale
PORT = 1883
TOPIC = "droni/sensori"
CLIENT_ID = "Drone_1"

# Connessione al broker MQTT
client = mqtt.Client(CLIENT_ID)
client.connect(BROKER, PORT, 60)
client.subscribe(f"droni/comandi/{CLIENT_ID}")
client.on_message = on_message  # Associa la funzione on_message come callback

# Loop principale per inviare dati ogni 5 secondi
try:
    while True:
        # Simula la raccolta dei dati del drone
        drone_data = get_drone_data()

        # Converte i dati in formato JSON
        drone_data_json = json.dumps(drone_data)

        # Pubblica i dati al server MQTT
        client.publish(TOPIC, drone_data_json)
        print(f"Dati inviati: {drone_data_json}")

        # Attende 5 secondi prima di inviare i nuovi dati
        time.sleep(5)

except KeyboardInterrupt:
    print("Chiusura del client MQTT.")
    client.disconnect()
