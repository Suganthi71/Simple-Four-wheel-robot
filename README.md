# Four-Wheel Robot Project

This repository contains the source code and URDF files for a four-wheel robot using ROS2.

## Project Structure

ros2_ws/
├── src/
│   ├── urdf_test/                # Robot description package
│   │   ├── CMakeLists.txt
│   │   ├── package.xml
│   │   ├── launch/               # ROS2 launch files
│   │   │   └── robot_launch.py
│   │   ├── include/              # Header files (if any)
│   │   ├── src/                  # Source code (nodes, scripts)
│   │   │   └── robot_node.py
│   │   └── urdf/                 # Robot URDF files
│   │       └── robot.urdf
│   └── my_camera_pkg/            # Camera or sensor package
│       ├── CMakeLists.txt
│       ├── package.xml
│       ├── launch/
│       ├── include/
│       └── src/
├── .gitignore                    # Ignore build/install/log files
├── README.md                     # Project overview and instructions
├── build/                        # Auto-generated build files (ignored)
├── install/                      # Auto-generated install files (ignored)
└── log/                          # Logs (ignored)

## How to Run

Launch the robot using:
ros2 launch urdf_test <launch_file>.launch.py

## Notes

Only source code and URDF files are tracked in this repository.
Build, install, and log directories are ignored via .gitignore.
