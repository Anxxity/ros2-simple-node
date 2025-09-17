# 🤖 ROS 2 (Humble) Python Node - Quickstart Guide

This is a simple ROS 2 (Humble) workspace setup and a basic Python node example using `rclpy`.



## 🛠️ Workspace Setup

bash
# Source ROS 2
```
source /opt/ros/humble/setup.bash
```
# Create workspace and source folder
```
mkdir -p ~/ros2_ws/src

cd ~/ros2_ws/src
```
# Create a Python package (replace <pkg_name>)
```
ros2 pkg create --build-type ament_python <pkg_name> --dependencies rclpy std_msgs

```
# Build the workspace
```
cd ~/ros2_ws
colcon build
source install/setup.bash

```

# 🛠️ Custom ROS 2 Node Creation (Python)

## 📌 Steps Overview

1. Import ROS 2 Libraries  
2. Create a Node Class  
3. Initialize the ROS 2 System  
4. Spin the Node (Keep it Running)  
5. Shutdown Cleanly



## 🔹 Step-by-Step Breakdown

### 1️⃣ Import ROS 2 Libraries

python
#!/usr/bin/env python3  # Shebang line to indicate Python 3

import rclpy             # Core ROS 2 Python library
from rclpy.node import Node  # Base Node class


### Create a Custom Node Class
```
class SimpleNode(Node):
    def __init__(self):
        super().__init__('simple_node')  # Initialize node with name
        self.get_logger().info('SimpleNode has been started')  # Print to console

```

### Initialize the ROS 2 System and Spin the Node
```
def main(args=None):
    rclpy.init(args=args)    # Initialize ROS 2 system
    node = SimpleNode()      # Create node instance
    rclpy.spin(node)         # Keep the node alive

```
### Shutdown Cleanly

```
    node.destroy_node()      # Destroy the node
    rclpy.shutdown()         # Shutdown the ROS system

```
