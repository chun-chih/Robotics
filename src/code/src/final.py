#!/usr/bin/env python

import rospy
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
import math as m 

def waypoints_callback(data):
    # Check if the received path contains enough waypoints
    if len(data.poses) >= 10:
        # Extract the first 10 waypoints
        waypoints = data.poses[:10]

        # Create a file path to save the waypoints
        file_path = "/home/chunchih/final_proj/src/code/src/waypoints.txt"

        # Open the file in write mode
        with open(file_path, "w") as file:
            # Iterate over each waypoint
            for i, waypoint in enumerate(waypoints):
                # Extract the position and orientation data
                position = waypoint.pose.position

                # Write the data to the file in the desired format
                file.write(f"{i*2} {position.x} {position.y} 4 0 \n")

        rospy.loginfo("Waypoints saved to waypoints.txt")

def main():
    # Initialize the ROS node
    rospy.init_node("waypoints_saver")

    # Subscribe to the /waypoints topic
    rospy.Subscriber("/waypoints", Path, waypoints_callback)

    # Spin the ROS node
    rospy.spin()

if __name__ == "__main__":
    main()