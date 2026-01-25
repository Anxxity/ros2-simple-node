# Experiment 2 - ROS2 Timer

This experiment demonstrates ROS2 timer-based periodic operations using Python.

## Package Overview
- **timerfr**: A Python package demonstrating timer-based node operations

## How to Build and Run

### 1. Build the workspace:
```bash
cd exp-2-ros
colcon build --packages-select timerfr
```

### 2. Source the workspace:
```bash
source install/setup.bash
```

### 3. Run the timer node:
```bash
ros2 run timerfr tim
```

## Features
- Periodic timer callbacks
- Time-based message publishing
- ROS2 node lifecycle management

## Dependencies
- `rclpy` - ROS2 Python client library
- `std_msgs` - Standard message types

## Usage
The timer node demonstrates:
- Creating ROS2 timers with custom periods
- Publishing messages at regular intervals
- Proper node initialization and shutdown
