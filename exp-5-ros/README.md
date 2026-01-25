# Experiment 5 - Advanced ROS2 Communication

This experiment demonstrates advanced ROS2 communication patterns and includes bag file recording capabilities.

## Package Overview
- **hello_world**: Enhanced version with additional communication patterns
- **exp_bag/**: Directory containing experiment-specific bag recordings

## How to Build and Run

### 1. Build the workspace:
```bash
cd exp-5-ros
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

### 4. Record experiment data:
```bash
# Record all topics
ros2 bag record -a

# Record specific topics
ros2 bag record chatter1 chatter2
```

### 5. Play back recorded data:
```bash
ros2 bag play <bag_directory>
```

## Features
- Advanced publisher/subscriber patterns
- Bag file recording and playback
- Topic remapping and parameter passing
- Message filtering and processing

## Topics
- `chatter1` / `chatter2` - String messages for communication

## Dependencies
- `rclpy` - ROS2 Python client library
- `std_msgs` - Standard message types

## Bag Files
The `exp_bag/` directory contains recordings from this experiment for analysis and replay.
