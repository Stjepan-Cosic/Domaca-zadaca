from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
def generate_launch_description():
    return LaunchDescription([
Node(
    package='rviz2',
    namespace='',
    executable='rviz2',
    name='rviz2'
),
Node(
    package='turtlesim',
    executable='turtlesim_node',
    name='sim'
),
Node(
    package='dz5',
    executable='turtle_tf2_broadcaster',
    name='broadcaster1',
    parameters=[
        {'turtlename': 'turtle1'}
    ]
),
Node(
    package='dz5',
    executable='goal_broadcaster',
    name='goal_broadcaster',
),
DeclareLaunchArgument(
    'target_frame', default_value='2d_goal_tf',
    description='Target frame name.'
),
Node(
        package='dz5',
        executable='turtle_controller',
        name='follower',
        parameters=[
            {'target_frame': LaunchConfiguration('target_frame')}
        ]
    ),
])
