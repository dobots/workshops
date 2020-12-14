#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64
from std_srvs.srv import SetBool

class NumberCounter:

    def __init__(self):
        self.counter = 0
        self.pub = rospy.Publisher("/number_count", Int64, queue_size=10)
        self.number_subscriber = rospy.Subscriber("/number", Int64, self.callback_number)
        self.reset_service = rospy.Service("/reset_counter", SetBool, self.callback_reset_counter)

    def callback_number(self, msg):
        self.counter += msg.data
        new_msg = Int64()
        new_msg.data = self.counter
        rospy.loginfo("Received Data: {}, Counter Value: {}".format(msg.data, new_msg.data))
        self.pub.publish(new_msg)

    def callback_reset_counter(self, req):
        if req.data:
            self.counter = 0
            return True, "Counter has been successfully reset"
        return False, "Counter has not been reset"

class NumberCounter_twice:

    def __init__(self):
        self.counter = 0
        self.pub = rospy.Publisher("/number_count_twice", Int64, queue_size=10) #Different Publisher
        self.number_subscriber = rospy.Subscriber("/number", Int64, self.callback_number)      
        self.reset_service = rospy.Service("/reset_counter_twice", SetBool, self.callback_reset_counter) #Different_service

    def callback_number(self, msg):
        self.counter += 2*msg.data
        new_msg = Int64()
        new_msg.data = self.counter
        rospy.loginfo("Received Data: {}, Counter Value Twice: {}".format(msg.data, new_msg.data))
        self.pub.publish(new_msg)

    def callback_reset_counter(self, req):
        if req.data:
            self.counter = 0
            return True, "Counter has been successfully reset"
        return False, "Counter has not been reset"

if __name__ == '__main__':
    rospy.init_node('number_counter')
    NumberCounter()
    NumberCounter_twice()
    rospy.spin()