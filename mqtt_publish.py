import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
import detect_keys

topic="Turtlebot cmd"
mqttBroker = "mqtt.eclipseprojects.io"


def on_log(client, userdata, level, buf):
    print("log: ",buf)

if __name__ == '__main__':

    client = mqtt.Client("Keyboard_cmd")
    client.connect(mqttBroker)

    print("Use directional keys here ...")
    
    fd,old_settings=detect_keys.ini()
    try:
        # Enter raw mode (key events sent directly as characters)
        detect_keys.setraw()

        # Loop, waiting for keyboard input
        while 1:
            #randNumber = uniform(20.0, 21.0)
            #client.on_log=on_log
            read=detect_keys.read_key()
            if read in detect_keys.commands: 
                k=detect_keys.commands[read]
                client.publish(topic, k)
                detect_keys.println("Just published " + k + " to Topic " + topic)
            time.sleep(0.01)

    # Always clean up
    finally:
        detect_keys.end(fd,old_settings)
