import os
from launch import LaunchDescription
import launch_ros.actions

def generate_launch_description():
    return LaunchDescription([
        
        launch_ros.actions.Node(
            package='turtlesim', executable='turtlesim_node', output='screen'
        ),

        
        launch_ros.actions.Node(
            package='tf2_ros', executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', '/world', '/turtle1']
        ),

        
        launch_ros.actions.Node(
            package='turtle_navigation', executable='turtle_controller.py', output='screen'
        ),
    ])