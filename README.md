# Four-Wheel Robot Project

This repository contains the source code and URDF files for a four-wheel robot using ROS2.

## Project Structure

ros2_ws/
├── src/
│ ├── urdf_test/ # Robot description and packages
│ │ ├── CMakeLists.txt
│ │ ├── package.xml
│ │ ├── launch/ # Launch files
│ │ ├── include/ # Header files
│ │ ├── src/ # Source code
│ │ └── urdf/ # Robot URDF files
│ └── my_camera_pkg/ # Camera package
├── .gitignore # Git ignore file

## How to Run

Launch the robot using:
ros2 launch urdf_test <launch_file>.launch.py

## Notes

Only source code and URDF files are tracked in this repository.
Build, install, and log directories are ignored via .gitignore.
