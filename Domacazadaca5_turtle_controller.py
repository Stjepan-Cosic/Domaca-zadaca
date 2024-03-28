import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, PoseStamped
from tf2_ros import TransformBroadcaster
from math import atan2
from tf2_geometry_msgs import TransformStamped
import tf2_ros

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.cmd_vel_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pose_sub = self.create_subscription(PoseStamped, '/turtle1/pose', self.pose_callback, 10)
        self.goal_pose_sub = self.create_subscription(PoseStamped, '/move_base_simple/goal', self.goal_pose_callback, 10)
        self.tf_broadcaster = TransformBroadcaster(self)

    def pose_callback(self, msg):
        turtle_pose = msg.pose
        angular_speed = 0.5
        linear_speed = 0.5

        
        desired_angle = atan2(self.goal_pose.position.y - turtle_pose.position.y,
                              self.goal_pose.position.x - turtle_pose.position.x)
        current_angle = atan2(2 * (turtle_pose.orientation.w * turtle_pose.orientation.z + turtle_pose.orientation.x * turtle_pose.orientation.y),
                              1 - 2 * (turtle_pose.orientation.y**2 + turtle_pose.orientation.z**2))
        angular_error = desired_angle - current_angle
        while angular_error > 3.14159:
            angular_error -= 2 * 3.14159
        while angular_error < -3.14159:
            angular_error += 2 * 3.14159
        angular_vel = angular_error * angular_speed

        
        distance = ((self.goal_pose.position.x - turtle_pose.position.x) ** 2 +
                    (self.goal_pose.position.y - turtle_pose.position.y) ** 2) ** 0.5
        linear_vel = min(linear_speed, distance)

        
        twist_msg = Twist()
        twist_msg.angular.z = angular_vel
        twist_msg.linear.x = linear_vel
        self.cmd_vel_pub.publish(twist_msg)

    def goal_pose_callback(self, msg):
        self.goal_pose = msg.pose

def main(args=None):
    rclpy.init(args=args)
    turtle_controller = TurtleController()
    rclpy.spin(turtle_controller)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
