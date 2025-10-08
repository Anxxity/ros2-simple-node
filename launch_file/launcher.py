from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='hello_world',
            executable='bye_world',
            name='bye_world',
            output='screen',
            parameters=[{'message':'hello can you here me'}],
            remappings = [('chatter1','chatter2')]
            
        ),
          Node(
            package='hello_world',
            executable='bye_vouwals',
            name='bye_recivevouwals',
            output='screen',
           # parameters=[{'message':'hello can you here me'}],
            remappings = [('chatter1','chatter2')]
            
        )
       #  Node(
       #     package='hello_world',
       #     executable='bye_worldrecive',
       #     name='bye_worldrecive'
       # ),
       # Node(
       #     package='timerfr',
       #     executable='tim',
       #     name='timer'
       # ),

    ])
