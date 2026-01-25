# Experiment 1 - ROS2 Hello World

This experiment demonstrates basic ROS2 node creation and communication using Python.

## Package Overview
- **hello_world**: A Python package demonstrating basic ROS2 publisher/subscriber patterns

## How to Build and Run

### 1. Build the workspace:
```bash
cd exp-1-ros
colcon build --packages-select hello_world
```

### 2. Source the workspace:
```bash
source install/setup.bash
```

### 3. Run the nodes:
```bash
# Run the publisher
ros2 run hello_world bye_world

# Run the subscriber (in another terminal)
ros2 run hello_world bye_worldrecive

# Run the vowels node (in another terminal)
ros2 run hello_world bye_vouwals
```

## Features
- Basic publisher/subscriber communication
- Topic remapping capabilities
- Parameter passing
- Message filtering (vowels detection)

## Topics
- `chatter1` / `chatter2` - String messages for communication

## Dependencies
- `rclpy` - ROS2 Python client library
- `std_msgs` - Standard message types
