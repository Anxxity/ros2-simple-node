# ROS2 Simple Node Tutorial

This directory contains a complete tutorial for creating a basic ROS2 node using C++.

## Package Overview
- **simplenode**: A basic C++ ROS2 node demonstrating fundamental concepts

## How to Build and Run

### 1. Build the workspace:
```bash
cd "ros2-creating _simple_node"
colcon build --packages-select simplenode
```

### 2. Source the workspace:
```bash
source install/setup.bash
```

### 3. Run the simple node:
```bash
ros2 run simplenode simplenode
```

## Package Structure

```
simplenode/
├── package.xml          # Package metadata and dependencies
├── CMakeLists.txt       # Build configuration
├── src/
│   └── simplenode.cpp   # Main node implementation
└── include/
    └── simplenode/      # Header files
```

## Features Demonstrated
- Basic ROS2 node initialization
- C++ node creation with `rclcpp::Node`
- Proper node lifecycle management
- CMake build system configuration

## Dependencies
- `rclcpp` - ROS2 C++ client library
- CMake build system
- C++17 or later

## Learning Objectives
This tutorial teaches:
1. How to structure a ROS2 C++ package
2. Basic node creation and initialization
3. CMake configuration for ROS2 packages
4. Package.xml setup for dependencies

## Next Steps
- Add publishers and subscribers
- Implement service clients/servers
- Add parameters and configuration
- Create launch files for complex scenarios
