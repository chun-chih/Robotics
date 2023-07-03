#!/usr/bin/env python

import rospy
from trajectory_msgs.msg import MultiDOFJointTrajectory, MultiDOFJointTrajectoryPoint
from geometry_msgs.msg import Transform
import math as m

def control_yaw(yaw_angle):
    # Create a ROS publisher to send the trajectory commands
    pub = rospy.Publisher('/firefly1/command/trajectory', MultiDOFJointTrajectory, queue_size=10)
    rospy.init_node('yaw_controller', anonymous=True)
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        # Create a trajectory message
        traj = MultiDOFJointTrajectory()
        traj.header.stamp = rospy.Time.now()
        traj.joint_names.append("firefly1::base_link")

        # Create a trajectory point and set the desired yaw angle
        point = MultiDOFJointTrajectoryPoint()
        point.transforms.append(get_yaw_transform(yaw_angle))
        traj.points.append(point)

        # Publish the trajectory
        pub.publish(traj)
        rate.sleep()

def get_yaw_transform(yaw_angle):
    # Create a transform message with the desired yaw angle
    transform = Transform()
    transform.rotation.x = 0.0
    transform.rotation.y = 0.0
    transform.rotation.z = m.sin(yaw_angle / 2)
    transform.rotation.w = m.cos(yaw_angle / 2)
    return transform

if __name__ == '__main__':
    try:
        # Set the desired yaw angle in radians
        desired_yaw = 1/2*m.pi  # Replace with your desired yaw angle
        control_yaw(desired_yaw)
    except rospy.ROSInterruptException:
        pass
