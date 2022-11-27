import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist


def callback(data):
    i=0
    #rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    rospy.loginfo(rospy.get_caller_id() + 'I heard x = %f , tetha = %f', data.linear.x, data.angular.z)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    #rospy.Subscriber('/cmd_vel', String, callback)
    rospy.Subscriber('/cmd_vel', Twist, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()