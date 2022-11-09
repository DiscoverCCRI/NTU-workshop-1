import bme280
import smbus2
import paho.mqtt.client as mqtt
import logging
from datetime import datetime

# define on_connect function
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # subscribe to the specified topic
    client.subscribe(topic)

# define on_publish function
def on_publish(client, userdata, mid):
    """
      Callback function when topic is published.
    """
    logging.info("Data published successfully.")

# define on_subscribe function
def on_subscribe(client, userdata, mid, granted_qos):
    """
      Callback function when topic is subscribed.
    """
    logging.info("Topic successfully subscribed with QoS: %s" % granted_qos)

# the callback function, it will be triggered when receiving messages
def on_message(client, userdata, msg):
    print(f"{msg.topic} {msg.payload}")

#define the publish function
def publish(self, topic, data, qos=1, retain=False):
    """
      Publish to a topic.
    """
    logging.info("Publishing to topic %s" % topic)
    self.client.publish(topic, data, qos=qos, retain=retain)


#create client instance
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.on_subscribe = on_subscribe


def main():
    # create connection, the three parameters are broker address, broker port number, keepalive (only broker address and broker port number are required)
    client.connect("ccrisupe1.iot.nau.edu", 1883, 60)

    # Connect to BME280
    port = 1
    address = 0x77
    bus = smbus2.SMBus(port)

    calibration_params = bme280.load_calibration_params(bus, address)

    bme280_data = bme280.sample(bus, address, calibration_params)

    # Change this to workshop id
    id = bme280_data.id
    timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    humidity = bme280_data.humidity
    pressure = bme280_data.pressure
    ambient_temperature = bme280_data.temperature

    print("Chip ID: " + str(id))
    print("Timestamp: " + str(timestamp))
    print("Humidity: %.2f" % humidity + "% rH")
    print("Atmospheric Pressure: %.2f hPa" % pressure)
    print("Temperature: %.2f °C" % ambient_temperature)

    topic = "sample/bme280"
    message = str(id) + "," + str(timestamp) + "," + str(humidity) + "," + str(pressure) + "," + str(ambient_temperature)

    print(f"\nSending the following string over MQTT on topic {topic}: \n{message}")

    client.publish(topic, message)

if __name__ == "__main__":
    main()