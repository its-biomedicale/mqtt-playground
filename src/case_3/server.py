import paho.mqtt.client as mqtt
import json

# Callback quando si riceve un messaggio MQTT
def on_message(client, userdata, msg):
    # Decodifica il payload del messaggio
    drone_data = json.loads(msg.payload)
    print(f"Dati ricevuti dal {drone_data['drone_id']}: Temperatura={drone_data['temperature']}°C, Umidità={drone_data['humidity']}%")
    
    # Applica una logica per inviare comandi se la temperatura supera una certa soglia
    if drone_data['temperature'] > 30.0:
        send_command(drone_data['drone_id'], "ATTENZIONE: Temperatura elevata!")
    
# Funzione per inviare un comando al drone
def send_command(drone_id, message):
    command_topic = f"droni/comandi/{drone_id}"
    client.publish(command_topic, message)
    print(f"Comando inviato al {drone_id}: {message}")

# Configurazione MQTT
BROKER = "localhost"
PORT = 1883
TOPIC = "droni/sensori"
CLIENT_ID = "Server_Centrale"

# Configurazione del client MQTT
client = mqtt.Client(CLIENT_ID)
client.on_message = on_message  # Associa la funzione on_message come callback

# Connessione al broker e sottoscrizione al topic dei sensori
client.connect(BROKER, PORT, 60)
client.subscribe(TOPIC)

# Loop principale per mantenere la connessione e ascoltare i messaggi
try:
    print("Server in ascolto sui dati dei droni...")
    client.loop_forever()

except KeyboardInterrupt:
    print("Chiusura del server MQTT.")
    client.disconnect()
