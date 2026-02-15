#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import PoseStamped


class TrajectoryPLotter(Node):

    def __init__(self):
        super().__init__("trajectory_plotter")
        self.declare_parameter("odom_topic", "bumperbot_controller/odom")
        odom_topic = self.get_parameter("odom_topic")
        self.odom_sub_ = self.create_subscription(Odometry, str(odom_topic.value), self.odometryCallback, 10)
        self.trajectory_pub_ = self.create_publisher(Path, "bumperbot_controller/trajectory", 10)
        self.trajectory_ = Path()
        
    def odometryCallback(self, msg):
        self.trajectory_.header.frame_id = msg.header.frame_id
        cur_pose = PoseStamped()
        cur_pose.header.frame_id = msg.header.frame_id
        cur_pose.header.stamp = msg.header.stamp
        cur_pose.pose = msg.pose.pose
        self.trajectory_.poses.append(cur_pose)
        
        self.trajectory_pub_.publish(self.trajectory_)


def main():
    rclpy.init()

    trajectory_plotter = TrajectoryPLotter()
    rclpy.spin(trajectory_plotter)
    
    trajectory_plotter.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()