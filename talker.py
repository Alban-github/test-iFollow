
import rospy
from std_msgs.msg import String
import sys
from geometry_msgs.msg import Twist

def talker(id=0):
    chatter_name= '/cmd_local' if (id=='1') else '/cmd_web'
    #print(chatter_name)
    
    
    #pub = rospy.Publisher(chatter_name, String, queue_size=10)
    pub = rospy.Publisher(chatter_name, Twist, queue_size=10)



    rospy.init_node('talker'+str(id), anonymous=True)
    rate = rospy.Rate(1) # 10hz


    twist = Twist()
    twist.linear.x = float(id)-1; twist.linear.y = 0.0; twist.linear.z = 0.0
    twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = float(id)-2
    while not rospy.is_shutdown():
        rospy.loginfo("Linear Components: [%f, %f, %f]"%(twist.linear.x, twist.linear.y, twist.linear.z))
        rospy.loginfo("Angular Components: [%f, %f, %f]"%(twist.angular.x, twist.angular.y, twist.angular.z))
        pub.publish(twist)
        rate.sleep()

'''
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % id 
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
'''

if __name__ == '__main__':
    try:
        talker(sys.argv[1])
    except rospy.ROSInterruptException:
        pass