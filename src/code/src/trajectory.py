#!/usr/bin/env python

import rospy
from trajectory_msgs.msg import MultiDOFJointTrajectory, MultiDOFJointTrajectoryPoint
from geometry_msgs.msg import Transform, Quaternion
from math import atan2
import math as m

def send_trajectory():

    
    # Create a publisher for the trajectory topic
    trajectory_pub = rospy.Publisher('/firefly1/command/trajectory', MultiDOFJointTrajectory, queue_size=10)
    
    # Wait for the publisher to connect to the topic
    rospy.sleep(1)
    
    # Create a trajectory message
    trajectory_msg = MultiDOFJointTrajectory()
    
    # Set the header information of the message
    trajectory_msg.header.stamp = rospy.Time.now()
    trajectory_msg.header.frame_id = "world"
    
    # Read trajectory points from the text file
    with open('/home/chunchih/final_proj/src/code/src/trajectory.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split(' ')
            time = float(data[0])
            x = float(data[1])
            y = float(data[2])
            z = float(data[3])
            
            # Calculate the yaw angle based on the direction of flight
            if len(trajectory_msg.points) > 0:
                prev_x = trajectory_msg.points[-1].transforms[0].translation.x
                prev_y = trajectory_msg.points[-1].transforms[0].translation.y
                dx = x - prev_x
                dy = y - prev_y
                yaw = atan2(dy, dx)
            else:
                # For the first waypoint, assume initial yaw angle as 0
                yaw = 0.0
            
            point = MultiDOFJointTrajectoryPoint()
            
            transform = Transform()
            transform.translation.x = x
            transform.translation.y = y
            transform.translation.z = z
            
            quat = Quaternion()
            quat.x = 0.0
            quat.y = 0.0
            quat.z = m.sin(yaw / 2.0)
            quat.w = m.cos(yaw / 2.0)
            
            transform.rotation = quat
            
            point.transforms.append(transform)
            point.time_from_start = rospy.Duration(time)
            trajectory_msg.points.append(point)
    
    # Publish the trajectory message
    trajectory_pub.publish(trajectory_msg)
    
    rospy.loginfo("Curve trajectory published!")
    
    # Spin and wait for the node to be shutdown
    rospy.spin()

if __name__ == '__main__':
    # Initialize the ROS node
    rospy.init_node('trajectory', anonymous=True)
    try:
        send_trajectory()
    except rospy.ROSInterruptException:
        pass

