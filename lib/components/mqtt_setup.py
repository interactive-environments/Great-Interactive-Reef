# mqtt_setup.py
import adafruit_connection_manager
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
import adafruit_minimqtt.adafruit_minimqtt as MQTT

class MQTTBroker():

    def __init__(self, wifi, topic, creature):

        try:
            from settings import settings
        except ImportError:
            print("WiFi settings are kept in settings.py, please add or change them there!")
            raise
        self.settings = settings
        self.wifi = wifi
        self.default_topic = topic
        self.client_id = self.settings["mqtt_clientid"]
        # creating a socket pool and ssl context
        pool = adafruit_connection_manager.get_radio_socketpool(self.wifi.esp)
        ssl_context = adafruit_connection_manager.get_radio_ssl_context(self.wifi.esp)

#        MQTT.set_socket(socket, self.wifi.esp)
        self.mqtt_client = MQTT.MQTT(
            client_id = self.client_id,
            broker=settings["mqtt_broker"],
            username=settings["mqtt_broker_user"],
            password=settings["mqtt_broker_password"],
            socket_pool=pool,
            ssl_context=ssl_context,
            socket_timeout=.02
        )

        self.creature = creature

        self.mqtt_client.on_connect = self.connected
        self.mqtt_client.on_disconnect = self.disconnected
        self.mqtt_client.on_message = self.message

        print("Connecting to MQTT broker...")
        self.mqtt_client.connect()

    def message(self, client, topic, message):
        self.creature.message(topic, message)

    ### MQTT connection functions ###
    def connected(self, client, userdata, flags, rc):
        print("Connected to MQTT broker! Listening for topic changes on %s" % self.default_topic)
        client.subscribe("reefcontrol/timeofday")
        client.subscribe("reefcontrol/energy")

    def disconnected(self, client, userdata, rc):
        print("Disconnected from MQTT Broker!")

    def send(self, message):
        self.mqtt_client.publish(self.default_topic, message)

    def loop(self):
        try:
            self.mqtt_client.loop(0.02)
        except (ValueError, RuntimeError) as e:
            print("Failed to get data, retrying\n", e)
            self.wifi.reset()
            self.mqtt_client.reconnect()
