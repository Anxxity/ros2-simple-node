# Launch Files Directory

This directory contains ROS2 launch files for starting multiple nodes with specific configurations.

## Files
- `launcher.py` - Main launch file for hello_world package nodes

## How to Use

### 1. Build the workspace first:
```bash
# From the parent directory containing hello_world package
colcon build --packages-select hello_world
source install/setup.bash
```

### 2. Run the launch file:
```bash
ros2 launch launch_file launcher.py
```

## Launch File Configuration

The `launcher.py` file starts:
- **bye_world** node: Publisher with custom message parameter
- **bye_vouwals** node: Vowels processing node

### Features:
- **Parameter passing**: Custom message configuration
- **Topic remapping**: `chatter1` remapped to `chatter2`
- **Screen output**: All node output displayed in terminal

### Configuration Options:
- Message parameter: `'hello can you here me'`
- Topic remapping: `chatter1` → `chatter2`

## Creating Custom Launch Files

To modify the launch configuration:
1. Edit `launcher.py`
2. Add/remove nodes as needed
3. Adjust parameters and remappings
4. Re-run with `ros2 launch launch_file launcher.py`

## Dependencies
- `launch` - ROS2 launch framework
- `launch_ros` - ROS2-specific launch actions
- `hello_world` package must be built and sourced
