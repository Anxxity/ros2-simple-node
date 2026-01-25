# Bag Files Directory

This directory contains ROS2 bag files for recording and playing back robot data.

## Structure
- `rosbag2_2025_09_25-15_00_40/` - Recorded bag file from September 25, 2025
- `subset/` - Subset of recorded data

## How to Use

### Play a bag file:
```bash
ros2 bag play <bag_directory_name>
```

### Record a new bag:
```bash
ros2 bag record <topics>
```

### Inspect bag contents:
```bash
ros2 bag info <bag_directory_name>
```

## Notes
- Bag files contain recorded ROS2 topics and messages
- Useful for testing, debugging, and data analysis
- Ensure sufficient disk space when recording
