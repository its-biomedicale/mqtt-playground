import paho.mqtt.client as mqtt
import json

# Configurazione MQTT
BROKER = "localhost"
PORT = 1883
TOPIC_DATA = "serbatoi/sensori"
CLIENT_ID = "Server_Centrale"

# Callback quando si riceve un messaggio MQTT con i dati dei serbatoi
def on_message(client, userdata, msg):
    # Decodifica il payload del messaggio
    tank_data = json.loads(msg.payload)
    tank_id = tank_data['tank_id']
    water_level = tank_data['water_level']
    
    print(f"[{CLIENT_ID}] Dati ricevuti da {tank_id}: Livello acqua={water_level}%")
    
    # Analisi delle condizioni: invio comandi in base al livello d'acqua
    if water_level < 30:
        send_command(tank_id, "ATTIVA_POMPA")
    elif water_level > 80:
        send_command(tank_id, "DISATTIVA_POMPA")

# Funzione per inviare un comando a un serbatoio
def send_command(tank_id, command):
    command_topic = f"serbatoi/comandi/{tank_id}"
    client.publish(command_topic, command)
    print(f"[{CLIENT_ID}] Comando inviato a {tank_id}: {command}")

# Configurazione del client MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, CLIENT_ID)
client.on_message = on_message  # Associa la funzione on_message come callback

# Connessione al broker e sottoscrizione al topic dei sensori
client.connect(BROKER, PORT, 60)
client.subscribe(TOPIC_DATA)

# Loop principale per mantenere la connessione e ascoltare i messaggi
try:
    print(f"[{CLIENT_ID}] Server in ascolto sui dati dei serbatoi...")
    client.loop_forever()

except KeyboardInterrupt:
    print(f"[{CLIENT_ID}] Chiusura del server MQTT.")
    client.disconnect()
