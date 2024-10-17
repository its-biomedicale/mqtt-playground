import paho.mqtt.client as mqtt
import random
import time
import json

# Configurazione MQTT
BROKER = "localhost"
PORT = 1883
TOPIC_DATA = "serbatoi/sensori"
TOPIC_COMMAND = "serbatoi/comandi/Tank_1"
CLIENT_ID = "Tank_1"

# Funzione per simulare i dati del serbatoio
def get_tank_data():
    return {
        "tank_id": "Tank_1",
        "water_level": random.randint(0, 100),  # Simula il livello d'acqua tra 0% e 100%
    }

# Callback per gestire i messaggi dal server
def on_message(client, userdata, message):
    command = message.payload.decode()
    print(f"[{CLIENT_ID}] Comando ricevuto dal server: {command}")
    if command == "ATTIVA_POMPA":
        print("[{CLIENT_ID}] Pompa attivata per riempire il serbatoio.")
    elif command == "DISATTIVA_POMPA":
        print("[{CLIENT_ID}] Pompa disattivata.")

# Connessione al broker MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, CLIENT_ID)
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.subscribe(TOPIC_COMMAND)  # Sottoscrizione per ricevere comandi dal server

# Loop principale per inviare dati periodici e ascoltare i comandi
try:
    client.loop_start()  # Avvia il loop per gestire i messaggi in background

    while True:
        # Simula la raccolta dei dati del serbatoio
        tank_data = get_tank_data()

        # Converte i dati in formato JSON
        tank_data_json = json.dumps(tank_data)

        # Pubblica i dati al server MQTT
        client.publish(TOPIC_DATA, tank_data_json)
        print(f"[{CLIENT_ID}] Dati inviati: {tank_data_json}")

        # Attende 5 secondi prima di inviare nuovi dati
        time.sleep(5)

except KeyboardInterrupt:
    print("[{CLIENT_ID}]Chiusura del client MQTT.")
    client.loop_stop()
    client.disconnect()
