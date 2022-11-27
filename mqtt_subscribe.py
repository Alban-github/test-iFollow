import paho.mqtt.client as mqtt
import time
from mqtt_publish import topic,mqttBroker
import rospy
#from std_msgs.msg import String
import sys
from geometry_msgs.msg import Twist


# topic="Turtlebot cmd"
# mqttBroker = "mqtt.eclipseprojects.io"


BURGER_MAX_LIN_VEL = 0.22
BURGER_MAX_ANG_VEL = 2.84/2

commands = {    'up arrow':(BURGER_MAX_LIN_VEL,0),
                'down arrow':(-BURGER_MAX_LIN_VEL,0),
                'right arrow':(0,-BURGER_MAX_ANG_VEL),
                'left arrow':(0,BURGER_MAX_ANG_VEL)}

data='no data'

# fonctions mqtt sur trigger :

def on_message(client, userdata, message):
    global data
    data = str(message.payload.decode("utf-8"))
    print("Received message: ", data)

def on_log(client, userdata, level, buf):
    print("log: ",buf)

def on_connect(client, userdata, flags, rc):
   print("connected !!")
   client.connected_flag=True

def on_disconnect(client, userdata, rc):
   print("NOT connected !!")
   print("disconnecting reason  "  +str(rc))


def interpret_data(self,data):
    #twist interpretaion of arrow keys
    if(data in commands):
        x,z=commands[data]
    else:
        x,z=0,0

    twist.linear.x, twist.angular.z = x,z


if __name__ == '__main__':
    
    client = mqtt.Client("ROS TB3")

    client.on_connect = on_connect
    client.on_disconnect = on_disconnect

    client.connect(mqttBroker)
    client.subscribe(topic)

    #talker part :
    
    try :
        chatter_name = sys.argv[1]
    except rospy.ROSInterruptException:
        chatter_name = '/cmd_vel'
    
    pub = rospy.Publisher(chatter_name, Twist, queue_size=10)
    rospy.init_node('web_talker', anonymous=True)
    
    delay_ms=10
    ros_rate = rospy.Rate(10)#00/delay_ms) # 10hz
    twist = Twist()

    client.loop_start()
    prev_time=rospy.get_rostime()
    while not rospy.is_shutdown():
        client.on_message = on_message
        #print(data)
        interpret_data(twist,data)
        if rospy.get_rostime().nsecs>=prev_time.nsecs+delay_ms*1000:
            data='no data'
        #rospy.loginfo("Linear Components: [%f, %f, %f]"%(twist.linear.x, twist.linear.y, twist.linear.z))
        #rospy.loginfo("Angular Components: [%f, %f, %f]"%(twist.angular.x, twist.angular.y, twist.angular.z))
        pub.publish(twist)
        ros_rate.sleep()

        
    time.sleep(0)
    client.loop_stop()
    print("end")

