#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Pose
from trajectory_msgs.msg import MultiDOFJointTrajectory, MultiDOFJointTrajectoryPoint
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from geometry_msgs.msg import Transform
import math as m

yaw = 0.0  # Initialize the yaw variable

def callback(pose):
    global yaw  # Declare the variable as global to modify its value
    # Extract position and orientation from the received pose message
    position = pose.position
    orientation = pose.orientation

    # Convert orientation from quaternion to Euler angles
    roll, pitch, yaw = euler_from_quaternion([orientation.x, orientation.y, orientation.z, orientation.w])

    # Create a trajectory message
    traj = MultiDOFJointTrajectory()
    traj.header.stamp = rospy.Time.now()
    traj.joint_names.append("firefly2::base_link")

    traj1 = MultiDOFJointTrajectory()
    traj1.header.stamp = rospy.Time.now()
    traj1.joint_names.append("firefly3::base_link")

    # Create a trajectory point and set the received position and yaw angle
    point = MultiDOFJointTrajectoryPoint()
    point.transforms.append(get_pose_transform(position.x, position.y, position.z, yaw))
    traj.points.append(point)

    point1 = MultiDOFJointTrajectoryPoint()
    point1.transforms.append(get_pose_transform1(position.x, position.y, position.z, yaw))
    traj1.points.append(point1)

    # Publish the trajectory
    pub.publish(traj)
    pub1.publish(traj1)

def get_pose_transform(x, y, z, yaw):
    # Create a transform message with the received position and yaw angle
    transform = Transform()
    yaw_n = yaw-m.pi/2
    transform.translation.x = x+2*(m.cos(yaw_n)+m.sin(yaw_n))
    transform.translation.y = y+2*(m.sin(yaw_n)-m.cos(yaw_n))
    transform.translation.z = z+1
    q = quaternion_from_euler(0, 0, yaw)
    transform.rotation.x = q[0]
    transform.rotation.y = q[1]
    transform.rotation.z = q[2]
    transform.rotation.w = q[3]
    return transform

def get_pose_transform1(x, y, z, yaw):
    # Create a transform message with the received position and yaw angle
    transform = Transform()
    yaw_n = yaw-m.pi/2
    transform.translation.x = x-2*(m.cos(yaw_n)-m.sin(yaw_n))
    transform.translation.y = y-2*(m.sin(yaw_n)+m.cos(yaw_n))
    transform.translation.z = z+1
    q = quaternion_from_euler(0, 0, yaw)
    transform.rotation.x = q[0]
    transform.rotation.y = q[1]
    transform.rotation.z = q[2]
    transform.rotation.w = q[3]
    return transform

if __name__ == '__main__':
    rospy.init_node('pose_listener', anonymous=True)
    
     # Subscribe to the pose topic of firefly2
    rospy.Subscriber('/firefly1/ground_truth/pose', Pose, callback)

    # Create a ROS publisher to send the trajectory commands
    pub = rospy.Publisher('/firefly2/command/trajectory', MultiDOFJointTrajectory, queue_size=10)
    pub1 = rospy.Publisher('/firefly3/command/trajectory', MultiDOFJointTrajectory, queue_size=10)

    rospy.spin()

