#!/usr/bin/env python

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
from std_msgs.msg import String


class Robot():

    def __init__(self):
        # In ROS, nodes are uniquely named. If two nodes with the same
        # name are launched, the previous one is kicked off. The
        # anonymous=True flag means that rospy will choose a unique
        # name for our 'listener' node so that multiple listeners can
        # run simultaneously.

        #Initializing ros nodes
        rospy.init_node('robot', anonymous=True)

        # Initialize publishers/subscribers.
        rospy.Subscriber('chatter', String, self.callback)
        self.robot_say_pub = rospy.Publisher('/qt_robot/speech/say', String, queue_size=10)


        # rate = rospy.Rate(10) # 10hz
        # # # # # # # # # # # # while not rospy.is_shutdown():
            # rate.sleep()


        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()


    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

        a = data.data
        # Parse the data to its components.
        sfname, slname, sgender, sbirth_date, sleft_right_handed, scountry, scity, sgame, slevel, sresult = a.strip().split()

        if sresult == 'w':
            # publish a text message to TTS (non-blocking)
            s = "congrats! You win"
            self.robot_say_pub.publish(s)
            rospy.loginfo(s)

        elif sresult == 'f':
            # publish a text message to TTS (non-blocking)
            s = "you need to try again. good job!"
            self.robot_say_pub.publish(s)
            rospy.loginfo(s)

        else:
            print("error")


if __name__ == '__main__':
    try:
        r = Robot()
    except rospy.ROSInterruptException:
        pass