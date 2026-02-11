import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from nav_msgs.msg import Path
from nav_msgs.msg import Odometry


class TrajectoryPublisher():
    
    def __init__(self):
        super().__init__("trajectory_publisher")
        self.pub_ = self.create_publisher(Path, "/bumperbot_controller/trajectory", 10)
        self.sub_ = self.create_subscription(Odometry, "/bumperbot_controller/odom", self.odomCallback,  10)
        
        
    def odomCallback(self, msg):
        pass
        
        