import paho.mqtt.client as mqtt
import logging

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

# create connection, the three parameters are broker address, broker port number, keepalive (only broker address and broker port number are required)
client.connect("192.168.1.123", 1883, 60)

topic = "test/message/python"
message = "Hello from Python!"

client.publish(topic, message)

